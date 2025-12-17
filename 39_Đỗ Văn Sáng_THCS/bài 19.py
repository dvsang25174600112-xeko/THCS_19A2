ten_diem = {'An':8,'Binh':7,'Chi':8}
kq = {}
for ten in ten_diem:
    diem = ten_diem[ten]
    if diem in kq:
        kq[diem].append(ten)
    else:
        kq[diem] = [ten]

print(kq)
