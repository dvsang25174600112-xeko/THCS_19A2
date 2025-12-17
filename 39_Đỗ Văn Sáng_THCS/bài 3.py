chuoi = input("Nhập chuỗi: ")
kq = ""
space = True
for i in chuoi:
    if i != " ":
        kq += i
        space = False
    else:
        if not space:
            kq += " "
        space = True
print(kq)
