A = [[1,2],[3,4]]
B = [[5,6],[7,8]]
C = []
i = 0
for b in A:
    hang = []
    j = 0
    for b in B[0]:
        tong = 0
        k = 0
        for b in B:
            tong += A[i][k] * B[k][j]
            k += 1
        hang.append(tong)
        j += 1
    C.append(hang)
    i += 1
print("Ma trận tích:", C)
