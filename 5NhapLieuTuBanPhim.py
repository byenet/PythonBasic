'''
    Trong python nhap lieu dung ham input(). Gia tri nhap vao cua ham input
thuong la kieu chuoi. Do do can chuyen kieu neu nhu muon luu tru gia tri nhap
vao khong phai kieu chuoi
'''

print(end="Moi ban nhao vao mot cai gi do: ")
s=input()
print("Ban vua nhap: ",s)
print("Kieu du lieu ban vua nhap la: ",type(s))
print("\n")

# Dua kieu du lieu vua nhap ve int:
print(end="Moi ban nhap int: ")
x=int(input())
print("ban vua nhap: ",x)
print("Kieu du lieu ban vua nhap: ",type(x))
print("\n")

# Dua kieu du lieu vua nhap ve float:
print(end="Moi ban nhap float: ")
y=float(input())
print("ban vua nhap: ",y)
print("Kieu du lieu ban vua nhap: ",type(y))
print("\n")

# Dua ve so boolean: (cach nay phai viet ham, se nghien cuu ki sau)
def StrToBool(s):
    return s.lower() in ("yes", "true", "t", "1")

print(end="Moi ban nhap kieu bool: ")
a=StrToBool(input())
print("Ban vua nhap: ", a)
print("Kieu du lieu: ", type(a))
print("\n")

#Vua nhap vua in nhan nhan tieu de:
t = input("Moi ban nhap gia tri gi do:")
print("Ban vua nhap: ",t)
print("\n")
