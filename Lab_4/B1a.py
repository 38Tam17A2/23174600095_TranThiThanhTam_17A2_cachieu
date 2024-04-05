sum = 0
n = []
while sum <= 1000:
    a = int(input("Nhập một số nguyên dương: "))
    if a % 2 != 0:
        n.append(a)
    sum += a
print("Các số lẻ đã nhập:")
for a in n:
    print(a)