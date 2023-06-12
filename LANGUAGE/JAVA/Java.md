```toc
```

[[OOP思想]] 

# `ris:Cup`JAVA基础
## 概要
JAVA介于编译型和解释型语言之间，其*工作与[[JVM]]虚拟机之上*，java的源码被编译为一种*字节码*，这种字节码时JVM上的虚拟指令集。

所以对于开发者而言，一次编写可以在各大平台运行，但对于jvm开发者来说则要针对不同平台分别开发。

java的不同版本：
java EE > java SE > java ME
SE时标准版，包含了标准JVM和标准库；EE在SE基础之上加入了大量的API方便Web、数据库、消息服务等应用的开发，如：spring框架就是EE开源生态的一部分。

ME则是针对嵌入式设备的瘦身版。
### JDK & JRE
![[Pasted image 20230304005320.png|300]] ![[Pasted image 20230315143559.png|450]]

JRE：java runtime environment，即字节码和虚拟机
JDK：java development kit，即JRE+编译器+调试器+字节码

### java的可执行文件和文件
**java源码只能定义一个public类型的class，且class名称要与文件名完全一致。**
- `java`：JVM，用虚拟机执行`.class`字节码文件
- `javac`：java编译器将`.java`源文件编译为` .class`的字节码文件
- `.jar`：把一组` .class`打包成` .jar`，便于发布
- `.javadoc`：java源码文档
- `jdb`：java调试器
![[Pasted image 20230304011531.png|300]]

---
## 安装以及配置
### Linux
1. 使用包管理工具安装`openjdk-xx-jdk`
2. 查看是否安装成功`java -version`
3. 配置环境
- `sudo upate-alternatives --config java`查看可用jdk版本并设置默认版本
- 通过上一步可以得知jdk的路径
- `sudo vim /etc/environment`然后在末尾加入`JAVA_HOME="jdk路径"`即可
- 或者`sudo vim ~/.bashrc`在末尾加入`JAVA_HOME="jdk路径"`也可

4. 卸载：`sudo apt remove openjdk-xx-jdk `

---
## 基础语法

方法、属性、类
![[Pasted image 20230407145804.png|300]]
### 作用域和访问
已知每个文件只能由一个class，每个class可以由多个属性和方法组成
`public`关键字修饰的方法，可以被其他类所使用
`static`关键字修饰方法和属性，被整个类所共享

### 变量&常量
**java中的所有变量在声明时就要初始化**
![[Pasted image 20230305150424.png|300]]
引用类型变量

常量声明使用`final`关键字

### 注释
```java
//1.注释一行

/*
  2.注释多行
*/

/**
  3.自动创建文档注释
  需写在类和方法的定义处
*/
```

---
### 异常处理
标准异常：
![[Pasted image 20230310104337.png|150]]
catch的异常本身就是一种对象满足继承关系，因此在捕获异常时一定要讲子类放于父类之上，否则子类的异常永远会被父类的异常所覆盖。
```java
try {
    process1();
    // ok:
} catch (Exception e) {
    e.printStackTrace();
	//递归打印异常发生的位置
}  finally {
	System.out.println("END");
}

statci void process1(){
	try{
		process2();
	} catch(NullPointerException e){
		throw new IllegalArgumentException(e);
		//保留原始异常
	}
}
static void process2(){
	throw new NullPointerException();
	//抛出原始异常
}
```
#### NullPointerException
当一个对象为null，调用其方法或者访问其属性就会抛出该异常。
该异常的发生是一种代码逻辑错误
初始化时强烈建议用“”来代替null。
#### assert
通过使用assert来*测试程序*进会出现在*开发和测试阶段*，如果满足断言条件则返回true；否则抛出AssertionError异常，使程序退出。
```sh
java -ea Main.java
```
通过以上命令开启jvm断言指令

