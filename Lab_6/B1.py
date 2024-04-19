n = int(input("Nhập số phần tử của mảng: "))
a = []
for i in range(n):
    num = int(input(f"Nhập phần tử thứ {i+1}: "))
    a.append(num)
sum_1 = 0
sum_2 = 0
for num in a:
    if num % 2 == 0:
        sum_1 += num
    else:
        sum_2 += num
print("Tổng các số chẵn trong mảng:", sum_1)
print("Tổng các số lẻ trong mảng:", sum_2)