toan = float(input("Nhap vao diem toan: "))
ly = float(input("Nhap vao diem ly: "))
hoa = float(input("Nhap vao diem hoa: "))
dtb = (toan+ly+hoa)/3
print("Diem trung binh khi chua lam tron: ",dtb)

# Lam tron so  bang ham round
print("Diem trung binh sau khi lam tron 2 chu so thap phan: ",round(dtb,2))
