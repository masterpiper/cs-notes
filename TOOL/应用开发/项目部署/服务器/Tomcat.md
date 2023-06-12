# 知识背景

## URL and URI
URI=URL+URN
![[Pasted image 20230412103644.png|300]]

# 🐱Tomcat是干什么的？
#JavaServlet引擎
一个运行JAVA的网络服务器，底层时Socket的一个程序；也是JSP和Servlet的容器。
也是运行与JVM中的一个进程，被定义为中间件，即：Java项目和JVM之间的中间容器。
Tomcat可以让比人访问你写的页面程序。
![[Pasted image 20230412094007.png|500]]


# 😿Tomcat工作原理？

## Tomcat目录结构
![[Pasted image 20230412101504.png|400]]
conf文件夹：
- server.xml用于配置server相关信息，如tomcat启动的端口号，配置主机
- web.xml配置web应用，相当于web应用的一个站点
- tomcat-user.xml配置用户名密码和相关权限

webapps文件夹：放置我们的web应用程序
- 每个web站点下创建一个html文件作为入口页面
- 站点目录结构：
![[Pasted image 20230412102100.png|400]]
work文件夹：存放jsp被访问后生成对应的server文件和.class文件



## Tomcat体系结构

![[Pasted image 20230412102911.png|550]]
## Tomcat浏览器访问web资源流程
![[Pasted image 20230412103512.png|550]]

# 😼如何配置Tomcat？
1. 首先安装[[Java#安装以及配置|JDK]]。
2. 然后安装Tomcat：在Ubuntu环境下`sudo apt intall tomcat9`
3. 安装完成后`systemctl status tomcat.service`查看tomcat服务是否开启；然后在浏览器查看（确保8080端口不被占用）http://localhost:8080/；如果现实It works！说明tomcat与Java版本匹配可以正常运行；如果显示错误则要切换jdk版本。
> 如果端口被占用，可以配置tomcat目录下的conf/server.xml文件。修改Connector标签下的port属性。
cd


# 😽如何使用Tomcat部署项目？
1. 将Web项目转换成war包，可以用[[Maven]]、IDEA、Eclipse等工具来打包
2. 将war拷贝到tomact的webapps目录下，需要对war包重命名
3. 重启tomcat，便可通过localhost:8080来访问

在部署Web项目时需要注意以下几点：
1.  如果您修改了Web项目的代码，需要重新生成war包并替换Tomcat中的war包。
2.  在部署Web应用时，应确保Tomcat中的webapps目录中没有同名的web应用，否则部署可能失败。  
3.  如果您修改了Web应用的配置文件，如web.xml等，需要重新生成war包并重新部署。 
4.  在Tomcat的日志中查看相关错误提示，以便快速找到问题并解决。

## 配置虚拟目录
编辑tomcat目录下的conf/server.xml文件。修改Connector标签下的port属性。 
添加`<Context path="/web1" docBase="/home/piper/project/web1">`

## 关于Linux VS Code下使用Tomcat
下载完的tomcat一定要记得，将tomcat目录的拥有者改为用户而不是root，否则Community Server Connectors无法识别本地服务器

其次部署项目是部署的是target目录下的项目或这`.war`文件，而不是整个项目目录，负责会导致浏览器因找不到路径返回404。