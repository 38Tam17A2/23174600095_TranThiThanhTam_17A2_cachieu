a=float(input("Nhập hệ số góc của đường thẳng 1: "))
b=float(input("Nhập vào hệ số tự do của đường thẳng 1: "))
c=float(input("Nhập hệ số góc của đường thẳng 2: "))
d=float(input("Nhập vào hệ số tự do của đường thẳng 2: "))
Góc_giữa_hai_đường_thẳng=abs(a-c)
if Góc_giữa_hai_đường_thẳng == 0:
    print("Hai đường thẳng là đường thẳng song song!!!")
elif Góc_giữa_hai_đường_thẳng == 90:
    print("Hai đường thẳng là đường thẳng vuông góc!!!")
else:
    print("Hai đường thẳng là đường thẳng cắt nhau!!!")
    