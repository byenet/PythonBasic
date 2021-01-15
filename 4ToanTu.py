'''Toan tu so hoc co ban (giong c++ (+,-,*,/,%,...) nhung khac mot vai cho duoi day: '''
print(9 / 2)  # ra ket qua 4.5 lay so le luon thay vi chi lay so nguyen la 4 giong c++
print(9 // 2)  # phep chia lay nguyen se ra ket qua la 4
print(9 % 2)  # phep chia lay du nhu trong c++
print(9 ** 2)  # ** la phep luy thua nhanh se ra ket qua 81

print("." * 40)  # in 40 lan dau cham de cach cho de doc

'''Toan tu gan thi tuong tu c++ va bo sung them mot so phep gan tren:
 =; +=; -=; *=; /=; //=; %=; **=.
 '''

'''Toan tu so sanh cung tuong tu c++ va bo sung them hai doi tuong la is va is not:
 ==; !=; <; <=; >; >=; is; is not
 '''
x=5
y=5

print(x==y)
print (x!=y)

print (x is y)  #True neu cac bien cung tro toi mot gia tri hoac cung gia tri bang nhau neu khong trỏ vè dalse
print (x is not y)# Nguoc lai voi is

print("." *40)

'''
    Toan tu logic cach hieu thi giong c++ nhung cu phap thi khac chung ta viet ra luon:
    and; or; not
'''

h=2016
print(h%4==0 and h%100!=0)
print(h%4==0 or h%100!=0)
if(not h>=5):
    print("false")
else:print("true")






