chuoi = input("Nhập chuỗi (độ dài hơn 10 ký tự): ")
if len(chuoi) <= 10:
    print("Độ dài chuỗi phải lớn hơn 10 ký tự.")
else:
    chuoi_con = chuoi[4:9]
    print("Chuỗi ký tự con gồm 5 ký tự kể từ vị trí thứ 5:", chuoi_con)
