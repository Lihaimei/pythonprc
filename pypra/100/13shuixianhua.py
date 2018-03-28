"""打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数本身。
例如：153是一个“水仙花数”，因为153=1的三次方＋5的三次方＋3的三次方。"""

"""import math
for i in range(100,1000):
    a = math.floor(i/100)
    b = math.floor((i-a*100)/10)
    c = (i-math.floor(i/10))/10
    if i == (a**3 + b**3 + c**3):
        print(i,end=',')"""

 for i in range(100,1000):
     a = i//100
     b = (i%100)//10
     c =i%10
     if i == a**3+b**3+c**3:
         print(i)


https://www.lijinlong.cc/python/pyxt/1525.html