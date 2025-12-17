d = {'a':10,'b':50,'c':30}
max_k = None
max_v = None
for k in d:
    if max_v is None or d[k] > max_v:
        max_v = d[k]
        max_k = k
print("Key có giá trị lớn nhất:", max_k)
