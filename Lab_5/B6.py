chuoi = input("Nhập chuỗi: ")
ky_tu_dac_biet = []
so_lan_xuat_hien = {}
tong_so_ky_tu = len(chuoi)
for ky_tu in chuoi:
    if not ky_tu.isalnum(): 
        ky_tu_dac_biet.append(ky_tu)
        if ky_tu in so_lan_xuat_hien:
            so_lan_xuat_hien[ky_tu] += 1
        else:
            so_lan_xuat_hien[ky_tu] = 1
print("Các ký tự đặc biệt trong chuỗi:", ky_tu_dac_biet)
print("Số lần xuất hiện của từng ký tự đặc biệt:")
for ky_tu, so_lan in so_lan_xuat_hien.items():
    print(f"'{ky_tu}': {so_lan} lần")
ty_le_phan_tram = {ky_tu: (so_lan / tong_so_ky_tu) * 100 for ky_tu, so_lan in so_lan_xuat_hien.items()}
print("Tỷ lệ phần trăm của mỗi ký tự đặc biệt trong chuỗi:")
for ky_tu, ty_le in ty_le_phan_tram.items():
    print(f"'{ky_tu}': {ty_le:.2f}%")
