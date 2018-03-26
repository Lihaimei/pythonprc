from urllib.request import urlopen
values ={
    "token":"a24becfad6d86c1492586cedc1e155c7",
    "room_title":"13240的聊天室",
    "city_name":"上海",
    "platform":"",
    "templet":"1",
    "v_num":""
}
response = urlopen('http://192.168.26.18:10011v1/chatroom/create',values)
#urlopen(url,data,timeout)2参3参可不传
print (response.read())