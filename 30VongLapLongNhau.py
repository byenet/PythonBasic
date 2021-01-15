n = int(input("Nhap vao chieu cao N: "))
for i in range(n):
    for j in range(n):
        if j==0 or i==j or j==n-1:
            print("*", end='')
        else:
            print(' ', end='')
    print()

print("#"*30)

a =0
while a<n:
    b = 0
    while b<n:
        if b == 0 or a == b  or b == n-1:
            print("#", end ='')
        else:
            print(' ', end='')
        b+=1
    a+=1
    print()