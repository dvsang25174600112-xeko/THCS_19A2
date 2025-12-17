chuoi = input("Nhập chuỗi: ")
n = int(input("Nhập n: "))
tu = ""
dem = 0
for i in chuoi + " ":
    if i != " ":
        tu += i
        dem += 1
    else:
        if dem > n:
            print(tu)
        tu = ""
        dem = 0