a = int(input("Nhap so nguyen: "))
s = 0
for n in range(5,10):
    if 4%a == 1:
        print("Ngung for")
        break
    s+=n;
else:
    print("Sum = ",s)