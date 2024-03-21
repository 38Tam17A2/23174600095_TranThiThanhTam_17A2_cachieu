a,b=map(int,input("Nhập vào hệ số của phương trình: ").split())
if a == 0:
    if b == 0:
        print("Phương trình bậc nhất cả vô số nghiệm!!!")
    else:
        print("Phương trình bậc nhất đã cho vô nghiệm!!!")
else:
    x=-b/a
    print("Phương trình có nghiệm duy nhất x=",x)
       