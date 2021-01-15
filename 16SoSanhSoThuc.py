# Xem lai bai so cham dong trong c++ de hieu tại sao phai lam nhu the nay:

d1 = 1.11 - 1.10
d2 = 2.11 - 2.10
d3 = 1.111111111111111111111111111
d4 = 1.111111111111111111111111111

print('d3 = ',d3,'\n','d4 = ',d4,'\n','d1 = ',d1,'\n','d2 = ',d2);
print(d3 == d4);

diff = d1 - d2 #compute difference
if diff < 0: #compute absolute value
    diff = -diff

if diff < 0.0000001: # are the values close enough?
    print('Same');
else:
    print('Different')