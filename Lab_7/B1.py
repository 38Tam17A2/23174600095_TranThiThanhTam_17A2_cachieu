N = int(input("Nhập số nguyên N: "))
if N <= 0:
    print("N phải là một số nguyên dương.")
else:
    Tên_sinh_viên = {x: x ** 3 for x in range(1, N + 1)}
    print("Từ điển dạng như sau:")
    print(Tên_sinh_viên)
