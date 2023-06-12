[Spring API](https://docs.spring.io/spring-framework/docs/current/javadoc-api/)
[Spring中文文档](https://springdoc.cn/spring/index.html)




# `ris:Leaf`SpringFrame
---

![[Pasted image 20230316150143.png|500]]
需要的背景知识：[[设计模式]]、[[XML]]、[[Java]]、[[Maven]]

后端开发
![[Pasted image 20230418143831.png|550]]

![[Pasted image 20230418144007.png|550]]


## IoC and DI 
---
#Spring/IoC #Spring/DI #Spring/Bean #Spring/Bean/生命周期 #面试高频
右侧的一列矩形构成了Bean的生命周期。

![[Pasted image 20230330103416.png|600]]


## Spring配置

**Springp配置优先级：**
命令行参数>java系统属性>properties>yml>yaml




## Spring Bean
---
#Spring/Bean
[[XML]]

关于Bean的一些理解：

### 获取Bean对象
```java
public class SpringbootWebConfigApplication{
	@Autowired 
	private ApplicationContext applicationContext;
	@Test
	pubblic void testGetBean(){
		//get by name
		DeptController bean1 = (DeptController) applicationContext.getBean("deptController");
		//get by class
		DeptController bean2 = (DeptController) applicationContext.getBean(DeptController.class);
		//get by class and name
		DeptController bean3 = (DeptController) applicationContext.getBean("deptController",DeptController.class);

	}
}
```



### Bean实例化流程
#Spring/Bean #Spring/IoC 
1. Context初始化时，将xml中bean的信息封装进BeanDefinition对象中
2. 所有的BeanDefinition对象会通过bean的id映射到beanDefinitionMap的Map< String,BeanDefinition>集合中区
3. ApplicationContext通过遍历beanDefinitionMap，使用[[Java#Reflection]]机制创建Bean实例对象，并将创建的Bean对象存储在singletoObjects的Map< String,Object>集合中
![[Pasted image 20230328112952.png|600]]
4. 当调用getBean方法时会通过Bean id获取单例池中的Bean对象。
![[Pasted image 20230328113949.png|500]]

#### BeanFactory & ApplicationContext
BeanFactory方法实例化bean
```java
public static void main(String[] args){
	DefaultListBeanFactory bf = new DefaultListBeanFactory();
	XmlBeanDefinitionReader rder = new XmlBeanDefinitionReader(bf);
	rd.loadBeanDefinitions("bean.xml");
	UserService userService = (UserService) bf.getBean("userService")
}
```
```xml
<bean id="userService" class="com.heima.service.UserServiceImpl">
</bean>
```
ApplicationContext方法实例化bean
```java
public static void main(String[] args){
	ApplicationContext applicationContext=new ClassPathXmlApplication("bean.xml");
	UserService userService = (UserService) applicationContext.getBean("userService");
}
```
三种不同的ApplicationContext

| Class                              | 功能                               |
| ---------------------------------- | ---------------------------------- |
| ClassPathXmlApplicationContext     | 加载类路径下的xml                  |
| FileSystemXmlApplicationContext    | 加载磁盘下的xml                    |
| AnnotationConfigApplicationContext | 加载注解配置类的ApplicationContext |

总结：ApplicaitonContext不仅包含了BeanFactory同时还具有国际化等其他功能，但是对于BeanFactory来说默认lazy-init，即：等到getBean使才实例化Bean对象；而ApplicationContext则是在创建时就已经将Bean中的内容完成实例化，但是我们可以通过在bean标签设置lazy-init属性使得ApplicationContext支持懒加载。


#### Bean实例化
#Spring/Bean #Spring/DI #Spring/IoC 

1. 含参/无参构造法
```xml
<bean id="userService" class="com.heima.UserServiceImpl">
	<property name="userDao" ref="userDao"/>
	<constructor-arg name="age" value="18"/>
</bean>
<bean id="userDao" class="com.heima.UserDaoImpl"></bean>
```
2. 静态工厂构造法
```java
public static UserDao userDao(){
//一些业务逻辑操作
	return new UserDaoImpl();}
```
```xml
<bean id="userDao" class="com.heima.UserDaoImpl" factory-method="userDao">
</bean>
```
3. 实例工厂构造法
java部分同上，只是不再需要static进行修饰
```xml
<bean id="myBeanFactory" class="com.heima.MyBeanFactory">
</bean>
<bean id="userDao" factory-bean="myBeanFactory" factory-method="userDao">
</bean>
```
4. 标准BeanFactory实例化方法
需要重写getObject和getObjectType方法
```java
public class MyBeanFactory implements FactoryBean<UserDao>{
	@Override
	pulbic UserDao getObject() throw Exception{
		return new UserDaoImpl();
	}
	@Override
	public Class<?> getObjectType(){
		return UserDao.class;
	}
}
```

---
#### Bean创建后的初始化
#Spring/Bean/初始化

1. xml配置式初始化
> 在实现中编写初始化函数，然后在xml的bean标签下配置init-method为相应函数名；对于销毁同理。
2. InitializingBean式初始化(*该方式在于配置init-method方式*)
```java
public class UserDaoImpl implements UserDao,InitializingBean{
	public void afterPropertiesSet() throw Exception{
		System.out.println("InitializingBean...");
	}
}
```

#### Bean依赖注入
#Spring/DI #Spring/Bean/实例化 

![[Pasted image 20230327113729.png|500]]

| Bean注入方式         | 配置方式                                                                       |
| -------------------- | ------------------------------------------------------------------------------ |
| 通过set方法注入      | `<property name="userDao" ref="userDao"/>` `<property name="age" value="18"/>` |
| 通过构造Bean方法注入 | `<constructor-arg name="name" ref="userDao"/>` `constructor-arg name="name" value="hao"/>`                                                                               |
集合类型注入：
list:
```xml
<bean id="userDao" class="com.heima.UserServiceImpl">
	<property name="userList">
		<list>
			<value>aaa</value>
			<value>bbb</value>
		</list>
	</property>
</bean>
```
```xml
<bean id="userDao" class="com.heima.UserServiceImpl">
	<property name="userList">
		<list>
			<ref bean="userDao1"></ref>
			<ref bean="userDao2"></ref>
		</list>
	</property>
</bean>
<bean id="userDao1" class="com.heima.UserDaoImpl"/>
<bean id="userDao2" class="com.heima.UserDaoImpl"/>
```
map:
```xml
<bean id="userDao" class="com.heima.UserServiceImpl">
	<property name="userList">
		<map>
			<entry key="d1" value-ref="userDao1"></entry>
			<entry key="d2" value-ref="userDao2"></entry>
		</map>
	</property>
</bean>
<bean id="userDao1" class="com.heima.UserDaoImpl"/>
<bean id="userDao2" class="com.heima.UserDaoImpl"/>
```

#### 非自定义Bean的实例化
关键问题：
- 被配置的Bean实例化方式是什么？是否有参？是否需要工厂？
- 被配置的Bean是否需要注入属性？
具体步骤可以参考[[SpringFrameWork#Bean实例化]]和[[SpringFrameWork#Bean依赖注入]]

---
### Bean的XML配置文件
- xmlns引入命名空间:xmlns与xsi:schemaLocation成对出现
- Bean配置
![[Pasted image 20230327141208.png|500]]
这里需要注意scope，当scope为singleton时创建的Bean为单例，实例化后会放在单例池中，每次使用都会访问单例池中的Bean对象，而是新建Bean对象。
而如果scope为prototype则每次实例化一个Bean对象都要新建。

- Beans配置
```xml
<!--该bean从属于dev环境-->
<beans profile="dev"></beans>
```

使用配置环境的方法
1. 命令行：`-Dspring.profiles.active=test`
2. 代码：`System.setProperty("spring.profiles.active","dev");`

- import导入外部配置（外部Bean）
`<import resource="classpath:otherApplicationContext.xml"/>`

Bean作用域
![[Pasted image 20230506144709.png|600]]


## Spring Bean后处理器——控制Bean的注册
允许我们介入Bean实例化过程中，以达到动态注册BeanDefinition和动态修改BeanDefinition，以及动态修改Bean的作用。
Bean实例化流程参考[[SpringFrameWork#Bean实例化流程]]

### BeanFactoryPostProcessor
#Spring/Bean/注册 
![[Pasted image 20230329115429.png|600]]
Bean工厂后处理器，在BeanDefinitionMap填充完毕，Bean实例化之前执行；
BeanFactoryPostProcessor接口的定义：
```java
public interface BeanFactoryPostProcessor{
	void postProcessBeanFactory(ConfigurableListableBeanFactory var1) throws BeansException;
}
```
实现了该接口的类只要交由Context管理，Spring就会回调该接口的方法，对BeanDefinition进行注册和修改。

---
#### BeanDefinition修改
**Bean从xml抽象到程序中的对象为BeanDefinition，每个bean都对应一个。**
1. 实现接口
```java
package com.heima.processor.MyBeanFactoryPostProcessor
public class MyBeanFactoryPostProcessor implements BeanFactoryPostProcessor{
	@Override
	public void postProcessBeanFactory(ConfigurableListableBeanFactory beanFactory) throws BeansException{
		System.out.println("post...");
		//修改BeanDefinition,使得创建userDao时，创建UserService
		BeanDefinition bd=beanFactory.getBeanDefinition("userDao");
		bd.setBeanClassName("com.heima.service.UserServiceImpl");
	}
}
```
2. 将实现的接口交由Spring容器托管
```xml
<bean class="com.heima.processor.MyBeanFactoryPostProcessor"/>
```

---
#### BeanDefinition动态注册
已知条件：UserDao接口以及接口实现UserDaoImpl在com.heima.dao目录下，但是没有在xml中配置
1. BeanFactoryPostProcessor接口实现注册
```java
package com.heima.processor.MyBeanFactoryPostProcessor
public class MyBeanFactoryPostProcessor implements BeanFactoryPostProcessor{
	@Override
	public void postProcessBeanFactory(ConfigurableListableBeanFactory beanFactory) throws BeansException{
		//注册BeanDefinition
		BeanDefinition bd= new RootBeanDefinition();
		bd.setBeanClassName("com.heima.dao.UserServiceImpl");
//由于ConfigurableListableBeanFactory没有registerBeanDefinition方法，所以要强制转换成其子类DefaultListableBeanFactory
		DefaultListableBeanFactory dfBeanFactory=beanFactory;
		dfBeanFactory.registerBeanDefinition("userDao",bd);
	}
}
```
2. 专用BeanDefinition注册子接口BeanDefinitionRegistryPostProcessor
```java
public class MyBeanFactoryPostProcessor implements BeanDefinitionRegistryPostProcessor{
	@Override
	public void postProcessBeanFactory(ConfigurableListableBeanFactory factory) throws BeansException{}
	@Override
	public void postProcessBeanDefinitionRegistry(BeanDefinitionRegistry registry) throws BeansException{
		BeanDefinition bd=new RootBeanDefinition();
		bd.setBeanClassName("com.heima.UserDaoImpl");
		registry.registerBeanDefinition("userDao",bd);
	}
}
```

最后，交由容器托管：
```xml
<bean class="com.heima.processor.MyBeanFactoryPostProcessor ">
</bean>
```
- BeanDefinitionRegistryPostProcessor对象在注册Bean时，先使用postProcessBeanDefinitionRegistry方法。
- 然后使用postProcessBeanFactory方法。


---
### BeanPostProcessor
#Spring/Bean/注册  
Bean后处理器，在**Bean实例化之后，添加到singletonObjects 之前执行**；期间会经历Bean初始化的过程。 
![[Pasted image 20230329150859.png|600]]
接口定义：
```java
public interface BeanPostProcessor {
	@Nullable
	default Object postProcessBeforeInitialization(Object bean, String beanName) throws {
		return bean;
	}
	@Nullable 
	default Object postProcessAfterInitialization(Object bean, String BeanName) throws {
		return bean;
	}
}
```
1. 接口自定义实现：
```java
package com.heima.processor
public class MyBeanPostProcessor implements BeanDefinitionRegistryPostProcessor{ 
	@Override 
	public Object postProcessBeforeInitialization(Object bean, String beanName) throws {
		return bean;
	}
	@Override  
	public Object postProcessAfterInitialization(Object bean, String BeanName) throws {
		return bean;
	}
}
```
2. 交由spring容器托管
```xml
<bean cllass="com.heima.processor.MyBeanPostProcessor"/>
```
执行顺序：
构造函数-->postProcessBeforeInitialization 
-->afterPropertiesSet --> init-method -->postProcessAfterInitialization 

---
## Spring Bean生命周期
#Spring/Bean/生命周期 
从Bean通过反射创建出对象之后，到Bean成为一个完整对象（所谓完整对象就是DI之后的对象）被存储到单例池的过程，称为SpringBean生命周期。

### Bean实例化阶段
Spring框架取出BeanDefinition的信息进行判断：
- 判断bean是否为singleton；
- 判断是否要延迟加载；
- 判断是不是FactoryBean；
最终将一个普通的singleton Bean通过反射进行实例化
**这一阶段主要体现在对xml的bean进行配置**

### Bean初始化阶段 
实例化阶段后的Bean因为没有**注入属性**还只是一个半成品，因此还需要对Bean执行一些操作：
- Bean属性注入
- Aware接口方法 ^72f13f
- [[SpringFrameWork#BeanFactoryPostProcessor]] 方法
- [[SpringFrameWork#BeanPostProcessor]]方法
- InitializingBean 初始化方法
- init-method 自定义初始化方法
- BeanPostProcessor 的after方法调用
**该阶段时Spring最具有技术含量和复杂度的阶段，AOP增强还有Spring注解，Bean的循环引用等问题都在这个阶段体现。**

---
#### Bean属性注入 
#Spring/Bean/循环依赖 #Spring/DI 
- 普通属性注入，直接通过set方法的反射进行设置
- 单项对象依赖注入，从容器中getBean获取依赖对象，通过set方法注入；如果容器中没有依赖对象，则先创建被依赖的对象Bean实例后，再进行注入。
- 双向对象循环依赖注入，这里Spring为方式出现死循环，设置了一个**三级缓存**
```java
public class DefaultSingletonBeanRegistry ... {
//最终单例池，存储完整的Bean——一级缓存
	Map<String , Object > singletonObjects = new ConcurrentHashMap(256);
//早期单例池，存储半成品Bean，且当前对象已被其他对象引用——二级缓存
	Map<String , Object > earlySingletonObjects =new ConcurrentHashMap(16);
//单例bean工厂池，缓存为引用的半成品Bean，使用时通过工厂创建Bean——三级缓存
	Map<String , ObjectFactory<?>> singletonFactories = new HashMap(16);
}
```
[[三级缓存源码剖析流程.pdf]]

#### Aware接口方法 
Aware接口方法 为我们提供了一种修改底层Bean的方法，即自定义底层Bean的方法。

| Aware接口               | 回调方法                                                    | 作用                                  |
| ----------------------- | ----------------------------------------------------------- | ------------------------------------- |
| ServletContextAware     | setServletContext(ServletContext context)                   | 注入ServletContext对象，web环境下生效 |
| BeanFactoryAware        | setBeanFactory(BeanFactory factory)                         | 注入BeanFactory对象                   |
| BeanNameAware           | setBeanName(String beanName)                                | 注入当前Bean容器中的beanName          |
| ApplicationContextAware | setAppicationContext(ApplicationContext applicationContext) | 注入applicationcontext对象            | 

用法：
1. 自定义的Bean对象implements Aware接口 
2. 重写接口的setter
3. 将Bean对象交由xml托管

### Bean完成阶段
初始化阶段后，bean已经“完整”，将完整的Bean存储到singletonObjects中去，就完成了Bean的生命周期。

---
## 基于注解的Sping应用
与xml配置方式一样，可以实现依赖注入，但是更加方便快捷；
用注解替代xml中的标签

### 自定义Bean标签注解
#Spring/Bean/注解 #Spring/Bean 
[[SpringFrameWork#Bean的XML配置文件]]
一些注解皆注于Bean类

| xml标签                     | 注解                           | 功能                                         |
| --------------------------- | ------------------------------ | -------------------------------------------- |
| `<bean id=""/>`             | @Component("bean_id")          | 注解于类，制定扫描范围内被spring加载并实例化 |
| `<bean scope=""/>`          | @Scope("singleton或prototype") | 注解于类，设定Bean的作用域                   |
| `<bean lazy-init=""/>`      | @Lazy("true或false")           | 注解于类，Bean延迟到使用getBean时加载        | 
| `<bean init-method =""/>`   | @PostConstruct                 | 注解于初始化方法之上，Bean实例化后使用的方法 |
| `<bean destroy-method=""/>` | @PreDestory("method_name")     | 注解于销毁方法之上，Bean销毁前调用的方法     |

#### 注解使用

##### @Component 及其衍生注解
由于JavaEE分层开发，所以对@Component进行了不同层次的语义化注解。
1. 在Bean类上打上注解 
```java
@Component("userDao")
public class UserDaoImpl implements UserDao{
}
```
2. 在xml配置文件，添加`<context:component-scan base-package="com.itheima"/>`标签

**JavaEE层次开发专用注解：**

| @Component 衍生注解 | 注解位置       |
| ------------------- | -------------- |
| @Repository         | Dao层次类      |
| @Service            | Service 层次类 |
| @Controller         | Web层次类      |
##### @Configuration 配置类注解
[[SpringFrameWork#Bean配置类的注解开发]]

##### @Primary 提高Bean优先级
注解于类
##### @Profile("env_name") 标注当前产生Bean在哪个环境下被激活
注解于类或者方法；激活环境的方法见：[[SpringFrameWork#Bean的XML配置文件]]


---
#### Bean依赖注入注解
#Spring/Bean/注解 #Spring/DI 
#面试高频 

| 对应标签                       | 注解                        | 功能                                                                                      |
| ------------------------------ | --------------------------- | ----------------------------------------------------------------------------------------- |
| `<property name="" value=""/>` | @Value("value")             | 注解于字段或方法，注入普通数据                                                            |
| `<property name="" ref=""/>`   | @Autowired                  | 注解于字段或方法，根据类型从容器中注入引用数据;如果同一类型Bean有多个，则尝试通过名字进行二次匹配 |
| `<property name="" ref=""/>`   | @Qualifier                  | 注解于字段或方法，结合@Autowired，根据名称匹配容器中的bean进行注入；即直接通过名字进行匹配                    |
| `<property name="" ref=""/>`   | @Resource(name="bean_name") | 注解于字段或方法，根据类型或名称进行注入;不加名称时根据类型注入，加名称时根据名字注入     | 
关于@Autowire注解的一个使用技巧
```java
//根据函数参数类型，引用容器中的Bean
@Autowired 
public void method1(UserDao userDao){}

//将容器中所有UserDao类型的Bean，加载到userDaoList中
@Autowired 
public void method2(List<UserDao> userDaoList){}
```
> 面试：@Autowired 与@Resource的区别
> 1. @Autowired 来自spring框架，@Resource由jdk提供
> 2. @Autowired 默认按类型注入；@Resource默认按名注入

---
### 非自定义Bean注解开发
非自定义Bean不能像自定义Bean一样使用@Component进行管理，非自定义Bean需要通过工厂方式进行实例化，使用@Bean标注，属性为bean_name
```java
@Bean("dataSource")
public DataSource dataSource(){
	 ...
	return dataSource;
}
```
Note: 被标注为@Bean的方法所在的类也必须交由Spring管理(即：必须被@Component标注)

#### 非自定义Bean属性注入
```java
@Bean("dataSource")
public DataSource dataSource(@Value("${jdbc.driver}") String driverClassName,
							@Autowired UserDao userDao,
							@Qualifier("userDao2") UserDao userDao2){
	 ...
	return dataSource;
}
```

---
 ### Bean配置类的注解开发
#Spring/Bean/注解  
Bean配置类的注解开发，目的是用配置类替代xml配置文件。 
```java
package com.itheima.config;

//当前类是一个配置类（用于替代xml）
@Configuration

//用于扫描Bean，等价于<context:component-scan base-package="com.itheima"/>
@ComponentScan(["com.itmeima"])

//用于加载属性配置资源，等价于<context:property-placeholder location="classpath:jdbc.properties"/>
@PropertySource(["classpath:jdbc.properties"])

//加载其他配置类，等价于<import resource=""/>
@Import(OtherBean.class)
public class SpringConfig{
}
```

```java
package com.itheima.test;

public class Test{
	//xml方式的Spring容器
	//ClassPathXmlApplicationContext appContext=new ClassPathXmlApplicationContext("applicationContext.xml");
	 //注解方式的Spring容器
	  ApplicationContext appContext = new AnnotationConfigApplicationContext(SpringConfig.class);
}
```

### Bean注解原理
#Spring/Bean/注解 
![[Pasted image 20230404154854.png|500]]

---
## AOP
#AOP
**概念：** AOP是横向对不同事物的抽象，属性与属性、方法与方法、对象与对象都可组成一个切面；假设左边的对象需要植入右边对象的方法，那么右边的对象叫做增强对象，植入的方法叫做增强方法；被植入的方法叫做主方法。
![[Pasted image 20230406143329.png|500]]

| 概念     | 单词      | 解释                               |
| -------- | --------- | ---------------------------------- |
| 目标对象 | Target    | 被增强的方法所在对象               |
| 代理对象 | Proxy     | 对目标增强后，客户端实际调用的对象 |
| 连接点   | Joinpoint | 目标对象可被增强的方法             |
| 切入点   | Pointcut  | 目标对象实际被增强的方法           |
| 增强     | Advice    | 增强部分的代码逻辑                 |
| 切面     | Aspect    | 增强和切入点的组合                 |
| 织入     | Weaving   | 将增强和切入点组合的动态过程       |
![[Pasted image 20230410155852.png|550]]


**实现方案：** 使用动态代理技术，runtime时对目标对象方法进行增强，参考：[[设计模式#Proxy]],[[SpringFrameWork#^72f13f|aware]]。
```java
@Override 
public Object postProcessAfterInitialization，ApplicationContextAware(Object bean, String beanName)throws BeansException {
	if(bean.getClass().getPackage().getName().equals("com.itheima.service.impl")){
		//生成Poxy
		Object beanProxy = Proxy.newPorxyInstance(
			baen.getClass().getClassLoader(),
			bean.getClass().getInterfaces(),
			new InvocationHandler(){
				(Object proxy, Method method,Object[] args)->{
					//执行增强对象的方法
					MyAdvice myAdvice = applicationContext.getBean(MyAdvice.class);
					myAdvice.beforeAdvice();
					//执行目标对象方法
					Object result = method.invoke(bean,args);
					//执行增强对象的方法 
					myAdvice.afterAdvice();
					return result;
				}
			}
		);
		return beanProxy;
	}
	return bean;
}
@Override 
public void setAppicationContext(ApplicationContext applicationContext)throws BeansException {
	this.applicationContext=applicationContext ;
}

```

---
### 基于xml配置AOP
#AOP 
- 切点表达式的配置：通过配置的方式指定哪些包的哪些类的哪些方法需要被增强；
- 配置Weaving：配置目标方法被哪些增强方法增强，以及增强时机；

**步骤**
Aspect式：
1. 导入AOP坐标；
```xml
<!--pom.xml-->
<dependency>
	<groupId>org.aspectj</groupId>
	<artifactId>aspectjweaver</artifactId>
</dependency>
```
2. 准备目标类、增强类、并配置给Spring管理；
- 要配置xml的命名空间
3. 配置切点表达式：对指定的方法进行增强
4. 配置Weaving：指定切点与哪些增强方法结合
```xml
<aop:config>
	<!--配置切点-->
	<aop:pointcut id="myPointcut" expression="execution(void com.itheima.service.impl.UserServiceImpl.show())"/>
	<!--配置增强aspect式-->
	<aop:aspect ref="MyAdvice">
		<!--配置Weaving-->
		<aop:before method="beforeAdvice" pointcut-ref="myPointcut"/>
		<aop:before method="beforeAdvice" pointcut="execution(void com.itheima.service.impl.UserService.show())"/>
	</aop:aspect>
</aop:config>
```

Advisor式
```java
public class MyAdvice implements MethodBeforeAdvice, AfterReturningAdvice{
	@Override 
	public void before(Method method,Object[] objects, Object o)throws Throwable {
		System.out.println("before advice");
	}
	@Override 
	public void afterReturning(Object o,Method method,Object[] objects,Object obj){
		System.out.println("after advice");}
}
```

```xml
<aop:config>
	<!--配置切点-->
	<aop:pointcut id="myPointcut" expression="execution(void com.itheima.service.impl.UserServiceImpl.show())"/>
	<aop:advisor advice-ref="myAdvice" pointcut-ref="myPointcut"/>
</aop:config>
```

#### 切点表达式表示
`execution([访问修饰符]返回类型 包名.类名.方法名(参数))`
- 某一级包名、类名、方法名可以用\*表示任意
- `..`用于表示该包及其子包
- 参数列表可以用`..`表示任意参数：一般用于重载的方法


#### Advice类型

| Advice名称 | 配置方式                | 执行时机                         |
| ---------- | ----------------------- | -------------------------------- |
| 前置Advice | `<aop:before>`          | 目标方法执行前                   |
| 后置Advice | `<aop:after-returning>` | 目标方法执行后，异常时不执行     |
| 环绕Advice | `<aop:around>`          | 目标方法执行前后执行，异常不执行 |
| 异常Advice | `<aop:after-throwing thowing="">`  | 目标方法抛出异常执行             |
| 最终Advice | `<aop:after>`           | 不管是否异常，都会执行           | 
#### Joinpoint 传参

获取连接点的参数
![[Pasted image 20230506100622.png|600]]

| 参数类型            | 作用                                                                 |
| ------------------- | -------------------------------------------------------------------- |
| JoinPoint           | 连接点对象，任何通知都可用，可以获得当前目标对象，目标方法参数等信息 |
| ProceedingJoinPoint | JoinPoint子类，在环绕Advice中执行proceed()，进而执行目标方法         |
| Throwable           | 异常对象，使用在异常Advice中，需在配置文件指出异常对象名             | 
`JoinPoint.getTarget()`获取目标对象



---
### 基于注解配置AOP

#### 基本使用
0. 在配置文件添加`<aop:aspectj-autoproxy/>`，开启AOP自动代理，使得Spring可以解析AOP注解
1. 为Advice类，添加`@Component`、`@Aspect`、`@Order`(用于注解增强器的顺序)
2. 为增强方法加注解 

`@Before("execution(* com.itheima.impl.*.*(..))")`、

`@AfterReturning("execution(* com.itheima.impl.*.*(..))")`、

`@AfterThrowing(pointcut="execution(* com.itheima.impl.*.*(..))",throwing="e")`、

`@After("execution(* com.itheima.impl.*.*(..))")`、

`@Around("execution(* com.itheima.impl.*.*(..))")`

#### 切点表达式抽取

- execution匹配
- @annotation匹配

![[Pasted image 20230506095048.png|600]]

由于注解中的增强方法注解需要写死切点表达式，这会让维护变得困难，所以我们希望有一个统一的对象来配置切点表达式
```java
package com.itheima.MyAdvice

@PointCut("execution(* com.itheima.service.impl.*.*(..))")//统一配置切点位置,public其他Advice类也可使用，private仅限当前类使用
public void show();

@Around("MyAdvice.show()")//切点位置定义在MyAdvice.show注解
public Object around(ProceedingJoinPoint proceedingJoinPoint){};
```

##### 基于自定义注解的切面表达式定位

自定义MyLog注解
```java
package com.itheima.annotation

@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
public @interface MyLog{
}
```

注解匹配切入点
```java
package com.itheima.aop

public class MyAdvice{
	@PointCut("@annotation(com.itheima.annotation.MyLog)")
	public void show(){};
}
```

为特定类的方法添加注解
```java
package com.itheima.service.impl

public class DeptServiceImpl implements DeptService{
	@MyLog
	@Override 
	public void delete(Integer id){};
}
```


#### 全注解开发核心配置类
```java
package com.itheima.config;

@Configuration 
@ComponentScan("com.itheima")
//<context:component-scan base-packge="com.itheima"/>
@EnableAspectJAutoProxy
//<aop:aspectj-autoproxy/>
public class Config{

}
```

配置详解

#### Advice类执行顺序

默认情况下与类名的字母排序有关
但可以通过@Order(number)注解来自定义Advice的执行顺序


## 事务控制

事务：就是一个需要保证一致性和原子性的持久化操作。
![[Pasted image 20230411164843.png|550]]

![[Pasted image 20230505163723.png|600]]


事务回滚：
![[Pasted image 20230505164753.png|600]]

#### 编程式事务控制
通过代码，对业务逻辑实现事务控制。与底层持久曾紧耦合，对于不同的持久层API有不同接口实现。
Spring事务控制接口：

| 事务控制类                 | 中文           | 作用                                                                                               |
| -------------------------- | -------------- | -------------------------------------------------------------------------------------------------- |
| PlatformTransactionManager | 平台事务管理器 | 一个接口标准，实现类就有事务提交、回滚、获取事务对象的功能，对不同持久层框架可能会有不同的实现方案 |
| TransactionDefinition      | 事务定义       | 封装事务的隔离级别，传播行为，过期时间等属性信息                                                   |
| TransactionStatus          | 事务状态       | 存储当前事务的状态信息，如事务是否提交、回滚、有回滚点等                                           | 

例子：搭建一个转账环境，dao层转入转出钱的方法；service转账业务的方法，内部调用dao层转入转出方法：
- 准备tb_account数据库表
- dao准备一个AccountMapper，包括incrMoney和decrMoney方法
- service层准备一个transferMoney方法，分别调用incrMoney和decrMoney方法
- 在applicationContext.xml文件中对Bean进行管理配置

```xml
<!--application.xml-->

Bean自动注入扫描
<context:component-scan base-packge="com.itheima"/>

数据库配置文件定位
<context:property-placeholder location="classpath:jdbc.properties"/>

数据库连接配置
<bean id="dataSource" class="com.alibaba.druid.pool.DruidDataSource">
	<property name="driverClassName" value="${jdbc.driver}"/>
	<property name="url" value="${jdbc.url}"/>
	<property name="username" value="${jdbc.username}"/>
	<property name="password" value="${jdbc.password}"/>
</bean>
配置数据源
<bean class="org.mybatis.spring.SqlSessionFactoryBean">
	<property name="dataSource" ref="dataSource"/>
</bean>

MapperScannerConfigurer自动扫描
<bean class="org.mybatis.spring.mapper.MapperScannerConfigurer">
	<property name="basePackage" value="com.itheima.mapper"></property>
</bean>

配置transaction-manager事务平台管理器
<bean id="transcationManager" class="org.springframework.jdbc.datasource.DataSourceTransactionManager">
	<property id="dataSource" ref="dataSource"/>
</bean>

配置Spring提供的事务Advice(别忘导入tx命名空间！！！)
<tx:advice id="txAdvice" transaction-manager="transcationManager">
	<tx:attributes>
配置不同方法的事务属性 name：方法名；
isolation：隔离级别解决幻读，脏读等问题;
timeout: 超时时间；
propagation:事务的传播行为，解决事务嵌套问题
		<tx:method name="transferMoney" isolation="READ_COMMITED" propagation="REQUIRED" timeout="3" read-only="false"/>
		<tx:method name="*"/>
	</tx:attributes>
</tx:advice>

配置AOP事务增强
<aop:config>
	<aop:pointcut id="txPointcut" expression="excution(* com.itheima.service.impl.*.*(..))"/>
	<aop:advisor advice-ref="txAdvice" pointcut-ref="txPointcut"/>
</aop:config>
```

Mapper层
```java
package com.itheima.mapper;

public interface AccountMapper{ 

	@Update("update tb_account set money=money+#{money} where account_name=#{accountName}")
	public void incrMoney(@Param("accountName")String accountName,@Param("money")Integer money);

	@Update("update tb_account set money=money-#{money} where account_name=#{accountName}")
	public void decrMoney(@Param("accountName")String accountName,@Param("money")Integer money);
}
```

```xml
<!--AccountMapper.xml-->
<mapper namespace="com.itheima.mapper.AccountMapper">
	<!--<update id="incrMoney"></update>使用注解方式实现-->
	<update id="decrMoney"></update>
</mapper>
```

Service层——业务层
```java
package com.itheima.service;

public interface AccountService{
	void transferMoney(String outAccount, String inAccount, Integer money);
}
```

使用AOP的思想来实现事务控制
目标类：AccountServiceImpl，内部切点transferMoney()
增强类：Spring提供，只需配置即可
- 需要导入Spring事务控制坐标
- 配置目标类AccountServiceImpl
- 使用advisor标签配置切面
```java
package com.itheima.servcie.impl;

import com.itheima.service.AccountService;
@Service("accountService")
public class AccountServiceImpl implements AccountService{ 

	@Autowired 
	private AccountMapper accountMapper;
	@Override 
	public void transferMoney(String outAccount, String inAccount, Integer money){
//开启事务
		accountMapper.decrMoney(outAccount ,money );
//失败回滚
		accountMapper.incrMoney(inAccount ,money );
//提交事务
	}
}
```



#### 注解声名式事务控制

![[Pasted image 20230505164954.png|600]]

通过配置，对业务逻辑实现事务控制。与底层持久层解耦，对于不同的持久层API我们使用统一的配置文件进行配置。
```xml
<!--application.xml-->
开启spring事务控制自动代理
<tx:annotation-driven/>
```

```java
package com.itheima.servcie.impl;

import com.itheima.service.AccountService;
@Service("accountService")
@Transactional(isolation=Isolation.READ_COMMITED,propagation=Propagation.REQUIRED)
public class AccountServiceImpl implements AccountService{ 

	@Autowired 
	private AccountMapper accountMapper;
	@Override 
	//@Transactional(isolation=Isolation.READ_COMMITED,propagation=Propagation.REQUIRED)
	public void transferMoney(String outAccount, String inAccount, Integer money){
//开启事务
		accountMapper.decrMoney(outAccount ,money );
//失败回滚
		accountMapper.incrMoney(inAccount ,money );
//提交事务
	}
}
```

#### 全注解式事务控制
SpringConfig.class
```java
package com.itheima.config;

@Configuration 
@ComponentScan("com.itheima")
@PropertySource("classpath:jdbc.properties")
@MapperScan("com.itheima.mapper")
@EnableTransactionManager//扫描TransactionManager
//相当于<tx:annotation-driven/>
public class SpringConfig{
	@Bean
	//TransactionManager
	public DataSourceTransactionManager  dSTM(DataSource ds){...}
}
```



---
# `ris:Seedling` Spring整合第三方框架
#Spring/框架整合
基于xml配置的Spring整合第三方框架的方案：
1. 不需要自定义命名空间，不需要使用Spring配置文件配置第三方框架本身内容：[[MyBatis]]
2. 需要引入第三方框架命名空间，需要使用Spring配置文件配置第三方框架本身内容：[[Duboo]]

## 非自定义ns整合——以MyBatis为例
1. 导入MyBatis 坐标到pom.xml
```xml
<dependency>
	<groupId>org.mybatis</groupId>
	<artifactId>mybatis</artifactId>
	<version>3.5.12</version>
</dependency>
<!---将MyBatis整合到Spring所需要的依赖-->
<dependency>
	<groupId>org.mybatis</groupId>
	<artifactId>mybatis-spring</artifactId>
	<version>3.0.1</version>
</dependency>
```
2. 编写POJO持久层对象，如User.java:
```java
package com.heima.pojo;

public class User {
	private Integer id;
	private String username;
	private String password;

	public void setId(Integer id) {
		this.id = id;}

	public void setUsername(String username) {
		this.username = username;}

	public void setPassword(String password) {
		this.password = password;}

	public Integer getId() {
		return id;}

	public String getUsername() {
		return username;}

	public String getPassword() {
		return password;}

	@Override
	public String toString(){
		return "User{"+"id="+id+", username='"+username
		+ '\'' + ", password='" + password +'\''+"}";}
	}
```
3. 编写Mapper和Mapper.xml
```java
package com.heima.mapper;

import com.heima.pojo.User;
import java.util.List;

public interface UserMapper {
List<User> findAll();
}
```
头部可以参考：[Mybatis中文文档](https://mybatis.net.cn/) [[MyBatis]]
```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper
PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
"https://mybatis.org/dtd/mybatis-3-mapper.dtd">

<mapper namespace="com.heima.mapper.UserMapper">
	<select id="findAll" resultMap="userInfo">
		select * from tb_user
	</select>
<resultMap id="userInfo" type="com.heima.pojo.User">
	<id property="id" column="id"/>
	<result property="username" column="username"/>
	<result property="password" column="password"/>
	</resultMap>
</mapper>
```
3. 配置SqlSessionFactoryBean和MapperScannerConfigurer，这里需要一些[[JavaWeb]]的知识，测试代码：
```java
//非整合版本
public class MyBatisTest {

public static void main(String[] args) throws Exception {
	InputStream in = Resources.getResourceAsStream("mybatis-config.xml");
	SqlSessionFactoryBuilder builder = new SqlSessionFactoryBuilder();
	SqlSessionFactory sqlSessionFactory = builder.build(in);
	SqlSession sqlSession = sqlSessionFactory.openSession();
	UserMapper mapper = sqlSession.getMapper(UserMapper.class);
	List<User> all = mapper.findAll();
	for(User user:all)System.out.println(user);}
}
```
整合版本：
```xml
<!--Bean配置文件-->
<!--配置数据源信息-->
<bean id="dataSource" class="com.alibaba.druid.pool.DruidDataSource">
	<property name="driverClassName" value="com.mysql.jdbc.Driver"></property>
	<property name="url" value="jdbc:mysql://localhost:3306/mybatis"></property>
	<property name="username" value="root"></property>
	<property name="password" value="123"></property>
</bean>

<!--配置SqlSessionFactoryBean，作用将SqlSessionFactory存储到spring容器-->
<bean class="org.mybatis.spring.SqlSessionFactoryBean">
	<property name="dataSource" ref="dataSource"></property>
</bean>

<!--MapperScannerConfigurer,作用扫描指定的包，产生Mapper对象存储到Spring容器-->
<bean class="org.mybatis.spring.mapper.MapperScannerConfigurer">
	<property name="basePackage" value="com.itheima.mapper"></property>
</bean>

<bean id="userService" class="com.itheima.service.impl.UserServiceImpl">
	<property name="userMapper" ref="userMapper"></property>
</bean>
```

```java
public class ApplicationContextTest {
	public static void main(String[] args) throws Exception {
	ClassPathXmlApplicationContext applicationContext = new ClassPathXmlApplicationContext("applicationContext.xml");
	UserService userService=applicationContext.getBean(UserService.class);
	userService.show();
	}
}
```

使用`Alt+Shift+o`可自动导入依赖包。

### 原理剖析
整合包提供了一个SqlSessionFactoryBean和一个扫描Mapper的配置对象，SqlSessionFactoryBean一旦被实例化，就会开始扫描Mapper，并通过动态代理产生Mapper的实现类存储在Spring容器中
- SqlSessionFactoryBean：需要配置，用于提供SqlSessionFactory
- MapperScannerConfigurer：需要配置，用于扫描指定mapper注册BeanDefinition
- MapperFactoryBean：Mapper的FactoryBean，获取指定Mapper时调用getObject方法
- ClassPathMapperScanner：definition.setAutowireMode(2)修改了自动注入状态，所以MapperFactoryBean中的setSqlSessionFactory会自动注入。

---
## 自定义ns整合——以Context为例
一般情况下数据库的信息存在jdbc.properties文件中：
```jdbc.porperties
jdbc.driver=com.mysql.jdbc.Driver
jdbc.url=jdbc:mysql://localhost:3306/mybatis
jdbc.username=root
jdbc.password=123
```
然后，将jdbc.properties加载到xml配置文件中：
这里使用了xml表达式
```xml
<context:property-placeholder location="classpath:jdbc.properties"/>

<bean id="dataSource" class="com.alibaba.druid.pool.DruidDataSource">
    <property name="driverClassName" value="${jdbc.driver}"></property>
    <property name="url" value="${jdbc.url}"></property>
    <property name="username" value="${jdbc.username}"></property>
    <property name="password" value="${jdbc.password}"></property>
</bean>
```
源码同上一节整合版本

外部命名空间标签的执行流程：
1. 将自定义标签约束、物理约束文件和网络约束名称 以键值的形式存储到spring.schemas文件里，该文件存储与类加载路径的META-INF里，Spring会自动加载
2. 自定义ns 与 自定义ns处理器的映射关系，以键值的形式存储在spring.handlers的文件里，该文件存储在META-INF里，spring会自动加载
3. 准备好的NamespaceHandler，如果命名空间只有一个标签，则直接杂parse方法中进行解析，一般解析的结果是注册该标签对应的BeanDefinition。如果有多个标签，则在init方法中为每个标签都注册一个BeanDefinitionParser，在执行NamespaceHandler的parse方法时分流给不同的BeanDefinitionParser进行解析。

---
### 案例——框架集成开发
进行某一框架和Spring的集成开发，通过一个指示标签，向Spring容器自动注入一个BeanPostProcessor：
1. 确定ns名称、schema虚拟路径、标签名称；如以下xml配置文件，定义了haohao的ns，以及haohao命名空间下的annotation-driven的标签。
```xml
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:haohao="http://www.itheima.com/haohao"
       xsi:schemaLocation="
	   http://www.springframework.org/schema/beans 
	   http://www.springframework.org/schema/beans/spring-beans.xsd
	   http://www.itheima.com/haohao 
	   http://www.itheima.com/haohao/haohao-annotation.xsd">
	<haohao:annotation-driven/>
</beans>
```
2. 编写schema约束文件如：haohao-annotation.xsd
```xml
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema xmlns="http://www.itheima.com/haohao"
            xmlns:xsd="http://www.w3.org/2001/XMLSchema"
            targetNamespace="http://www.itheima.com/haohao">
<!--定义该ns下的标签-->
    <xsd:element name="annotation-driven"></xsd:element>
</xsd:schema>
```
3. 在类加载路径(resources目录)下创建META-INF目录，编写约束映射文件spring.schemas和处理器映射文件spring.handlers:
```xml
<!--spring.schemas-->
http\://www.itheima.com/haohao/haohao-annotation.xsd=com/itheima/haohao/config/haohao-annotation.xsd

```

```xml
<!--spring.handlers-->
http\://www.itheima.com/haohao=com.itheima.handlers.HaohaoNamespaceHandler
```

4. 编写ns处理器HaohaoNamespaceHandler，在init方法中注册HaohaoBeanDefinitionParser
```java
package com.itheima.handlers;
public class HaoHaoNamespaceHandler extends NamespaceHandlerSupport{
	@Override 
	public void init(){
		//初始化，在一个ns中为每个标签注册一个标签解析器
		this.registerBeanDefinitionParser("annotation-driven",new HaohaoBeanDefinitionParser);
	}
}
```
5. 编写标签解析器HaohaoBeanDefinitionParser，在parse方法中注册HaohaoBeanPostProcessor，实现HaohaoBeanDefinitionParser
```java
package com.itheima.parser;
public class HaohaoBeanDefinitionParser implements BeanDefinitionParser{
	@Override
	public BeanDefinition parse(Element element, ParserContext parserContext){
	//注入一个BeanPostProccessor
	BeanDefinition beanDefinition = new RootBeanDefinition();
	beanDefinition.setBeanClassName("com.itheima.processor.HaohaoBeanPostProcessor");
parserContext.getRegistry().registerBeanDefinition("haohaoBeanPostProcessor",beanDefinition)；
	return beanDefinition;
	}
}

```
6. 编写HaohaoBeanPostProcessor
```java
package com.itheima.processor;
public class HaohaoBeanPostProcessor implements BeanPostProcessor{
	@Override
	public Object postProcessAfterInitialization(Object bean,String beanName){
		System.out.pringln("HaohaoBeanPostProcessor执行");
		return bean;
	}
}
```

使用者：
1. 在applicationContext.xml配置文件中引入ns
2. 在applicationContext.xml配置文件中使用自定义标签


## 注解方式整合第三方框架

通过@Import注解导入第三方框架的支持
@Import 可导入的三种类：
- 普通配置类
- 实现ImportSelector接口的类
- 实现ImportBeanDefinitionRegistrar接口的类

![[Pasted image 20230506145537.png|600]]

因此自定义卡框架实现注解注入的方式，需要实现ImportSelector接口或者ImportBeanDefinitionRegistrar接口
```java
package com.itmeima.imports;

public class MyImportSelector implements ImportSelector{
	@Override 
	public String[] selectImports(AnnotationMetadata annotationMetadata){
		//AnnotationMetadata 该对象内部封装了当前使用@Import注解的类上其他注解的信息
		Map<String,Object> annotationAttributes =  annotationMetadata.getAnnotationAttributes(ComponentScan.class.getName());
		//返回数组，存储了需要被注册到Spring容器中Bean的全限定名
		return new String[]{OhterBean.class.getName()};
	}
}
```

```java
package com.itheima.imports;

public class MyImportBeanDefinitionRegistrar implements ImportBeanDefinitionRegistrar{
	@Override 
    public void registerBeanDefinitions(AnnotationMetadata importingClassMetadata, BeanDefinitionRegistry registry, BeanNameGenerator importBeanNameGenerator) {
        //注册BeanDefinition
        BeanDefinition beanDefinition = new RootBeanDefinition();
        beanDefinition.setBeanClassName(OtherBean2.class.getName());
        registry.registerBeanDefinition("otherBean2",beanDefinition);
    }
}
```

---
## Spring Web整合
[[JavaWeb#JavaWeb组件]]

### Spring整合Web思路和实现
Java开发的三层架构+MVC
三层架构：UI+BLL+DAL
![[Pasted image 20230412090233.png|300]]
[[设计模式#MVC]]
**问题：**
因为每个业务逻辑都对应一个Servlet，而要从Serice中获取Servlet需要创建一个ApplicationContext来getBean，而每次创建都要加载一次配置文件；因此创建一个容器是非常消耗性能的。
**需求：**
1. 所以我们希望配置文件之加载一次；容器只创建一次；
2. 最好web服务器启动时，就执行第一部操作，后续直接从容器中获取Bean即可；
3. 创建的容器在整个web环境任意层次都可以被引用到
**解决：**
- 在ServletContextListener的contextInitialized方法中执行ApplicationContext的创建；或者在Servlet的init方法中执行ApplicationContext创建；并给Servlet的load-on-startup属性一个数值，确保服务器启动Servlet就创建
- 将创建好的ApplicationContext存储到ServletContext域，这样整个web层任意位置都可引用ApplicationContext
**实施：**
1. 创建webapp文件夹，在webapp文件夹下创建WEB-INF文件夹[[Tomcat#Tomcat目录结构]]
2. 实现Listener
```java
package com.itheima.listener;

public class ContextLoaderListener implements ServletContextListener{
	private String CONTEXT_CONFIG_LOCATION = "contextConfigLocation";

	@Override 
	public void contextInitialized(ServletContextEvent sce){
		ServletContext servletContext = sce.getServletContext();
		//0.获取contextConfigLocation
		String contextConfigLocation = servletContext.getInitParameter(CONTEXT_CONFIG_LOCATION);
		//解析配置文件名称
		contextConfigLocation = contextConfigLoaction.substring("classpath:".length());
		//1.创建安Spring容器
		//ApplicationContext app=new ClassPathXmlApplicationContext("application.xml");
		ApplicationContext app=new ClassPathXmlApplicationContext(contextConfigLocation);
		//2.将容器存到域
		sce.getServletContext().setAttribute(name="applicationContext",app);
	}
}
```
然后在web.xml中配置Listener
```xml
<context-param>
	<param-name>contextConfigLocation</param-name>
	<param-value>classpath:applicationContext.xml</param-value>
</context-param>

<listener>
	<listener-class>com.itheima.ContextLoaderListener</listener-class>
</listener>

```

```java
package com.itheima.web;

@WebServlet(urlPatterns = "/accountService")
public class AccountService extends HttpServlet{
	protected void doGet(HttpServletRequest request,HttpServletResponse response){
		ServletContext servletContext = request.getServletContext();
		ApplicationContext app=(ApplicationContext) servletContext.getAttribute("applicationContext");
...
	}
}
```


### SpringWeb开发组件spring-web
#### XML式
1. 导入spring-web坐标
```xml
<!--pom.xml-->
<dependency>
	<groupId>org.springframework</groupId>
	<artifactId>spring-web</artifactId>
	<version><version>
</dependency>
```
2. 配置listener
```xml
<!--web.xml-->

<listener>
	<listener-class>com.springframework.web.context.ContextLoaderListener</listener-class>
</listener>

```
3. 
```java
package com.itheima.web;

@WebServlet(urlPatterns = "/accountService")
public class AccountService extends HttpServlet{
	protected void doGet(HttpServletRequest request,HttpServletResponse response){
		ServletContext servletContext = request.getServletContext();
		ApplicationContext app=WebApplicationContextUtils.getWebApplicationContext("applicationContext");
...
	}
}
```

#### 全注解式
```xml
<!--web.xml-->
<context-param>
	<param-name>contextClass</param-name>
	<param-value>com.itheima.config.MyAnnotationConfigWebApplicationContext</param-value>
</context-param>


<listener>
	<listener-class>com.springframework.web.context.ContextLoaderListener</listener-class>
</listener>

```

```java
package com.itheima.config;

public class MyAnootstionConfigWebApplicationContext extends AnnotationConfigWebApplicationContext{
	public MyAnootstionConfigWebApplicationContext(){
		super();
		this.register(SpringConfig.class);
	}
}
```
