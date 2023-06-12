一般作为前端服务器

# 基本原理
[[服务器基本原理]]

# Nginx概述
[深入浅出Nginx](https://zhuanlan.zhihu.com/p/34943332)
一款轻量级的Web服务器，反向代理服务器（也可作正向代理，但用的比较少），占内存少，启动快，高并发。
![[Pasted image 20230411100711.png|500]]


# 使用
目录结构：
![[Pasted image 20230421162439.png|300]]
配置端口：
conf目录下的nginx.conf，修改server对象listen端口

## 实现反向代理
#反向代理 
配置nginx.conf
linux安装的nginx配置文件一般在/usr/local/nginx/conf目录下
```conf
server{
	listhen 8086;
	server_name localhost;
 
# 资源根目录
	location / {
		 root html;
		 index index.html index.htm;
	}
# 当请求localhost:8086/api/...时,
# 会自动访问192.168.17.130:8080/api/...
	location /api/ {
		proxy_pass http://192.168.17.130:8080/;
	}
}
```


## 负载均衡
#负载均衡 





