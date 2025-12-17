n = [1, 5, 3, 9, 7]
max1 = None
max2 = None
for x in n:
    if max1 is None or x > max1:
        if x != max1:
            max2 = max1
        max1 = x
    elif x != max1:
        if max2 is None or x > max2:
            max2 = x
print("Số lớn thứ hai:", max2)