a = [1, 2, 3, 4, 5]
tong_chan = 0
tong_le = 0
for i in a:
    if i % 2 == 0:
        tong_chan += i
    else:
        tong_le += i
print("Tổng chẵn:", tong_chan)
print("Tổng lẻ:", tong_le)