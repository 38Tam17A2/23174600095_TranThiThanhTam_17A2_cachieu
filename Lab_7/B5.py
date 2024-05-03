kho = {
    "banana": 6,
    "apple": 5,
    "orange": 32,
    "pear": 15
}
gia_tien = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
mua_hang = {
    "banana": 2,
    "apple": 3,
    "orange": 1,
    "pear": 2
}
tong_tien = 0
print("Hóa đơn:")
for item, quantity in mua_hang.items():
    if item in kho:
        if kho[item] >= quantity:  
            gia = gia_tien[item] * quantity
            tong_tien += gia
            print(f"{quantity} {item} - Đơn giá: {gia_tien[item]} - Thành tiền: {gia}")
            kho[item] -= quantity 
        else:
            print(f"Không đủ hàng cho {item}")
print("Tổng tiền:", tong_tien)
