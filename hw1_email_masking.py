# hw1_email_masking.py

# 1.Nhập dữ liệu
email =input("Nhập gmail vào đây:" )

# 2.Xử lí dữ liệu
cat = email.split('@')
# split() : tách chuỗi thành 1 danh sách
tach = email[0:3]
# sciling[] : trích xuất những từ muốn hiện 
che = "***"+email[10:]
ket_hop = tach+che

# 3.In ra kết quả
print("\n--- BIÊN LAI ĐIỆN TỬ ---")
print(f": {ket_hop}")

