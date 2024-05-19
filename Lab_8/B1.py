limit = 1000
e = []
for num in range(2, limit):
    m = True
    if num > 2:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                m = False
                break
    elif num == 2:
        m = True
    else:
        m = False
    if m:
        e.append(num)
print("Các cặp số nguyên tố sinh đôi nhỏ hơn", limit, "là:")
for i in range(len(e) - 1):
    if e[i+1] - e[i] == 2:
        print(e[i], e[i+1])