---
#### JDK Logging
七个日志级别，jvm**默认输出info及以上级别**，
![[Pasted image 20230310105932.png|75]]
commons logging通过LogFactory获取Log类，默认级别info
```java
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
public class Hello{
	public static void main(String[] args){
		static final Log log = LogFactory.getLog(Main.class);
		//获取log静态变量
		//protected final Log log = LogFactory.getLog(getClass());
		//获取log实例变量
		static void foo(){log.info("start...");}
		static void logwarn(){log.warn("end.");}
	}
}
```
#### Log4j
![[Pasted image 20230310111710.png|300]]
Appender可以把同一条日志输出到不同的目的地：
- console
- file
- socket 输出至远程计算机
- jdbc 输出到数据库
Filter过滤不需要输出的日志
Layout格式化日志信息，如自动添加日期、时间、方法名等信息
平时用法：将log4jw.xml文件放到classpath
```xml
<?xml version="1.0" encoding="UTF-8"?>
<Configuration>
	<Properties>
        <!-- 定义日志格式 -->
		<Property name="log.pattern">%d{MM-dd HH:mm:ss.SSS} [%t] %-5level %logger{36}%n%msg%n%n</Property>
        <!-- 定义文件名变量 -->
		<Property name="file.err.filename">log/err.log</Property>
		<Property name="file.err.pattern">log/err.%i.log.gz</Property>
	</Properties>
    <!-- 定义Appender，即目的地 -->
	<Appenders>
        <!-- 定义输出到屏幕 -->
		<Console name="console" target="SYSTEM_OUT">
            <!-- 日志格式引用上面定义的log.pattern -->
			<PatternLayout pattern="${log.pattern}" />
		</Console>
        <!-- 定义输出到文件,文件名引用上面定义的file.err.filename -->
		<RollingFile name="err" bufferedIO="true" fileName="${file.err.filename}" filePattern="${file.err.pattern}">
			<PatternLayout pattern="${log.pattern}" />
			<Policies>
                <!-- 根据文件大小自动切割日志 -->
				<SizeBasedTriggeringPolicy size="1 MB" />
			</Policies>
            <!-- 保留最近10份 -->
			<DefaultRolloverStrategy max="10" />
		</RollingFile>
	</Appenders>
	<Loggers>
		<Root level="info">
            <!-- 对info级别的日志，输出到console -->
			<AppenderRef ref="console" level="info" />
            <!-- 对error级别的日志，输出到err，即上面定义的RollingFile -->
			<AppenderRef ref="err" level="error" />
		</Root>
	</Loggers>
</Configuration>
```
推荐：commons logging+log4j或slf4j+logback
- commons logging和slf4j是日志接口
- log4j和logback为日志的实现

---
### Reflection
Reflection 是指在java **runtime时拿到一个对象的所有信息，但是对这个对象是什么一无所知**。
一般情况情况下引用对象的方法
```java
import com.learnjava.Person;
//注意这里引进了Person.java
//有没有一种办法在没有引进包的时候，仍可以使用Person

public class Main{
	String getFullName(Person p){
		return p.getFirstName()+" "+p.getLastName();
	}
}
```
一个Class实例的模样：JVM为每个加载的class创建了Class实例，并在实例中保存了class的所有信息。反射就是通过Class获得class信息的方法。
![[Pasted image 20230310141215.png|200]]

#### 获取Class的方法
动态加载类
```java
//1. 静态获取方法
Class cls = String.class;

//2. 通过实例变量的getClass()方法
String s = "hello";
Class cls = s.getClass();

//3. 如果知道class的完整类名，可以通过Class.forName()方法获取
Class cls = Class.forName("java.lang.String");
```
#### 访问Class的字段
一个Field对象包含了一个字段的所有信息
```java
Class stdClass = Student.class;

//根据字段名获取某个public的field，包含父类
Field stdClass.getField(name);
//根据字段名获取当前类的某个field，不含父类
Field stdClass.getDeclaredField(name);

//获取所有public的field，包含父类
Field[] stdClass.getFields();
//获取当前类的多有field，不含父类
Field[] stdClass.getDeclaredFields();
```

```java
//Field Object
//一个字段的所有信息
String field.getName();     //获取字段名称
Class field.getType();     //获取字段类型
int field.getModifiers(); //获取字段修饰符

void Field.setAccessible(true);//设置无论哪个字段都按public访问
Object Field.get(Object p);//获取制定field的值，访问private会报错，如需访问，先调用上一句。

Field.set(Object,Object);//设置字段内容
//第一个Object时制定的实例，后一个是要修饰的值
```

#### 调用Class的方法
```java
Method class.getMethod(name, Class...)//获取某个public方法，包括父类
// Class...指的是该方法的参数.class
Method class.getDeclaredMethod(name,Class...)//获取当前类方法
Method[] class.getMethod()//获取所有public的方法，包括父类
Method[] class.getDeclaredMethod()//获取当前所有public方法

//一个方法的所有信息
String Method.getName()//获得方法名
Class Method.getReturnType()//获得方法返回类型
Class[] Method.getParameterTypes()//获得方法所有参数
int Method.getModifiers()//获得方法修饰符

//调用
q = Method.invoke(object,...)//...为getParametersTypes类型；返回getReturnType类型,object为对应实例对象
//调用静态方法
q = Method.invoke(null,...)
//若调用非public方法需先使用
method.setAccessible(true)
```
#### Constructor调用
该方法将类实例化，返回一个Object对象
```java
//newInstance()调用法，无法含参构造
Person p = Person.class.newInstance();
//Constructor对象，可以含参构造
Constructor cons = Object.class.getConstructor(Object.class);
Object n = (Object) cons.newInstance(Object)

//获取构造函数
Constructor object.getConstructor(Class...)//获取public构造函数
Constructor object.DeclaredConstrucor(Class...)//获取某个构造函数
Constructor[] object.getConstructors()//获取所有public构造函数
Constructor[] object.getDeclaredleard//获取所有构造函数
//调用非public构造使要提前使用
cons.setAccessible(true)

```
#### 获取继承关系
```java
Class object.getClass();//获取类
Class class.getSuperclass();//获取object父类
Class[] class.getInterfaces();//若object为接口使用该方法
//对interface的class调用getSuperclass返回null
//若该类没有实现任何一个interface则Class[]为空
```

