file_nguon = input("Nhập đường dẫn file nguồn: ").strip()
file_dich  = input("Nhập đường dẫn file đích: ").strip()
kich_thuoc_khoi = 1024 
with open(file_nguon, "rb") as f_in, open(file_dich, "wb") as f_out:
    while True:
        data = f_in.read(kich_thuoc_khoi)
        if data == b"": 
            break
        f_out.write(data)
print("Đã sao chép xong!")