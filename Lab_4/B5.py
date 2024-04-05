import math
while True:
    a=float(input("Nhập vào số thứ nhất: "))
    b=float(input("Nhập vào số thứ hai: "))
    Phép_cộng=a+b
    Phép_trừ=a-b
    Phép_nhân=a*b
    Phép_chia=a/b
    Số_mũ=a**b
    căn_bậc_hai_a=math.sqrt(a)
    căn_bậc_hai_b=math.sqrt(b)
    print("Kết quả cộng:", Phép_cộng)
    print("Kết quả trừ:", Phép_trừ)
    print("Kết quả nhân:", Phép_nhân)
    print("Kết quả chia:", Phép_chia)
    print("Kết quả lũy thừa:", Số_mũ)
    print("Căn bậc hai của số thứ nhất:", căn_bậc_hai_a)
    print("Căn bậc hai của số thứ hai:", căn_bậc_hai_b)
    choice = input("Bạn có muốn tiếp tục không? (y/n): ")
    if choice.lower() != "y":
        break
    