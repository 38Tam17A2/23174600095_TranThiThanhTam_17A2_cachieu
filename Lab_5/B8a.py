chuoi = input("Nhập chuỗi (độ dài hơn 10 ký tự): ")
if len(chuoi) <= 10:
    print("Độ dài chuỗi phải lớn hơn 10 ký tự.")
else:
    chuoi_con = chuoi[1:8]
    print("Chuỗi ký tự con từ vị trí thứ 2 đến vị trí thứ 8:", chuoi_con)
