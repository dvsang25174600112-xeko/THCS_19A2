A = {1,2,3}
B = {3,4,5}
giao = set()
A_B = set()
B_A = set()
hop = set()
for x in A:
    hop.add(x)
    if x in B:
        giao.add(x)
    else:
        A_B.add(x)
for x in B:
    hop.add(x)
    if x not in A:
        B_A.add(x)
print("Giao:", giao)
print("A - B:", A_B)
print("B - A:", B_A)
print("Hợp:", hop)
