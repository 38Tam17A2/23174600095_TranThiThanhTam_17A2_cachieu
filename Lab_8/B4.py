n = 36
divisors = [i for i in range(1, n) if n % i == 0]
sum_divisors = sum(divisors)
print(sum_divisors) 
