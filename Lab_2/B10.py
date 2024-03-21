Phim=input("Nhập thể loại phim(Hành động, Kinh dị, Tình cảm, Hài hước, Hoạt hình): ")
Thời_gian=input("Nhập thời gian muốn xem phim(Sáng, Trưa, Chiều, Tối): ")
if Phim =="Hành động":
    if Thời_gian == "Sáng" or Thời_gian == "Trưa" or Thời_gian == "Chiều" or Thời_gian == "Tối":
        print("Phim Hành động được chiếu vào mọi khung giờ trong ngày.")
    else:
        print("Không có suất chiếu.")
elif Phim == "Kinh dị":
    if Thời_gian == "Tối":
        print("Phim Kinh dị được chiếu vào buổi tối.")
    else:
        print("Không có suất chiếu.")
elif Phim == "Tình cảm":
    if Thời_gian == "Tối":
        print("Phim Tình cảm được chiếu vào buổi tối.")
    else:
        print("Không có suất chiếu.")
elif Phim == "Hài hước":
    if Thời_gian == "sáng" or Thời_gian == "trưa":
        print("Phim Hài hước được chiếu vào buổi sáng và trưa.")
    else:
        print("Không có suất chiếu.")
elif Phim == "Hoạt hình":
    if Thời_gian == "sáng" or Thời_gian == "trưa":
        print("Phim Hoạt hình được chiếu vào buổi sáng và trưa.")
    else:
        print("Không có suất chiếu.")
else:
    print("Thể loại phim không hợp lệ.")