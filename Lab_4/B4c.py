n = int(input("Nhập số nguyên n (n > 10): "))
a = 1 
sum_S3=0
while a <= n:
    term = (-1) ** a * a ** 2  
    sum_S3 += term  
    a += 1 
print("Tổng S3 =", sum_S3)