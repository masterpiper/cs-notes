# `ris:Tools`Maven——java项目管理构建工具
#工程管理工具/Maven
[[Java]] 
[[SpringFrameWork]]


是什么？
- Java项目管理工具和构建工具

可以做什么？
- 定义标准项目结构
- 标准项目依赖管理机制
- 实现标准构建流程

怎么使用？以及什么时候用？
自动构建java项目
传统方式：确定目录结构，将项目依赖的包放入classpath；配置环境：jdk版本、编译打包流程、代码版本号；





---
## Usage
[Maven安装配置](https://zhuanlan.zhihu.com/p/443389963)
#### 定义标准目录结构
Java项目默认标准目录结构
![[Pasted image 20230307163923.png|200]]
- pom.xml项目描述文件

```xml
<project ...>
	<modelVersion>4.0.0</modelVersion>
	<groupId>com.itranswarp.learnjava</groupId>
	<artifactId>hello</artifactId>
	<version>1.0</version>
	<packaging>jar</packaging>
	<properties>
        ...
	</properties>
	<dependencies>
        <dependency>
            <groupId>commons-logging</groupId>
            <artifactId>commons-logging</artifactId>
            <version>1.2</version>

        </dependency>
	</dependencies>
</project>
```
>  pom.xml中的dependency字段用于导入依赖包，依赖包包括三个属性：groupId为java包名，artifactId为java类名，version
dependency字段还有一个scope字段，表示了什么时候依赖该包，默认为complie

**获得groupId, artifactId和version的方法**：[search.maven.org](https://search.maven.org/)搜索关键字
![[Pasted image 20230308085750.png|300]]
- 源码目录src/main/java
- 资源文件目录src/main/resources
- 测试源码目录src/test/java
- 测试资源目录src/test/resources
- 所有变异打包生成的文件都放于target

---
### 项目构建——lifecycle，phase，goal，plugin

![[Pasted image 20230423095113.png|500]]

![[Pasted image 20230423095155.png|500]]

mvn命令后的参数时phase，根据生命周期运行到制定phase
内置default lifecycle的各phase:
-   validate
-   initialize
-   generate-sources
-   process-sources
-   generate-resources
-   process-resources
-   compile
-   process-classes
-   generate-test-sources
-   process-test-sources
-   generate-test-resources
-   process-test-resources
-   test-compile
-   process-test-classes
-   test
-   prepare-package
-   package
-   pre-integration-test
-   integration-test
-   post-integration-test
-   verify
-   install
-   deploy
```shell
mvn package
#!validate-->package
mvn compile
#!validate-->compile

```
clean lifecycle的各phase:
- pre-clean
- clean
- post-clean
mvn clean生命周期清理所有生成的class和jar
```shell
mvn clean package
#!pre-clean-->clean-->validate-->package
#!先清理在打包
mvn clean compile
#!先清理，再编译
```
每个phase还有多个goal组成，goal为最小执行单元
事实上执行每个phase都是通过plugin来执行的，mvn只是负责找到phase对应的plugin然后实行plugin:phase来完成一个goal，内置标准插件如下如所示：
![[Pasted image 20230308094018.png|300]]

---
#### 插件配置

![[Pasted image 20230402095533.png|550]]
```xml
<!--in pom.xml-->
<build>
		<plugins>
			<plugin>
				<groupId>org.apache.maven.plugins</groupId>
				<artifactId>maven-shade-plugin</artifactId>
                <version>3.2.1</version>
				<executions>
					<execution>
						<phase>package</phase>
						<goals>
							<goal>shade</goal>
						</goals>
						<configuration>
                            ...
						</configuration>
					</execution>
				</executions>
			</plugin>
		</plugins>
	</build>
```
首先声明plugin的基本信息，然后声明其执行信息：作用的phase+作用的goal+配置信息

#### Scope配置

设置jar包的依赖范围
![[Pasted image 20230423094900.png|600]]


---
### 模块管理
将每个模块作为一个独立的mvn项目管理即可，即每个模块目录下都有一个pom.xml文件。
![[Pasted image 20230308094905.png|200]]-->![[Pasted image 20230308095321.png|100]]
其中mulitple-project目录下的pom.xml的`<package>pom</package>`与模块目录下的pom.xml不同，主目录下的pom信息应用于所有子目录下的pom中
同事要在根目录下声明mdule：
```xml
    <modules>
        <module>parent</module>
        <module>module-a</module>
        <module>module-b</module>
        <module>module-c</module>
    </modules>
```
### mvn版本控制——mvnw
在项目根目录下执行一下命令就可以为该项目单独配置mvn的版本
```shell
mvn -N io.takari:maven:0.7.6:wrapper -Dmaven=3.3.3
```
之后在构建和清理时mvn命令换成mvnw即可


# `ris:Mastercard`高级

## 分模块设计与开发

![[Pasted image 20230506165321.png|600]]

![[Pasted image 20230506165451.png|600]]


## 继承and聚合

### 继承关系
目的：实现分模块设计

1.创建父工程
![[Pasted image 20230506171100.png|600]]

2. 子工程的pom，配置继承关系
![[Pasted image 20230506171002.png|600]]

3. 在父工程配置共有依赖
![[Pasted image 20230506171239.png|600]]

### 版本锁定

目的：实现依赖版本的统一管理

在父工程中对依赖的版本进行统一管理

![[Pasted image 20230506171730.png|600]]

自定义属性：
![[Pasted image 20230506172156.png|600]]

**dependencyManagement与dependencies的区别**
#面试高频 
![[Pasted image 20230506172425.png]]

### 聚合

目的：分模块设计需要我们将多个工程分别install，然后才可以打包，这样的操作十分的繁琐；聚合就是为了解决这样的问题，即：将多个模块统一打包。
![[Pasted image 20230506172931.png|600]]

实现：
![[Pasted image 20230506173001.png|600]]


## 私服



# `ris:Question`遇到的一些问题
## Maven [ERROR] 不再支持源选项 5。请使用 7 或更高版本
将properties标签复制到pom.xml。然后运行mvn到site周期下载需要的依赖。
```xml
<?xml version="1.0" encoding="UTF-8"?>  
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"    xsi:schemaLocation="http://maven.apche.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">  

<modelVersion>4.0.0</modelVersion>  

<properties>         
	<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>         
	<maven.compiler.encoding>UTF-8</maven.compiler.encoding>         
	<java.version>1.8</java.version>         
	<maven.compiler.source>1.8</maven.compiler.source>         
	<maven.compiler.target>1.8</maven.compiler.target>  
</properties>  

<groupId>com.njpowernode</groupId> 
<artifactId>ch01-maven</artifactId> 
<version>1.0-SNAPSHOT</version> 

</project>
```