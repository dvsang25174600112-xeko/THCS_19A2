a = [1, 2, 2, 3, 1, 4]
b = []
for x in a:
    ton_tai = False
    for y in b:
        if x == y:
            ton_tai = True
    if not ton_tai:
        b.append(x)
print("Danh sách sau khi loại trùng:", b)