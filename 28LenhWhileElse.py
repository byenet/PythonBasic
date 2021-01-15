count = sum = 0;
print("Nhap 5 so >= 0 de tinh gia tri trung binh")
while count < 5:
    val = int(input("Nhap gia tri: "))
    if val < 0:
        print("Nhap sai quy tac")
        break
    sum+=val
    count+=1
else:
    print("Trung Binh = ", sum/count)