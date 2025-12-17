a = [1, 2, 3, 4, 5]
n = int(input("Nhập tổng k: "))
i = 0
while i < 4:
    j = i + 1
    while j < 5:
        if a[i] + a[j] == n:
            print(a[i], a[j])
        j += 1
    i += 1