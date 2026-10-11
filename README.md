# Quản lý điểm sinh viên

Ứng dụng Streamlit minh họa quản lý điểm cho 10 sinh viên.

## Chức năng
- Hiển thị bảng điểm và xếp loại.
- Tính điểm tổng kết theo công thức: 20% chuyên cần + 30% giữa kỳ + 50% cuối kỳ.
- Thống kê điểm trung bình, cao nhất, thấp nhất và số sinh viên đạt.
- Tra cứu điểm từng sinh viên bằng Selectbox.
- Vẽ biểu đồ cột điểm tổng kết.
- Hiển thị thông tin người thực hiện ở cuối trang.

## Chạy ứng dụng trên máy tính

1. Cài Python 3.10 trở lên.
2. Mở Terminal/CMD tại thư mục dự án.
3. Cài thư viện:

   ```bash
   pip install -r requirements.txt
   ```

4. Chạy ứng dụng:

   ```bash
   streamlit run app.py
   ```

## Đưa lên GitHub và triển khai Streamlit Community Cloud

1. Tạo một repository mới trên GitHub, ví dụ `quan-ly-diem-sinh-vien`.
2. Tải lên `app.py`, `requirements.txt` và `README.md`.
3. Mở https://share.streamlit.io/ và đăng nhập bằng GitHub.
4. Chọn **Create app**, chọn repository, branch `main`, và file chính `app.py`.
5. Nhấn **Deploy**.

Trước khi công khai ứng dụng, hãy sửa dòng thông tin cuối `app.py` thành họ tên và MSSV thật của bạn.

## Lưu ý
Dữ liệu điểm hiện là dữ liệu minh họa được khai báo trực tiếp trong `app.py`. Đây chưa phải ứng dụng lưu trữ dữ liệu lâu dài hay chỉnh sửa điểm qua giao diện.
