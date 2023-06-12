
# 基本结构

![[Pasted image 20230506164802.png|600]]

![[Pasted image 20230506164833.png|600]]

![[Pasted image 20230506164933.png|600]]

前段基于vue；后端基于：java，Mybatis的交互模式
![[前后端交互图.png|500]]


## 前后端交互

整个前后端的交互周期基本，与HTTP/HTTPS连接和释放的声明周期相同。
![[Pasted image 20230419111410.png|550]]

![[Pasted image 20230419111838.png|550]]

### 建立连接阶段

前段：
- 组成socket发送HTTP CONNECT请求与服务器建立连接
后端：

### 服务阶段

前端：
- 将用户行为提供的参数封装进HTTP/HTTPS发送给服务器
后端：
- 接受到客户端发来的HTTP/HTTP请求并解析
- 根据解析出的请求选择相应的API提供服务
- API会调用服务器内部的其他不对外展示服务实现用户需求
- API在实行完成后会向用户反馈
前段：
- 显示响应页面

## 前端

[[前端指南]]

1. 前段负责展示页面，并定义用户行为，并且将用户行为提供的参数发送给服务器。
2. 在收到服务器响应后，更新用户界面。

前段的请求并不会直接交付给服务器，而是通过 #LD负载均衡器 计算出可以提供服务的服务器地址，然后进行转发。

### 前段功能与技术对偶

