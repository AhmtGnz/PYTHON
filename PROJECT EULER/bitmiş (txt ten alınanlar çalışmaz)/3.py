while True:
    sayı = 600851475143

    for i in range(2,sayı+1):
        while sayı%i == 0:
            
            sayı = sayı/i
            if sayı == 1:
                print("Cevap: ",i)
                break
