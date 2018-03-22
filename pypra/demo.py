import urllib.request

request1 = urllib. request("http://www.baidu.com")
response = urllib.urlopen(request1)  #urlopen(url,data,timeout)2参3参可不传
print (response.read())