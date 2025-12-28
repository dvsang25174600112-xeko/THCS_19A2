list_int = [2, 4, 5, 6]
with open(r"C:\Users\Windows\Desktop\VSC\Chương 13\bài 3\so_nguyen.txt", "w") as file:
    for i in list_int:
        file.write(f"{i} \n")
with open(r"C:\Users\Windows\Desktop\VSC\Chương 13\bài 3\so_nguyen.txt", "r", encoding='utf-8') as file:
    noi_dung = file.read()
print(noi_dung)