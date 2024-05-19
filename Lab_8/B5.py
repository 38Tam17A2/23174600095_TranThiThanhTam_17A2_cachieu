a = 220
b = 284
divisors_a = [i for i in range(1, a) if a % i == 0]
sum_divisors_a = sum(divisors_a)
divisors_b = [i for i in range(1, b) if b % i == 0]
sum_divisors_b = sum(divisors_b)
e = (sum_divisors_a == b) and (sum_divisors_b == a)
print(f"{a} và {b} là số amicable: {e}")
