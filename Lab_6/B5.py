e = input("Nhập dãy số, cách nhau bằng dấu cách: ")
numbers = e.split()
numbers = [int(num) for num in numbers]
i = True
difference = numbers[1] - numbers[0]
for i in range(2, len(numbers)):
    if numbers[i] - numbers[i-1] != difference:
        i = False
        break
if i:
    print("Dãy số", numbers, "là cấp số cộng.")
else:
    print("Dãy số", numbers, "không tạo thành cấp số cộng.")