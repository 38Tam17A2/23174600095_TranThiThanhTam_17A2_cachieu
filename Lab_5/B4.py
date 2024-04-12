chuoi = input("Nhập chuỗi ký tự: ")
chuoi_chi_so = ''.join(filter(str.isdigit, chuoi))
if chuoi_chi_so.isdigit():
    so_nguyen = int(chuoi_chi_so)
    if so_nguyen <= 1:
        la_so_nguyen_to = False
    else:
        la_so_nguyen_to = True
        for i in range(2, int(so_nguyen**0.5) + 1):
            if so_nguyen % i == 0:
                la_so_nguyen_to = False
                break
    if la_so_nguyen_to:
        print(f"{so_nguyen} là số nguyên tố.")
    else:
        print(f"{so_nguyen} không phải là số nguyên tố.")
else:
    print("Chuỗi không chứa số nguyên.")