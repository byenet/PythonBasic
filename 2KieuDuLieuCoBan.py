
""" Khai bao bien va kieu du lieu: ( Trong python khong can khai bao kieu du lieu cho bien, khi ta gan gia tri cho bien
thi python se tu dong noi suy ra kieu du lieu cua bien. Nen mot bien trong python co the co nhieu kieu du lieu tuy thuoc
vao gia tri chung ta gan.
"""

print("Cac kieu du lieu co trong python: ")
x = 5
print("Kieu của 5 la:", type(x))
x = 'teo'
print("Kieu cua teo la:", type(x))
x = True
print("Kieu cua True la:", type(x))
x = 5.5
print("Kieu cua 5.5 la:", type(x))
x = complex(113, 114)
print("Kieu cua 113 + 114i la: ", type(x))
print("Phan thuc la:", x.real ,",Phan ao la:", x.imag)

# Xoa bien bang cu phap del name (del x)

# Cach kiem tra vung luu tru:

import sys
print("\n Vung du lieu: ")
print("Thong tin chi tiet cua int: ")
print(sys.int_info)
print("Thong tin chi tiet cua float: ")
print(sys.float_info)




