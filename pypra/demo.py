from urllib.request import urlopen


response = urlopen('http://www.baidu.com ') #urlopen(url,data,timeout)2参3参可不传
print (response.read())