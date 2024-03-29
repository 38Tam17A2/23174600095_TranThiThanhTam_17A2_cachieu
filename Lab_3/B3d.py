for n in range(1,501):
    Sum = 0
    for i in range(1, n):
        if n % i == 0:
            Sum +=i
    if Sum == n:
        print(n)