
SpringBoot项目静态资源(html, js, css)：
- classpath:/static
- classpath:/public 
- classpaht:/resources

@SpringBootApplication 注解包含了@ComponentScan，可以自动扫描此包以及子包下的所有组件。


# `ris:RecordCircle`入门
---

1. 请求路径映射，设置Controller
```java
package com.itheima.controller;

@RestController
public class HelloController {
    @GetMapping("/hello")
	//接收请求
    public String hello() {
	//请求响应
        System.out.println("Hello world");
        return "Hello world";
    }
}

```

2. 设置启动类
```java
package com.itheima;

@SpringBootApplication
// @RestController
public class DemoApplication {
	public static void main(String[] args) {
		SpringApplication.run(DemoApplication.class, args);
	}

	// @GetMapping("/hello")
	// public String hello() {
	// System.out.println("Hello World");
	// return "Hello World";
	// }

}
```

> 一定要将Application启动类方的其他包的外侧，否则浏览器请求会有“This application has no explicit mapping for /error, so you are seeing this as a fallback.“报错。


# `ris:Server`请求响应的实现——Controller
---

#B/S架构 #MVC 
![[Pasted image 20230419095341.png|550]]

## 请求

![[Pasted image 20230423142111.png|400]]

### 简单参数
#HTTP 
参数名和形参变量名相同，定义形参即可接收参数
- @RestController
- @RequestMapping("/hello")
- @RequestParam(name="name")
```java
@RequestMapping("/simpleParam")
public String simpleParam(String name, Integer age) {
	System.out.println(name + ":" + age);
	return "OK";
}


@RequestMapping("/simpleParam")
public String simpleParam(@RequestParam(name = "name")String username, required = false)
//被@RequestParam注解的形参require默认为true
    String username, Integer age) {
    System.out.println(username + ":" + age);
    return "OK";
}
```

### 实体参数
#pojo #HTTP 

前端 GET：
url：`localhost:8080/complexPojo?name=Tom&age=10&address.province=beijing&address.city=beijing`

后端 接收响应：
```java
//package com.itheima.pojo.User;

public class User{
	private String name;
	private Integer aga;
	private Address address;
}

//package com.itheima.pojo.Address;

public class Address{
	private String province;
	private String city;
}

//package com.itheima.controller;
public String complexPojo(Usr user){
	System.out.println(user);
	return "OK";
}

```

### 数组集合参数
#HTTP 
前端 GET
url：`localhost:8080/hobby=java&hobby=game`

后端 接收响应：

- 使用数组接收：请求参数名和数组变量名相同，可直接用书组封装
```java
@RequestMapping("/arraryParam")
public String arrayParam(String[] hobby){
	System.out.println(Arrays.toString(hobby));
	return 'OK';
}
```
- 使用集合接收：请求参数名和集合变量名相同，通过@RequestParam绑定参数关系
```java
@RequestMapping("/listParam")
public String listParam(@RequestParam list<String> hobby){
	System.out.println(hobby);
	return 'OK';
}
```

### 日期参数
#HTTP 

前端 GET
url：`localhost:8080/updateTime=2022-12-12 10:05:45`

后端 接收响应：
将前端请求日期，封装给LocalDateTime
```java
@RequestMapping("/updateTime")
public String dateParam(@DateTimeFormat(pattern="yyyy-MM-dd HH:mm:ss")LocalDateTime updateTime){
	System.out.println(updateTime);
	return "OK";
}
```

### JSON参数
#HTTP #json 
前端 POST
```json
{
	"name":'Tom',
	"age":16,
	"address":{
		"province":"beijing",
		"city":"beijing"
	}
}
```
> 前端的json数据对应一个后端的Pojo对象，且**json键名要与pojo的属性名保持一致**

url：`localhost:8080/jsonParam`

后端 接收响应：
```java
@RequestMapping(value="/jsonParam",method=GET)
public String jsonParam(@RequestBody User user){
	System.out.println(user);
	return "OK";
}
```

### 路径参数
#HTTP 
前端请求
url：
`localhost:8080/path/1`
`localhost:8080/path/2`
`localhost:8080/path/3`

后端 接收响应： 
**路径名要与形参名保持一致**
```java
@RequestMapping("/path/{id}/{name}")
public String pathParam(@PathVariable Integer id,@PathVariable String name){
	System.out.println(id+":"+name);
	return "OK";
}
```

## 响应
#SpringBoot/注解 
@ResponseBody
- 可注解与Controller方法/类
- 将方法返回值直接响应；若返回类型为实体/集合，则会转为JSON格式响应
> @RestController = @Controller + @ResponseBody 

### 统一响应结果Result
该对象是为了统一规范后端不同接口的响应格式，从而使得前端不必专注于解析响应数据的格式；
从而降低系统的维护成本；
```java
//package com.itheima.pojo.Result;

public class Result{
//响应码
	private Integer code;
//提示信息
	private String msg;
//返回数据
	private Object data;
...
}

```


## 分层解耦MVC
---
#MVC #Spring/IoC #Spring/DI 

