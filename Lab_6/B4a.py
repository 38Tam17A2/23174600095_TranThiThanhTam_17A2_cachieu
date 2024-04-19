n = int(input("Nhập số lượng số Fibonacci muốn tạo: "))
fibonacci_list = [0, 1] if n > 1 else [0] if n == 1 else []   
[fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2]) for _ in range(2, n)]
print("Danh sách", n, "số Fibonacci đầu tiên là:", fibonacci_list)