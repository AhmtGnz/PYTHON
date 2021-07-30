asal = [2]
i = 3

while len(asal) < 10001:

    for x in range(2,i):
        bolundu = False
        if i%x == 0:
            bolundu = True
            break
        else:
            continue

    if bolundu == False:
        asal.append(i)
            
    i += 1


print(len(asal))
print("cevap:",asal[-1])