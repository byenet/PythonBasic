
print(end="Nhap diem trung binh: ")
dtb = float(input())
if dtb >= 9:
    print("Xep loai gioi")
elif dtb >= 7:
    print("Xep loai kha")
elif dtb >= 5:
    print("Xep loai trung binh")
else:
    print("Xep loai yeu")
