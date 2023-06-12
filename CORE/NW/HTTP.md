# `ris:FileText`HTTP介绍
#HTTP
超文本传输协议：规定Brower和Server之间的数据传输规则

特点：
- 基于TCP
- 基于Request-Response：一次请求一次响应
- 无状态：没有记忆，每次request-response都是独立的

缺点：
- 多次请求不能共享数据
> 为解决此问题，JavaWeb使用了Coookie和Session这样的会话技术

工具推荐：Postman

# HTTP格式

## Request 

请求行：请求方式+资源路径
>请求方式
>> GET
>> POST
> 资源路径

#HTTP/GET #HTTP/POST
> GET和POST的区别：
> GET请求参数位于请求行；而POST请求参数位于请求体
> GET限制了请求参数的大小；而POST没有


请求头：key:value
- HOST: 主机名
- User-Agent: 浏览器版本（用于处理浏览器兼容性问题，对不同的浏览器采取不同的响应）
- Accept: 浏览器可接受的资源类型
- Accept-Language: 浏览器偏好语言
- Accept-Encoding: 浏览器支持的压缩格式

请求体：
针对POST请求的最后一部分，存放请求参数

## Response

响应行：协议版本+状态码
> 1xx: 响应中
> 2xx: 成功
> 3xx: 重定向
> 4xx: 客户端响应错误
> 5xx: 服务器响应错误

响应头：key:value 
- Content-Type: 响应内容的类型
- Content-Length: 响应内容的长度
- Content-Encoding: 响应内容的压缩算法
- Cache-Control: 客户端缓存方式

响应体：存放响应数据

