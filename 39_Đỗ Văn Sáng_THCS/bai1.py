import math
n = int(input("Nhập số cần kiểm tra:"))
if math.sqrt(n) ** 2 == n:
    print(n, "là số chính phương")
else:
    print(n, "không là số chính phương")