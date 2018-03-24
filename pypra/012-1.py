#判断101-200之间有多少个素数，并输出所有素数
#用101到200之间的数去整除2到该数前面的一个数；

for i in range(101,201):
    for j in range(2,i):
        if i%j ==0:
            break
        else:
            print(i)




