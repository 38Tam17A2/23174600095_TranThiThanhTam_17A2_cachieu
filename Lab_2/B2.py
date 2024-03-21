n=int(input("Nhập một số nguyên: "))
chữ_số_hàng_nghìn= n//1000
if chữ_số_hàng_nghìn == 0:
    print("Số không có chữ số hàng nghìn!!!")
elif 0 < chữ_số_hàng_nghìn <= 9:
    print("Chữ số hàng nghìn là:",chữ_số_hàng_nghìn)
else:
    phan_du = chữ_số_hàng_nghìn % 100
    if phan_du == 0:
        print("Chữ số hàng nghìn là:",0)
    else:
        print("Chữ số hàng nghìn là:",phan_du)