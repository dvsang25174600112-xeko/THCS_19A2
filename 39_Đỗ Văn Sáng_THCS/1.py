def chuyen_nhiet_do(do_c):
    do_f = (do_c * 9/5) + 32
    return do_f
n = int(input("Nhập số n:"))
if int(n**0.5)**2 == n:
    print("là số chính phương")
else:
    print("không phải số chính phương")