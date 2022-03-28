with open('data_2.txt', 'r') as f:
    d = f.read()
    occ = dict()
    for chr in d:
        occ[chr]=occ.get(chr, 0) + 1
print(sorted(occ.items(), key=lambda x: x[1]))