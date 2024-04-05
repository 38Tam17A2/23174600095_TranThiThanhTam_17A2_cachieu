n = 2
while n < 100:
    a = True
    m = 2
    while m <= n // 2:
        if n % m == 0:
            a = False
            break
        m += 1
    if a:
        print(n)
    n += 1