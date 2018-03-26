#判断101-200之间有多少个素数，并输出所有素数
#用101到200之间的数去整除2到该数前面的一个数；

b = 0#个数
for i in range(101,200):
    k = 0
    for j in range(2,i):
        if i%j ==0:
            k +=1
    if k == 0:
            print(i)
            b +=1
print("素数一共有",b,"个")