[[SpringFrameWork#IoC and DI]]

### 分层
#MVC 
[[SpringMVC]]
![[Pasted image 20230423153800.png|600]]


![[Pasted image 20230423162539.png|650]]

### 解耦
#Spring/IoC #Spring/DI 
[[OOP思想]]
通过容器实现存储并管理对象，从而实现层与层之间的解耦
1. 为Controller，Service，Dao类分别注解@Controller, @Service, @Reporsitory
2. Service类聚合Dao类；Contrroller类聚合Service类
![[Pasted image 20230423163526.png|600]]


# `ris:Pushpin2`配置文件——属性注入
---
#yml

配置优先级参考：[[SpringFrameWork#Spring配置]]
SpringBoot仅支持properties和yml这两种类型的配置文件。
![[Pasted image 20230504145509.png|600]]

yml语法：
![[Pasted image 20230504145725.png|200]]

将yml或properties中的属性注入到Bean对象：
![[Pasted image 20230504150052.png|600]]

![[Pasted image 20230504145352.png|600]]

# `ris:ArrowDropRight`SpringBoot原理
---
#面试高频 
## 起步依赖

`org.springframework.boot:spring-boot-starter-web`
该依赖包含了java-web项目的常用jar包。

## 自动配置

SpringBoot的自动配置即：当Spring容器启动后，一些配置类、Bean对象就会自动存入IOC容器，而无需手动声明。
![[Pasted image 20230506151228.png|600]]

![[Pasted image 20230508094722.png|600]]

### 第三方依赖引入
#面试高频 

1. @ComponentScan方案
@SpringBootApplication自动扫描项目路径下的Bean，而不会扫描第三方项目中的Bean。因此我我们可以通过@ComponentScan()来设置需要扫描项目路径
**缺点：**
- 包多时不宜管理；
- 仅需要包中的几个类，却需要大规模的扫描整个包，性能低
> 使用了@ComponentScan后会自动覆盖@SpringBootApplication的扫描路径，因此还需要手动导入当前项目路径。

![[Pasted image 20230506151603.png|600]]

2. @Import方案
Import导入的类会被Spring加载到IoC容器中

![[Pasted image 20230506152602.png|600]]

SpringBoot会根据@Conditional注解智能的注入Bean
![[Pasted image 20230506160217.png|600]]

3. **第三方提供的配置类注解@EnableXxxx**，**推荐！！！**


### 自动配置原理`==@SpringBootApplication`的实现


1. `@SpringBootApplication = @SpringBootConfiguration + @ComponentScan + @EnableAutoConfiguration`
2. `@SpringBootConfiguration = @Configuration`
3. `@EnableAutoConfiguration include @Import`,`@import`加载MATE-INF/spring.factories和MATE-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports。


- @SpringBootApplication，SpringBoot启动会自动加载MATE-INF/spring.factories和MATE-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports。
- MATE-INF/spring.factories：类的全类名，*2.7.x之前版本的配置文件*，*spring3.0.0以上版本则彻底移除了该文件*
- MATE-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports：自动配置类的全类名（这些类都带有AutoConfiguration后缀），*2.7.x版本之后的配置文件*

#### AutoConfiguration类实现
由@AutoConfiguration注解标识，而@AutoConfiguration由@Configuration实现；
**被@AutoConfiguration标识的XxxAutoConfiguration类主要作用是在内部声明Bean对象，其中Bean对象都被@Bean，和@ConditionalOnMissingBean标识**
- @Bean：被该注解标识的类，可被SpringFrameWork识别为Bean对象
- @ConditionalOnMisssingBean：该注解为@Conditional的子注解，功能是当Bean缺失时，产生该Bean。

#### 条件装配Bean——@ConditionalXxx

![[Pasted image 20230508093640.png|600]]


## 自定义starter
---
starter就是一个Bean集合，该Bean集合集成到SpringBoot，在启动时自动交由IOC容器托管。
![[Pasted image 20230508095045.png|600]]
步骤
1. 创建空SpringBoot项目，Xxxx-xxx-xxx-starter，只留pom即可
2. 创建空SpringBoot项目，Xxxx-xxx-xxx-autoconfigure，保留pom，需要启动类
3. 编写工具类XxxxUtils，编写工具类的自动配置类XxxxUtilsAutoConfiguration
> 工具类不需要@Component声明，在自动配置类中统一编写工具对象的实例化，并在生成方法上添加@Bean注解；实例化用的配置参数通过形参传递

```java
@Configuration

@EnableConfigurationProperties(AliOSSProperties.class)

public class AliOSSAutoConfiguration {

@Bean

public AliOSSUtils aliOSSUtils(AliOSSProperties aliOSSProperties){

AliOSSUtils aliOSSUtils = new AliOSSUtils();

aliOSSUtils.setAliOSSProperties(aliOSSProperties);

return aliOSSUtils;

}

}
```

4. 在MATE-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports配置工具类全类名
5. 在Xxx-xxx-xxx-starter的pom配置自动配置的坐标
6. `mvn install` starter项目，成功后该项目坐标可用

![[Pasted image 20230508095349.png|600]]
实践
![[Pasted image 20230506163131.png|600]]



