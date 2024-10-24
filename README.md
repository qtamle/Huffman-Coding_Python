## Nén dữ liệu bằng huffman

### Tổng quan ###
- **main.py**!
Tệp "main.py" đóng vai trò là điểm khởi đầu của chương trình. Nó nhận đường dẫn ảnh đầu vào và điều phối việc gọi các chức năng được mô tả trong các thành phần khác của chương trình. Các chức năng này kết thúc bằng việc nén và giải nén nội dung chữ và ảnh thông qua ứng dụng các nguyên tắc mã hóa Huffman.

- **huffman_coding.py**:
Module "huffman_coding.py" chứa các hàm thực hiện mã hóa Huffman một cách cẩn thận. Các hàm này bao gồm việc tính toán tần suất byte trong ảnh đầu vào, xây dựng cây Huffman, lấy mã Huffman, và thiết lập liên kết byte với mã. Thông qua các thuật toán này, mã hóa Huffman được thực hiện, tối ưu hóa việc biểu diễn dữ liệu với sự quan tâm đến phân bố tần suất ký tự.

- **binary_data_handler.py**:
Module "binary_data_handler.py" quản lý dữ liệu nhị phân. Nó bao gồm các hàm để đọc và ghi các tệp hình ảnh và ký tự. Dữ liệu nhị phân được đọc từ ảnh, chữ đầu vào và kết quả nén hoặc giải nén sẽ được ghi vào tệp đầu ra.

### Hướng dẫn cài đặt
- **Bước 1: Cài đặt**
  - 1. Clone repo:
```git clone ```
- **Bước 2: cài đặt thêm**
  - 1. Đảm bảo bạn đã cài đặt Python 3.x trên máy tính.
  - 2. Cài đặt các gói phụ thuộc bằng cách chạy lệnh.
- **Step 3: Sử dụng**
  - 1. Khởi chạy công cụ bằng lệnh: ```python main.py```
  - 2. Nén một ảnh:
      Nén một ảnh: Nhấn nút "Nén ảnh" trong giao diện. 
      Chọn ảnh mà bạn muốn nén. Công cụ sẽ xử lý ảnh bằng thuật toán Huffman và hiển thị kết quả ảnh đã nén
  - 3.Giải nén một ảnh:
      Nhấn nút "Giải nén ảnh" trong giao diện. 
      Chọn tệp ảnh nén mà bạn muốn giải nén. Công cụ sẽ khôi phục ảnh gốc từ dữ liệu nén và hiển thị kết quả giải nén.
  - 4. Nén chữ:
      Nhập chữ bạn muốn nén vào giao diện
      Nén chữ: Nhấn nút "Nén chữ" trong giao diện. 
      Công cụ sẽ xử lý chữ bằng thuật toán Huffman và hiển thị kết quả chữ đã nén ra tệp.
  - 5.Giải nén chữ:
      Nhấn nút "Giải nén chữ" trong giao diện. 
      Công cụ sẽ khôi phục chữ gốc từ dữ liệu nén và hiển thị kết quả giải nén.

- **Bước 4: Kiểm tra**
  - Huffman Codes:
Công cụ này tạo ra các mã Huffman cho mỗi ký hiệu trong quá trình nén. Bạn có thể tìm thấy các mã này trong tệp "huffman_codes.txt" nằm trong thư mục "IO/Outputs.

###  Lỗi đang gặp phải

- **Lỗi nếu nén ảnh trước, sau đó nén chữ thì tại file huffman_code_text sẽ bị trùng với file huffman_code_image, Những khi decompress chữ thì vẫn ra kết quả đúng**
```Đã thử khắc phục bằng cách chia ra lưu 2 file riêng khi nén nhưng vẫn không được.```
