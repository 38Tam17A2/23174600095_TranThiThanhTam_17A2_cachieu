a = []
n = int(input("Nhập số phần tử trong mảng: "))
for i in range(n):
    num = int(input(f"Nhập phần tử thứ {i+1}: "))
    a.append(num)
print("Các số nguyên tố trong mảng là:")
for num in a:
    if num > 1:
        is_prime = True
        for i in range(2, int(num/2)+1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)
print("Các số hoàn hảo trong mảng là:")
for num in a:
    if num > 1:
        divisors = []
        for i in range(1, num):
            if num % i == 0:
                divisors.append(i)
        if sum(divisors) == num:
            print(num)