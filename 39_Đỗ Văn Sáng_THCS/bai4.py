n = int(input("nhập n:"))
for x in range(2, n):
    kiemtra = True
    for i in range(2, x):
        if x % i == 0:
            kiemtra = False
            break
    if kiemtra == True:
        print(x, end= " ")