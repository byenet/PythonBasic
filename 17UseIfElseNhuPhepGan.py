a = 5
b = 7

""" Day la doan code binh thuong
    if a!b:
        c = 113
    else: 
        c = 115
    print(c)
"""

#Day la doan code khi dung if else nhu phep gan:

c = 113 if a!=b else 115
print(c);

# VD tiep theo

x = int(input("Nhap mot so: "))
print("Chan" if x%2==0 else "Le")