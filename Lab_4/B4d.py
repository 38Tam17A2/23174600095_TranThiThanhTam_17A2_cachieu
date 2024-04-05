n = int(input("Nhập số nguyên n (n > 10): "))
a = 1
sum_s4 = 0
while True:
    s4 = a * (a + 1) * (a + 2)
    if s4 > n:
        break
    sum_s4 += s4
    a += 1
print("Tổng S4 =", sum_s4)