n=float(input("Nhập vào số điểm của bạn:"))
if 0<=n<=5:
    print("Điểm Kém!!!")
elif 5<n<=7:
    print("Điểm Trung Bình!!!")
elif 7<n<=8.5:
    print("Điểm Khá!!!")    
elif 8.5<n<=10:
    print("Điểm Tốt!!!")
else:
    print("Điểm của bạn không hợp lệ!!!")