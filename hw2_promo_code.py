# hw2_promo_code,py

# 1. Nhập dữ liệu
ho_ten = input("Nhập họ và tên: ")
nam = int(input("Nhập năm sinh: "))

# 2. Xử lí dữ liệu
cat = ho_ten.split()
ten = cat[-1]
# split : dùng để tách chuỗi thành danh sách

ten_moi = ten[:3].upper()
# [] này là slicing dùng để trích xuất từ mong muốn
# upper() : dùng viết hoa toàn bộ từ đó

# f-string : nối chuỗi

# 3. Xuất kết quả
print(f"{ten_moi}-{nam}-VIP")
