import csv
with open("nhan_vien.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "Tên", "Lương"])
    writer.writerow([1, "Long", 45000])
    writer.writerow([2, "Linh", 52000])
    writer.writerow([3, "Hùng"])          # thiếu lương
    writer.writerow([4, "Dũng", 50000])
with open("nhan_vien.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["Lương"] is None or row["Lương"] == "":
            continue  # bỏ qua dòng thiếu lương
        luong = float(row["Lương"])
        if luong > 50000:
            print(f"ID: {row['ID']}, Tên: {row['Tên']}, Lương: {row['Lương']}")
