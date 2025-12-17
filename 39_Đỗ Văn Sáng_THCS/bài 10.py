a = [[1,2],[3,4],[5,6]]
max_tong = None
hang = 0
i = 0
for b in a:
    tong = 0
    for x in b:
        tong += x
    if max_tong is None or tong > max_tong:
        max_tong = tong
        hang = i
    i += 1
print("Hàng có tổng lớn nhất:", hang)
