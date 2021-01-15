while True:
    x = int(input("Nhap vao so: "))
    print(x," la so chan " if x % 2==0 else " la so le")
    hoi = input("Tiep tuc chuong trinh khong? (c/k): ")
    if hoi == "k":
        break;
print("Bye! hen gap lai");

n = int(input("Nhap N: "))
s = 0;
for x in range(1,n+1):
    s+=x
    if s >= 15:
         break
print("S= ", s)
