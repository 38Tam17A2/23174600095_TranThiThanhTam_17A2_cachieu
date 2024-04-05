n = int(input("Nhập số nguyên n (n > 10): "))
a = 0
S2 = 0
while True:
    S2 = 1 / (3**(2*a+1))
    a += 1
    if S2 <= n:
        break
print("Các tổng S2:",S2)