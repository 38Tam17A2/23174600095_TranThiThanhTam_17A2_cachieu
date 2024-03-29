a, b = 0, 1
for i in range(100):
    if b >= 100:
        break
    print(b)
    a, b = b, a + b