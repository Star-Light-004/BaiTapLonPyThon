import time
import schedule
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

# Dùng Tesseract để hỗ trợ đọc mã captcha
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Hàm để xử lí ảnh captcha 
def preprocess_image(captcha_img):
    captcha_img = captcha_img.convert('L')
    enhancer = ImageEnhance.Contrast(captcha_img)
    captcha_img = enhancer.enhance(2)
    captcha_img = captcha_img.resize((captcha_img.width * 2, captcha_img.height * 2))
    captcha_img = captcha_img.filter(ImageFilter.MedianFilter())
    captcha_img = captcha_img.point(lambda p: p > 150 and 255)

    return captcha_img

# Hàm check phạt nguội
def check_phat_nguoi(bienso):
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
#    1. Vào website đã chọn.
    try:
        driver.get("https://www.csgt.vn/tra-cuu-phuong-tien-vi-pham.html")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "BienKiemSoat")))
#     2. Nhập các thông tin Biển số xe, chọn loại phương tiện
        # Nhập biển số
        bien_input = driver.find_element(By.NAME, "BienKiemSoat")
        bien_input.clear()
        bien_input.send_keys(bienso)

        # Chọn xe máy
        Select(driver.find_element(By.NAME, "LoaiXe")).select_by_value("2")

        # 3. Trích xuất mã bảo mật bằng thư viện pytesseract hoặc thư viện nào đó ra dạng text rồi nhập tự động vào ô Input
        # Đợi ảnh CAPTCHA xuất hiện
        captcha_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "imgCaptcha"))
        )
        # Chụp ảnh CAPTCHA bằng Selenium
        captcha_screenshot = captcha_element.screenshot_as_png
        captcha_img = Image.open(BytesIO(captcha_screenshot))

        # xử lý ảnh
        captcha_img = preprocess_image(captcha_img)

        # Nhận diện văn bản Captcha
        captcha_text = pytesseract.image_to_string(
            captcha_img, config='--oem 3 --psm 7 -c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ).strip().replace(" ", "").replace("\n", "")

        print(f" Capcha đọc được: {captcha_text}")

        # Nhập CAPTCHA vào ô input
        captcha_input = driver.find_element(By.NAME, "txt_captcha")
        captcha_input.clear()
        captcha_input.send_keys(captcha_text)

        # 4. Kiểm tra kết quả phạt nguội.
        driver.find_element(By.CLASS_NAME, "btnTraCuu").click()

        # Chờ kết quả
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "result"))
        )

        result = driver.find_element(By.ID, "result").text
        print(f"Kết quả {bienso}: {result.strip()}")

    except Exception as e:
        print(f"Lỗi: {str(e)}")
    finally:
        driver.quit()

def job():
    bien_so = "74H18072"
    check_phat_nguoi(bien_so)
# Em dùng hàm này để kiểm tra ngay sau khi run code
def main():
    print("Kiểm tra ")
    job()

   #5. Set lịch chạy 6h sáng và 12h trưa hằng ngày
    schedule.every().day.at("06:00").do(job)
    schedule.every().day.at("12:00").do(job)

    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()
