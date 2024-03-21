a,b,c=map(int,input("Nhập vào các số tương ứng: ").split())
if a>=b and a>=c:
    if b>=c:
        print("Số lớn thứ hai là:",b)
    else:
        print("Số lớn thứ hai là:",c)
elif b>=a and b>=c:
    if a>=c:
        print("Số lớn thứ hai là:",a)
    else:
        print("Số lớn thứ hai là:",c)
else:
    if a>=b:
        print("Số lớn thứ hai là:",a)
    else:
        print("Số lớn thứ hai là:",b)