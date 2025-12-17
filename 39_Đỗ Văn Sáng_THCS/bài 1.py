chuoi = input("Nhập chuỗi: ")
chu = 0
so = 0
d_biet = 0
for i in chuoi:
    if ('a' <= i <= 'z') or ('A' <= i <= 'Z'):
        chu += 1
    elif '0' <= i <= '9':
        chu += 1
    else:
        d_biet += 1
print("Chữ cái:", chu)
print("Chữ số:", so)
print("Ký tự đặc biệt:", d_biet)

