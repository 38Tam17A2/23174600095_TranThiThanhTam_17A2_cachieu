chuoi = input("Nhập chuỗi (độ dài hơn 10 ký tự): ")
if len(chuoi) <= 10:
    print("Độ dài chuỗi phải lớn hơn 10 ký tự.")
else:
    chuoi_con = chuoi[-3:]
    print("Chuỗi ký tự con từ cuối chuỗi gồm 3 ký tự:", chuoi_con)
