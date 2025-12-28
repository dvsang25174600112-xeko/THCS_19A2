with open("van_ban.txt", 'r', encoding="utf-8") as f:
    noi_dung = f.read()
so_tu = noi_dung.split()
print("Tổng số từ:", len(so_tu))