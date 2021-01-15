print("Nhap 1 so [1..10]")
x = -1;
while x<1 or x>10:
    x=int(input("Nhap [1..10]: "))
print(x**2)


n = int(input("Nhap N: "))
s=0
i=0
while i<=n:
    s+=i
    i+=1
print("Tong =",s)