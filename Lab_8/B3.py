n = 123
cubesum = sum([int(digit) ** 3 for digit in str(n)])
print("Tổng của các lập phương của các chữ số của", n, "là:", cubesum)
for num in range(1, 1000):
    if sum([int(digit) ** 3 for digit in str(num)]) == num:
        print(num, "là số Armstrong")
n = 153
is_armstrong = sum([int(digit) ** 3 for digit in str(n)]) == n
print(n, "là số Armstrong:", is_armstrong)
