tan_suat = {}
with open("van_ban.txt", 'r', encoding="utf-8") as f:
    noi_dung = f.read()
tach_noi_dung_thanh_cac_tu = noi_dung.split()
for tu in tach_noi_dung_thanh_cac_tu:
    tu = tu.lower()          # đưa về chữ thường
    tu = tu.strip(".,")      # bỏ dấu . ,
    if tu in tan_suat:
        tan_suat[tu] = tan_suat[tu] + 1     #có rồi + 1
    else:
        tan_suat[tu] = 1     #chưa có gán = 1
for tu in tan_suat:
    print(tu, ":", tan_suat[tu])