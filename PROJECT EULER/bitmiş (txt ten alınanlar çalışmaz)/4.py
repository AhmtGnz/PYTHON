liste1 = range(100,999)
palindromik = []

for i in liste1[::-1]:
    for j in liste1[::-1]:
        çarpım = i*j
        ters = str(çarpım)
        ters = int(ters[::-1])
        if çarpım < 100000:
            continue
        else:
            if çarpım == ters:
                palindromik.append(çarpım)

palindromik.sort()
print(f"3 haneli çarpanları olan en büyük Palindromik sayı: ",palindromik[-1])
