chuoi = input("Nhập chuỗi văn bản: ")
tu_can_tim = input("Nhập từ cần tìm kiếm: ")
vi_tri = chuoi.find(tu_can_tim)
if vi_tri != -1:
    print(f"Từ '{tu_can_tim}' xuất hiện ở vị trí: {vi_tri}")
else:
    print(f"Từ '{tu_can_tim}' không xuất hiện trong chuỗi.")
tu_nhieu_nhat = max(chuoi.split(), key=chuoi.split().count)
so_lan_xuat_hien_nhieu_nhat = chuoi.split().count(tu_nhieu_nhat)
print(f"Từ xuất hiện nhiều nhất trong chuỗi là '{tu_nhieu_nhat}', xuất hiện {so_lan_xuat_hien_nhieu_nhat} lần.")