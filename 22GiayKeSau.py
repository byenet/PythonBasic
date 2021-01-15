t = int(input("Nhap vao so giay ban muon tinh: "))
hour = (t//3600)%24
minute = (t%3600)//60
second = (t%3600)%60
print("Thoi gian ban da nhap la:",hour,":",minute,":",second)

second += 1
if second >= 60:
    minute += 1
    second = 0

if minute >= 60:
    hour += 1
    minute = 0

print("Thoi gian ban nhap sau 1 giay la:", hour, ":", minute, ":", second)

