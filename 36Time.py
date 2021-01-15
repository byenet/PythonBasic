import time

start = time.time()
x=int(input("Moi ban nhap vao 1 gia tri: "))
for x in range(x):
    time.sleep(0.5)
    print(x,end='')
end = time.time()

duration = end - start
print('\nduration = ',duration)

print('-'*40)
print("seconds = ", time.time())
print("Local time: ", time.ctime())
print("Local time: ", time.ctime(time.time()))
print("Local time: ", time.ctime(1610711000))


result = time.localtime(1610711000)
print("result:", result)
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)

# https://viblo.asia/p/module-time-trong-python-07LKXeBkZV4