- 前端服务器[[Nginx]]
- [[HTML]]提供了一个展示的内容模板，并*显示数据*，静态网页一般用HTML即可；但如果要实现动态网页还需要 #asp ， #php ， #jsp ， #aspx 等技术的支持。
- [[JS]]用于*实现html中的按键功能*，并且可以通过**HTTP/HTTPS**向服务器端*发送请求*
- [[SpringBoot#JSON参数]]用于*表示JS中的对象*，一种轻量级的*数据交换格式*。
- [[XML]]用于实现*数据的传输*，并定义数据的格式
- [[CSS]]的功能则是*对html进行渲染*，包括字体，间距，颜色等

### 前段技术演进


## 后端

[[后端指南]]

后端的作用是响应用户界面
- 接受到客户端发来的http/https请求并解析
- 根据解析出的请求选择相应的API提供服务
- API会调用服务器内部的其他不对外展示服务实现用户需求
- API在实行完成后会向用户反馈
后端服务器，不同的请求配置相应API，API实现了用户请求的功能。
![[v2-e6f568f641bd3cbbc8e2596679261a09_720w.webp|700]]

### 后端功能与技术对偶

### Web服务器

服务器分为两种，一种是需要访问www的Internet服务器，另一种就是我们常用的Web应用服务器，本节着重介绍后者

Web服务器的功能，首先能够和客户端建立连接，因此需要一个*监听器*来监听*端口*；在监听器捕获请求后需要对HTTP请求进行解析，因此要需要一个*解析器*，一般解析GET和POST；在解析出应用请求后我们还要将解析出的参数传递给响应的API，这样的服务程序就被成为*容器*；在实行完程序后Web服务器还会向客户端给予反馈，如：html，css，js，rar，txt等。
- 实现主机为其他主机提供web服务需要软件的支持： #apache ， #ngix

### Servlet容器

Servlet 全称Server Applet即服务端小程序；与之相对Applet为客户端小程序。
在服务器上运行Servlet需要服务器支持编程语言的运行时环境。Servlet容器就是Servlet程序的运行时环境， #tomcat 不仅拥有基本的Web服务器的功能还集成了JSP。
![[Pasted image 20230307111633.jpg|300]]

### 后端架构
[[SpringBoot]]

# `ris:File`文件服务

## 文件上传

### 传至本地

![[Pasted image 20230428161220.png|600]]

前端：
- 表单项 type="file"
- 表单提交方式 post
- 表单entype属性 multipart/form-data
后端：
- MultipartFile接收文件
```java
@RestController

public class UploadController {

@PostMapping("/upload")

public Result upload(String name, Integer age,MultipartFile file) throws IllegalStateException, IOException{

log.info("upload file:{},{},{}",name, age, file);
String fileName = file.getOriginalFilename();
if(fileName==null)return Result.error("file name should not null");
//UUID 通用唯一识别码
String newFileName =UUID.randomUUID().toString()+fileName.substring(fileName.lastIndexOf("."));
log.info("new file name:{}",newFileName);
//转存文件
file.transferTo(new File("/home/piper/Upload/"+newFileName));
return Result.success();
}

}
```


### 传至云端——阿里云OSS

![[Pasted image 20230428161951.png|600]]

参考文档：[Java前言](https://help.aliyun.com/document_detail/32008.htm?spm=a2c4g.52834.0.0.3ee362a9UnJVWc#concept-32008-zh)
![[Pasted image 20230428162327.png|600]]




# 登陆校验

![[Pasted image 20230504164737.png|600]]

## `ris:Cellphone`会话技术
#会话技术 
会话：一次完整的通信过程，一次会话包括多次请求响应，直到一方断开连接会话结束

会话跟踪：目的是为了维护浏览器的状态，服务器需要识别多次请求是否来自统一浏览器，以便在一次会话的多次请求间共享数据。

### 会话跟踪
#会话技术/会话跟踪
#会话技术/Cookie #会话技术/Session #会话技术/JWT 

![[Pasted image 20230505084853.png|600]]

- 客户端会话跟踪——Cookie，即Cookie信息存储于客户端
用户登录后，服务器会生成Cookie并响应给客户端，客户端的每次请求对要携带Cookie，Cookie经过拦截校验便可继续会话
> 优点：HTTP协议支持技术
> 缺点：移动端APP无法使用Cookie；可被禁用；不支持跨域

- 服务端会话跟踪——Session，即Session信息存储于服务端
基于Cookie实现，该技术限定了Cookie的格式，服务器维护一个会话池，用户登陆时，服务器为客户端生成一个会话标识，并通过set-Cookie的方式告知客户端，之后客户端凭借此标识进行会话，服务器通过标识从会话池取出会话对象进行响应。
> 基于Cookie，存储于服务器，安全；不支持集群，因为集群中的各服务器维护的会话池各不相同

- **JWT令牌**，json web token
JWT前两部分为Base64编码，第三部分为数字签名

![[Pasted image 20230505093321.png|600]]

JWT令牌技术与Cookie类似，在登陆成功时服务器端产生JWT令牌，JWT令牌被存储在客户端，客户端会话期间都要携带令牌，但是该令牌即可放置于Cookie也可放置于请求体或属性中；经过拦截校验JWT的有效性，可继续会话。

![[Pasted image 20230505094301.png|600]]

![[Pasted image 20230505095038.png|600]]

> 支持PC和移动端；支持集群；减轻服务器存储压力；但要自己实现令牌

由此延伸出了一些问题：
- 统一拦截系统如何保证令牌、Cookie、Session的有效性？
- 如果黑客获得以上认证不就可以伪装成登陆的用户进行访问？
答：因为JWT第三部分，数字签名的存在，保障了JWT的安全性。
#### JWT关键代码
#会话技术/JWT 
```java
public class JwtUtils {

    private static String signKey = "itheima";
    private static Long expire = 43200000L;

    /**
     * 生成JWT令牌
     * @param claims JWT第二部分负载 payload 中存储的内容
     * @return
     */
    public static String generateJwt(Map<String, Object> claims){
        String jwt = Jwts.builder()
                .addClaims(claims)
                .signWith(SignatureAlgorithm.HS256, signKey)
                .setExpiration(new Date(System.currentTimeMillis() + expire))
                .compact();
        return jwt;
    }

    /**
     * 解析JWT令牌
     * @param jwt JWT令牌
     * @return JWT第二部分负载 payload 中存储的内容
     */
    public static Claims parseJWT(String jwt){
        Claims claims = Jwts.parser()
                .setSigningKey(signKey)
                .parseClaimsJws(jwt)
                .getBody();
        return claims;
    }
}

```

#### Session关键代码
#会话技术/Session 
```java
    @GetMapping("/s1")
    public Result session1(HttpSession session){
        log.info("HttpSession-s1: {}", session.hashCode());
        session.setAttribute("loginUser", "tom"); 
//往session中存储数据
        return Result.success();
    }

    @GetMapping("/s2")
    public Result session2(HttpServletRequest request){
//获取Session
        HttpSession session = request.getSession();
        log.info("HttpSession-s2: {}", session.hashCode());
        Object loginUser = session.getAttribute("loginUser"); //从session中获取数据
        log.info("loginUser: {}", loginUser);
        return Result.success(loginUser);
    }
```

## `ris:ShieldCross`拦截技术

![[Pasted image 20230505161438.png|600]]

### Filter

实现登陆校验，统一编码处理，敏感字符处理
入门：
1. 实现Filter接口
- 主要实现doFilter接口
- doFilter接口中要有chain.doFilter(request,response)放行操作
2. 在Filter添加@WebFilter(urlPatterns="/\*")注解
3. 在SpringBoot入口添加@ServletComponentScan注解

![[Pasted image 20230505151335.png|600]]

![[Pasted image 20230505151826.png|600]]

#### 关键代码
```java
public class MyFilter implements Filter{
    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)throws IOException, ServletException {
        HttpServletRequest req = (HttpServletRequest) request;
        HttpServletResponse resp = (HttpServletResponse) response;
		chain.doFilter(req,resp);
		return;
	}
} 

```

### Interceptor

![[Pasted image 20230505155805.png|600]]

入门：
1. 定义拦截器
![[Pasted image 20230505160016.png|600]]
2. 注册拦截器
![[Pasted image 20230505160120.png|600]]
拦截路径配置
![[Pasted image 20230505161119.png|600]]

#### 关键代码
```java

public class LoginCheckInterceptor implements HandlerInterceptor {
    @Override //目标资源方法运行前运行, 返回true: 放行, 放回false, 不放行
    public boolean preHandle(HttpServletRequest req, HttpServletResponse resp, Object handler) throws Exception {
        //1.获取请求url。
        String url = req.getRequestURL().toString();
        log.info("请求的url: {}",url);

        //2.判断请求url中是否包含login，如果包含，说明是登录操作，放行。
        if(url.contains("login")){
            log.info("登录操作, 放行...");
            return true;
        }
        return false;
    }

    @Override //目标资源方法运行后运行
    public void postHandle(HttpServletRequest request, HttpServletResponse response, Object handler, ModelAndView modelAndView) throws Exception {
        System.out.println("postHandle ...");
    }

    @Override //视图渲染完毕后运行, 最后运行
    public void afterCompletion(HttpServletRequest request, HttpServletResponse response, Object handler, Exception ex) throws Exception {
        System.out.println("afterCompletion...");
    }
}

```

### Filter VS Interceptor 

![[Pasted image 20230505161542.png|600]]


# 异常处理

定义全局异常处理器：
![[Pasted image 20230505162430.png|600]]

# 现代web技术
![[v2-89046ee2fadac4fd7eb54bcb9fa599fd_1440w.webp|300]]

## C/S架构
客户端/服务器
即用户需要下载客户端软件，才可以接受服务。
中间件的出现突破了原有C/S架构的诸多限制
中间件

### 技术栈

## B/S架构
浏览器/服务器
即用户登录网站，就可以接受服务。
![[v2-589bc3e9c5e00d84ab9086afec49545d_1440w.webp|300]]


### 技术栈

## 微服务架构
![[v2-a3c964f265535f48192a4ad0828fa7d6_1440w.webp|300]]

### 技术栈