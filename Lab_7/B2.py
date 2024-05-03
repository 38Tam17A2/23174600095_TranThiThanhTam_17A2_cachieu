students = {}
for i in range(1, 11):
    print(f"Nhập thông tin của sinh viên thứ {i}:")
    name = input("Tên sinh viên: ")
    while True:
        u= input("Điểm thi: ")
        if u.replace('.', '', 1).isdigit() and 0 <= float(u) <= 10:
            A = float(u)
            break
        else:
            print("Điểm thi phải là số và nằm trong khoảng từ 0 đến 10.")
    students[name] = A
Điểm = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
for name, A in students.items():
    if A >= 8.5:
        Điểm["A"] += 1
    elif A >= 7.0:
        Điểm["B"] += 1
    elif A >= 5.5:
        Điểm["C"] += 1
    elif A >= 4.0:
        Điểm["D"] += 1
    else:
        Điểm["F"] += 1
print("\nThống kê số lượng sinh viên ở mỗi loại học lực:")
for grade, count in Điểm.items():
    print(f"{grade}: {count} sinh viên")
