chuoi = input("Nhập chuỗi (độ dài hơn 10 ký tự): ")
if len(chuoi) <= 10:
    print("Độ dài chuỗi phải lớn hơn 10 ký tự.")
else:
    chuoi_chu_hoa = chuoi.upper()
    print("Chuỗi sau khi chuyển đổi các ký tự thành chữ hoa:", chuoi_chu_hoa)