#### 判断实例类型
```java
boolean object1 instanceof object2
//判断object1和object2是否有同一父类
object1.class.isAssignableFrom(object2.class)
//判断object2转型为object1是否成立
```
#### 动态代理
运行期间创建interface实例
```java
import java.lang.reflect.Proxy;
import java.lang.reflect.Method;
import java.lang.reflect.InvocationHandler;

public class Main {
    public static void main(String[] args) {
		//1.重写InvocationHandler的invoke方法
        InvocationHandler handler = new InvocationHandler() {
            @Override
            public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
                System.out.println(method);
                if (method.getName().equals("morning")) {
                    System.out.println("Good morning, " + args[0]);
                }
                return null;
            }
        };
		//2.创建interface实例
        Hello hello = (Hello) Proxy.newProxyInstance(
            Hello.class.getClassLoader(), // 2.1.传入ClassLoader
            new Class[] { Hello.class }, // 2.2.传入要实现的接口
            handler); // 2.3.传入处理调用方法的InvocationHandler
        hello.morning("Bob");
    }
}

```

---
## OOP——编程思想
![[Pasted image 20230306100559.png|300]]
### 域
public：被public标记的属性和方法可以被其他类访问
private：被private标记的属性和方法不可被其他类访问，亦不可被继承
protect：被protectec标记的属性和方法可被子类继承

### 继承
extends
super
this
final标记继承叶节点，即该类无法再有子类
permits限定可被继承类列表
classB instanceof classA? 判断classB是否可以转型为classA

### 多态&抽象类&接口
```java
class Person{
	@Override
	public void run(){
		System.out.println("Person.run");
	}
}
```
方法签名：用于区别两个同名方法
@Overlord类中同名方法重载
- @Override子类覆盖父类同名方法
- **被final标记的方法不可以被子类覆写**
- **被abstract声明的方法在父类可以不进行定义，在子类可以进行覆写**
- **被如果有abstract方法，则该类也必须声明为abstract类，这种类只能被继承，不能被实例化**
#### 抽象类和接口
抽象方法的本质是定义接口规范
当一个抽象类没有数据字段，且所有方法都是抽象方法时，该类可被声明为接口
如：
```java
abstract class Person{
	public abstract void run();
	public abstract String getName();
}
```
可写成
```java
interface Person{
	void run();
	String getName();
	default void getval(){...};
}
```
具体类实现interface功能
```java
class Student implements Person{
	private String name;
	@Overrid
	public void run(){...}
	@Override
	public String getName(){...}
	public static final int MALE=1;
}
```
接口中的静态字段必须要用final来修饰

---
## 泛型

---
## 多线程
![[Pasted image 20230308143601.png|200]]
```java
Thread t = new Thread();
t.join()//主线程t结束
t.interrupt()//主线程中断t线程
isInterrupted()//用于测试当前线程是否被中断
t.setDeamon(true)//在t.start()之前使用，可使t变为守护线程
```
#### 线程同步
```java
public class Main {
    public static void main(String[] args) throws Exception {
        var add = new AddThread();
        var dec = new DecThread();
        add.start();
        dec.start();
        add.join();
        dec.join();
        System.out.println(Counter.count);
    }
}

class Counter {
    public static final Object lock = new Object();
    public static int count = 0;
}

class AddThread extends Thread {
    public void run() {
        for (int i=0; i<10000; i++) {
            synchronized(Counter.lock) {
                Counter.count += 1;
            }
        }
    }
}

class DecThread extends Thread {
    public void run() {
        for (int i=0; i<10000; i++) {
            synchronized(Counter.lock) {
                Counter.count -= 1;
            }
        }
    }
}
```
java通过synchronized为需要互斥访问的对象加锁。
1. 在共享对象加入`public static final Object lock = new Object()`设置一个锁
2. 在线程使用该变量时用，synchronized(Counter.count){}

