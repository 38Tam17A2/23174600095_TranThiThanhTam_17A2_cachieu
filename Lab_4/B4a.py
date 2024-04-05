n = int(input("Nhập vào số nguyên n (n > 10): "))
a = 0
sum = 0
m = 6
while sum <= n:
    sum += m ** a
    a += 1
print("Tổng S1 là:", sum)