while True:
    n=int(input("Nhap 1 so nguyen duong: "))
    dem = 0
    for i in range(1, n+1):
        if n%i == 0:
            dem+=1
    if dem == 2:
        print(n,"La so nguyen to")
    else:
        print(n,"Khong la so nguyen to")
    hoi=input("Ban cô muon tiep tuc chuong trinh khong? (c/k): ")
    if hoi == 'k':
        break
print("Bye bye!")