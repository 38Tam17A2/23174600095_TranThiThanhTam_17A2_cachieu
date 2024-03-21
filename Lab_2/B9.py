import math
a=float(input("Nhập hệ số góc của đường thẳng: "))
b=float(input("Nhập hệ số tự do của đường thẳng: "))
x=float(input("Nhập toạ độ x của tâm đường tròn: "))
y=float(input("Nhập toạ độ y của tâm đường tròn: "))
r=float(input("Nhập bán kính đường tròn: "))
Khoảng_cách_từ_tâm_đến_đường_thẳng=abs(a*x-y+b)/math.sqrt(a**2+1)
if Khoảng_cách_từ_tâm_đến_đường_thẳng < r:
    print("Đường thẳng cắt đường tròn!!!")
elif Khoảng_cách_từ_tâm_đến_đường_thẳng == r:
    print("Đường thẳng tiếp xúc đường tròn!!!")
else:
    print("Đường thẳng nằm ngoài đường tròn!!!")