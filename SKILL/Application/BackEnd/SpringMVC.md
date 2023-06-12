# `ris:CustomerService2`SpringMVC
#MVC
使用DispatcherServlet作为前端控制器，内部提供处理器映射器、处理器适配器、视图解析器等组件，简化JavaBean封装、Json转化、文件上传；

![[Pasted image 20230412153224.png|500]]
快速入门：
1. 导入spring-mvc坐标，要将该项目设置为`<packaging>war</packaging>`。
2. 配置前端控制器DispatcherServlet
```xml
<!--src/resources/spring-mvc.xml-->
...
<context:component-scan base-package="com.itheima.controller"/>
```

```xml
<!--src/webapp/WEB-INF/web.xml-->
<servlet>
<!--再次创建了一个servlet对象-->
	<servlet-name>DispatcherServlet</servlet-name>
	<servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
	<init-param>
<!--将本地bean配置导入Controller配置-->
		<param-name>contextConfigLocation</param-name>
		<param-value>classpath:spring-mvc.xml</param-value>
	</init-param>
<!--服务器启动时创建DispatcherServlet-->
	<load-on-startup>2</load-on-startup>
</servlet>
<servlet-mapping>
<!--再次创建了一个servlet-->
	<servlet-name>DispatcherServlet</servlet-name>
	<url></url>
</servlet-mapping>
<!--服务器开启加载容器-->
<load-on-startup>2</load-on-startup>
```

```java
packaging com.itheima.controller

@Controller
public class QuikStart{
	@RquestMapping("/show")//配置映射路径
	public void show(){
		System.out.println("show....");
	}
}
```
3. 编写Controller，配置映射路径，并交给SpringMVC容器管理


### 请求处理

### 相应处理

### 拦截器

[[Web应用结构#`ris:ShieldCross`拦截技术]]

### 全注解开发

### 组件工作原理

### 异常处理机制






# `ris:Plant` SSM
springMVC+Mybatis+SpringBoot
