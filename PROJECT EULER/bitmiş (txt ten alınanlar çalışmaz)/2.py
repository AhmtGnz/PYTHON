fibonacci = [1,2]
for i in range(2,400):
    fibonacci.append(fibonacci[i-2]+fibonacci[i-1])
    if fibonacci[i] > 4000000:
        fibonacci.pop()
        break

print("\nFibonacci Dizisi:\n",fibonacci)

çift = [k for k in fibonacci if k % 2 == 0]
toplam = 0
for j in çift:
    toplam += j
print("\nToplam = ",toplam) 
