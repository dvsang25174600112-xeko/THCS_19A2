a = [[1,2,3],[2,4,5],[3,5,6]]
doi_xung = True
i = 0
for row in a:
    j = 0
    for _ in row:
        if a[i][j] != a[j][i]:
            doi_xung = False
        j += 1
    i += 1
print("Ma trận đối xứng:", doi_xung)
