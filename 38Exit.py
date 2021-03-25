while True:
    n = int(input("Mời bạn nhập 1 số: "))
    dem = 0
    for i in range(1,n+1):
        if n % i == 0:
            dem+=1;
    if(dem == 2):
        print(n, "là số nguyên tố")
    else:
        print(n, "Không là số nguyên tố")
    print("Tiếp không?(c/k): ")
    if input() == "k":
        exit()
print("Bye!")