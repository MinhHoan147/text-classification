# text-classification


Giai đoạn huấn luyện:

 ![image](https://user-images.githubusercontent.com/72193415/170854642-ac2569ba-004e-4100-ab26-a50d72101914.png)

Trong đó:

	Ngữ liệu huấn luyện: dữ liệu đầu vào, chính là các đoạn văn bản người dùng muốn phân loại
  
	Tiền xử lý: chuyển đổi dữ liệu sao cho phù hợp 
  
	Vector hóa: mã hóa văn bản, chuyển đổi văn bản từ dạng text thành các mô hình trọng số  ví dụ như vector.
  
	Trích chọn đặc trưng: loại bỏ những đặc trưng dư thừa
  
	Thuật toán huấn luyện: mô hình machine learning mà ta sử dụng
  
	Đánh giá: đánh giá hiệu suất của bộ phân lớp
  
  
  Giai đoạn phân lớp:
  
  ![image](https://user-images.githubusercontent.com/72193415/170854793-622e246e-e400-499d-811f-8d72fa09badc.png)

--------------------------------------------------------------------------------------------------------
# Thuật toán Naive Bayes

![Screenshot (100)](https://user-images.githubusercontent.com/72193415/170854995-b39efb7e-0a54-4a50-bac1-03de2bfdd266.png)

  Các công thức trên là toàn bộ tư tưởng chung của thuật toán Naive Bayes, khác nhau ở chỉ ở chỗ tìm các phân phối để tính toán xác suất trên. Thực tế và đặc biệt là đối với dữ liệu dạng text thì các thành phần của x luôn luôn liên quan đến nhau để tạo ra ngữ cảnh. Nhưng kết quả mà thuật toán naive bayes mang lại rất khả quan (điều này cũng giải thích cho chữ naive - ngây thơ).
  Phân phối xác suất thường dùng cho các bài toán đa lớp là multinomial naive bayes

