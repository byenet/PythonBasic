print("Chuong trinh dem so ngay trong thang!!!")
month = int(input("Moi ban nhap vao thang muon tinh: "))
year = int (input("Moi ban nhap vao nam: "))
if month in (1,3,5,6,7,8,10,12):
    print("Thang",month,"nam",year,"co 31 ngay")
elif month in (4, 6, 9, 11):
    print("Thang", month, "nam", year, "co 30 ngay")
elif month ==  2:
    if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Thang", month, "nam", year, "la nam nhuan nen co 29 ngay")
    else:
        print("Thang", month, "nam", year, "khong phai nam nhuan nen co 28 ngay")
else:
    print("Thang",month,"ban nhap khong hop le")