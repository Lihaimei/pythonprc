#判断101-200之间有多少个素数，并输出所有素数
#用101到200之间的数去整除2到sqrt（这个数）；
import math
b =0
for i in range(101,200):
    k = 0
    a =int(math.sqrt(i))
    for j in range(2,a):
        if i%j ==0:
            k +=1
    if k ==0:
        print(i);
        b +=1
print("素数个数：",b,"个")
