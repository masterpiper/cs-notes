# TCP
应用层报文基本格式
```
URL:
Method:
Params:
```

## GET vs POST
GET用来从服务器获取数据
POST向服务器上传参数
|                | GET                         | POST                               |
|:--------------:| --------------------------- | ---------------------------------- |
| 退出、刷新按钮 | 无害                        | 数据不被重新提交                   |
|      书签      | 可收藏                      | 不可收藏                           |
|     coding     |                             |                                    |
|      历史      | 参数保留浏览器历史          | 参数不会保留                       |
|    数据长度    | URL最长2048字符             | 无限制                             |
|    数据类型    | 只允许ASCII                 | 无限制，允许二进制                 |
|     安全性     | 不安全发送数据时URL的一部分 | 安全，参数不会保存在浏览器和服务器 |
|     可见性     | 数据在URL对所有人可见       | 数据不会显示于URL                  |
```
# when params are : name=qiming.c, age=22

GET /index.php?name=qiming.c&age=22 HTTP/1.1  
Host: localhost

 POST /index.php HTTP/1.1
Host: localhost   
 Content-Type: application/x-www-form-urlencoded name=qiming. c&age=22
```
