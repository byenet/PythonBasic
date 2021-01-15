print("Chuong trinh Tim ngay ke sau va quy cua thang!!!")
day  = int(input("Moi ban nhap vao ngay: "))
month = int(input("Moi ban nhap vao thang: "))
year = int (input("Moi ban nhap vao nam: "))

day += 1
hople = 1

nhuan = 0
if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): nhuan = 1

if month in (1, 3, 5, 6, 7, 8, 10, 12) and day <= 31:
    if day >= 31: month+=1 ; day = 1
elif month in (4, 6, 9, 11) and day <= 30:
    if day >= 30: month+=1 ; day = 1
elif month == 2 and nhuan == 1 and day <= 29:
    if day >= 29: month += 1 ; day = 1
elif month == 2 and nhuan == 0 and day <= 28:
        if day >= 28: month += 1; day = 1
else:
    hople = 0

if month in (1,2,3): quy = 1
elif month in (4,5,6): quy = 2
elif month in (7,8,9): quy = 3
elif month in (10,11,12): quy = 4

if hople == 0: print("Ngay thang nam ma ban nhap khong hop le...")
else:
    print("Thoi gian ke sau: Ngay",day,"Thang",month,"Nam",year);
    print("Thuoc Quy",quy);
