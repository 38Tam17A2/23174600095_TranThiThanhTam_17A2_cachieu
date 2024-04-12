chuoi_1 = input("Nhập chuỗi thứ nhất: ")
chuoi_2 = input("Nhập chuỗi thứ hai: ")
chuoi_tron = ''
i = 0
while i < len(chuoi_1) or i < len(chuoi_2):
    if i < len(chuoi_1):
        chuoi_tron += chuoi_1[i]
    if i < len(chuoi_2):
        chuoi_tron += chuoi_2[i]
    if i < min(len(chuoi_1), len(chuoi_2)) - 1:
        chuoi_tron += '-'
    i += 1
print("Chuỗi sau khi trộn:", chuoi_tron)
