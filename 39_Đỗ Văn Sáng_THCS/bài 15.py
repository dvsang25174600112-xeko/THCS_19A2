n = (1,2,3,4,5)
chan = ()
le = ()
tong_chan = 0
tong_le = 0
for i in n:
    if i % 2 == 0:
        chan += (i,)
        tong_chan += i
    else:
        le += (i,)
        tong_le += i
print("Tuple chẵn:", chan, "Tổng:", tong_chan)
print("Tuple lẻ:", le, "Tổng:", tong_le)
