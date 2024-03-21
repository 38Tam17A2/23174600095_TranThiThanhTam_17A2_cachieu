Số_lượng_người=int(input("Nhập vào đây số lượng người tương thích:"))
Giá_vé=120000
Tổng_tiền= Số_lượng_người * Giá_vé
if Số_lượng_người >=2 and Số_lượng_người <=4:
    Tổng_tiền=(Số_lượng_người * Giá_vé)*0.95
elif Số_lượng_người >=5 and Số_lượng_người <=10:
    Tổng_tiền=(Số_lượng_người * Giá_vé)*0.9
elif Số_lượng_người >10:
    Tổng_tiền=(Số_lượng_người * Giá_vé)*0.8
else:
    print("Số lượng người không hợp lệ!!!")
print("Tổng số tiền phải trả là:", Tổng_tiền, "đồng")