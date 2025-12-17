a = [[1,2,3],[4,5,6],[7,8,9]]
n = 0
for b in a:
    n += 1
tong = 0
i = 0
while i < n:
    tong += a[i][n-1-i]
    i += 1
print("Tổng đường chéo phụ:", tong)
