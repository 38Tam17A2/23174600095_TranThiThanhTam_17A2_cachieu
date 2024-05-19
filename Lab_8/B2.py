import math
n = int(input("Nhập n: "))
r = int(input("Nhập r: "))
p_n_r = math.factorial(n) // math.factorial(n - r)
print(f"Số hoán vị của {n} phần tử lấy {r} phần tử mỗi lần: p({n}, {r}) = {p_n_r}")
c_n_r = p_n_r // math.factorial(r)
print(f"Số tổ hợp của {n} phần tử lấy {r} phần tử mỗi lần: c({n}, {r}) = {c_n_r}")
