a =  int(input("Moi ban nhap vao so < 1000 muon doi sang chu: "))
tram = a // 100
chuc = (a % 100)//10
dvi = (a % 100)%10


if tram == 0:   t = ""
elif tram == 1: t = "Mot Tram"
elif tram == 2: t = "Hai Tram"
elif tram == 3: t = "Ba Tram"
elif tram == 4: t = "Bon Tram"
elif tram == 5: t = "Nam Tram"
elif tram == 6: t = "Sau Tram"
elif tram == 7: t = "Bay Tram"
elif tram == 8: t = "Tam Tram"
elif tram == 9: t = "Chin Tram"


if tram == 0 and chuc == 0: ch = ""
elif tram > 0 and chuc == 0: ch = "Le"
elif chuc == 1: ch = "Muoi"
elif chuc == 2: ch = "Hai Muoi"
elif chuc == 3: ch = "Ba Muoi"
elif chuc == 4: ch = "Bon Muoi"
elif chuc == 5: ch = "Nam Muoi"
elif chuc == 6: ch = "Sau Muoi"
elif chuc == 7: ch = "Bay Muoi"
elif chuc == 8: ch = "Tam Muoi"
elif chuc == 9: ch = "Chin Muoi"

if dvi == 0:   dv = ""
elif dvi == 1: dv = "Mot"
elif dvi == 2: dv = "Hai"
elif dvi == 3: dv = "Ba"
elif dvi == 4: dv = "Bon"
elif dvi == 5 and chuc == 0: dv = "Nam"
elif dvi == 5 and chuc != 0: dv = "Lam"
elif dvi == 6: dv = "Sau"
elif dvi == 7: dv = "Bay"
elif dvi == 8: dv = "Tam"
elif dvi == 9: dv = "Chin"

print( "So",a,"Sau khi doi sang chu la: ")
print(t,ch,dv)

