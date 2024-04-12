chuoi = input("Nhập chuỗi (độ dài hơn 10 ký tự): ")
if len(chuoi) <= 10:
    print("Độ dài chuỗi phải lớn hơn 10 ký tự.")
else:
    chuoi_dao_nguoc = chuoi[::-1]
    print("Chuỗi sau khi đảo ngược:", chuoi_dao_nguoc)
