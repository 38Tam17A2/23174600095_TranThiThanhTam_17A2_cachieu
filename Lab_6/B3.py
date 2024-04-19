num = input("Nhập dãy số, cách nhau bằng dấu cách: ")
num_list = num.split()
if len(num_list) == 0:
    print("Dãy số rỗng.")
else:
    max_num = float(num_list[0])
    min_num = float(num_list[0])
    for num_str in num_list[1:]:
        f = False
        for char in num_str:
            if char.isdigit() or char == '.':
                f = True
            else:
                f = False
                break
        if f:
            num = float(num_str)
            if num > max_num:
                max_num = num
            if num < min_num:
                min_num = num
        else:
            print("Lỗi: '{}' không phải là một số hợp lệ.".format(num_str))
    print("Số lớn nhất trong dãy số là:", max_num)
    print("Số nhỏ nhất trong dãy số là:", min_num)
