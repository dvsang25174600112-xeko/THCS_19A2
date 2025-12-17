ihuoi = input("Nhập ihuỗi: ")
luu = {}
for i in ihuoi:
    if i in luu:
        luu[i] += 1
    else:
        luu[i] = 1
print(luu)
