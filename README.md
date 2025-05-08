# BaiTapLonPython
# Kiểm tra Phạt Nguội Tự Động

Đây là một ứng dụng Python tự động kiểm tra phạt nguội trên website CSGT Việt Nam bằng cách sử dụng Selenium, Tesseract OCR và thư viện `schedule` để tự động chạy vào các thời điểm nhất định. 

## Hướng dẫn Cài Đặt

Để cài đặt và chạy ứng dụng, cần thực hiện theo các bước sau:

1. Cài đặt các thư viện cần thiết bằng lệnh sau:

    ```bash
    pip install selenium pytesseract Pillow schedule
    ```

2. Cài đặt Tesseract OCR:
   - Tải và cài đặt [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) từ GitHub hoặc trang chính thức của nó.
   - Sau khi cài đặt Tesseract, bạn cần chỉ định đường dẫn tới Tesseract trong mã nguồn. Mở file `main.py` và thay đổi đường dẫn đến Tesseract tương ứng với hệ thống của bạn. Ví dụ, nếu bạn sử dụng Windows, đường dẫn mặc định thường là:
     ```python
     pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
     ```

3. Cài đặt WebDriver:
   - Tải [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) phù hợp với phiên bản Google Chrome bạn đang sử dụng.
   - Đảm bảo rằng `chromedriver` được thêm vào biến môi trường PATH của hệ thống hoặc bạn có thể chỉ định đường dẫn tới `chromedriver` trong mã nguồn.

4. Cấu hình và chạy ứng dụng:
   - Mở file `main.py` và thay đổi biển số xe mà bạn muốn kiểm tra phạt nguội (biển số mẫu trong mã là `74H18072`).
   - Để chạy ứng dụng, chỉ cần thực thi lệnh sau trong terminal hoặc command prompt:
     ```bash
     python PhatNguoiAuto.py
     ```
   - Ứng dụng sẽ tự động kiểm tra phạt nguội vào lúc 6h sáng và 12h trưa mỗi ngày. Chúng ta có thể thay đổi các thời gian này bằng cách chỉnh sửa các dòng sau trong mã:
     ```python
     schedule.every().day.at("06:00").do(job)
     schedule.every().day.at("12:00").do(job)
     ```

5. Giới thiệu về lịch trình:
   - Ứng dụng sử dụng thư viện `schedule` để lên lịch chạy kiểm tra phạt nguội vào các thời điểm đã định, ví dụ:
     - **06:00**: Kiểm tra phạt nguội.
     - **12:00**: Kiểm tra phạt nguội.
   - Ứng dụng sẽ chạy liên tục và tự động kiểm tra phạt nguội vào các thời gian đã cấu hình.

6. Ghi chú:
   - Ứng dụng yêu cầu máy tính có kết nối internet để truy cập website CSGT.
   - Đảm bảo rằng bạn đã cài đặt và cấu hình đúng Tesseract OCR để nhận diện mã CAPTCHA chính xác.
   - Ứng dụng hỗ trợ chạy trên hệ điều hành Windows hoặc các hệ điều hành khác hỗ trợ Python và Selenium.
7. Hạn chế:
   -  Trong bài làm em đang sử dụng ứng dụng và thư viện miễn phí nên nó không đọc được chính xác mã Captcha, nên sẽ không tránh khỏi những hạn chế và sai xót. Em 
      mong thầy thông cảm và góp ý thêm cho bài làm ạ. Em cảm ơn Thầy rất nhiều ạ
