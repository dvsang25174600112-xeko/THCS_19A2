tu = int(input("Nhập tử số:"))
mau = int(input("Nhập mẫu số:"))
a = tu
b = mau
while b != 0:
    a,b = b, a% b
uc = a
tu //= uc
mau //= uc
print("Phân số tối giản:", tu, "/", mau)