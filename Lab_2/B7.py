Cân_nặng=float(input("Nhập vào số cân nặng(kg)của bạn:"))
Chiều_cao=float(input("Nhập vào đây chiều cao(mét)của bạn:"))
BMI= Cân_nặng/(Chiều_cao**2)
print("Chỉ số BMI của bạn là: ",BMI)
if BMI <18.5:
    print("Gầy!!!")
elif 18.5<= BMI <=24.9:
    print("Bình thường!!!")
elif 25.0<= BMI <=29.9:
    print("Hơi mập!!!")
else:
    print("Mập xỉu!!!")