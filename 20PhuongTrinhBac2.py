from math import sqrt

print("Chuong trinh Giai phuong trrinh bac 2:")
a = float(input("Nhap a:"))
b = float(input("Nhap b:"))
c = float(input("Nhap c:"))
if a==0:
    if b == 0 and c == 0:
        print("Phuong trinh co vo so nghiem")
    elif b == 0 and c !=0:
        print("Phuong trinh vo nghiem")
    else:
        x = -c/b
        print("Phuong trinh co mot nghiem la: ",x);

else:
    delta = b**2-4*a*c
    if delta < 0:
        print("Phuong trinh vo nghiem")
    elif delta == 0:
        x = -b/(2*a)
        print("Phuong trinh co nghiem kep la x1=x2=",x)
    else:
        x1 = (-b - sqrt(delta)) / (2 * a)
        x2 = (-b + sqrt(delta)) / (2 * a)
        print("Phuong trinh co hai nghiem phan biet la: ")
        print("X1=",x1)
        print("X2=",x2)