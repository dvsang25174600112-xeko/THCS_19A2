a = [[1,0],[0,1]]
don_vi = True
i = 0
for b in a:
    j = 0
    for x in b:
        if (i == j and x != 1) or (i != j and x != 0):
            don_vi = False
        j += 1
    i += 1
print("Ma trận đơn vị:", don_vi)
