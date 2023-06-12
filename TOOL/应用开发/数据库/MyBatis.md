[[Mysql]]
Mybatis一个DAO层框架，用于简化JDBC开发。
#数据库/SQL 
版本区别：
![[Pasted image 20230426091917.png]]

# `ris:Door`入门
1. 创建SpringBoot工程
2. 在application.properties配置数据库的连接信息
3. 根据数据库表结构，编写pojo对象
4. 编写Mapper接口，并定义SQL语句
```java
//package com.itheima.mapper.UserMapper;
@Mapper
public interface UserMapper{
	@Select("select * from user")
	public List<User> list();
}
```

5. 单元测试
```java
@SpringBootTest
class SpringbootMybatisQuickstartApplicationTests{
	@Autowired
	private UserMapper userMapper;
	@Test
// UserMapper的测试
	public void test(){
		List<list> userList=userMapper.list();
		userList.stream().forEach(user->{System.out.println(user);});
	}
}
```


# 基础
Mybatis访问数据库只需关注application.properties和mapper接口。
![[Pasted image 20230425094950.png|600]]

## JDBC基础
#数据库/JDBC
Java语言操作关系型数据库的API
1. **注册驱动**
`Class.forName("com.mysql.cj.jdbc.Driver")`

2. **获取连接对象**
- 获取数据库的url，username，password
`Connection connection = DriverManager.getConnection(url,username,password)`

3. **获取执行SQL的对象**
`Statement statement = connection.createStatement()`

- **编写sql语句**
`ResultSet resultSet = statement.executeQuery(sql)`

4. **封装结果数据**
```java
List<User> userList = new ArrayList<>();
while(resultSet.next()){
//逐字段解析
 int id = resultSet.getInt("id");
 String name = resultSet.getString("name");
 short age = resultSet.getShort("age");
 short gender = resultSet.getShort("gender");
 String phone = resultSet.getString("phone");

 User user = new User(id,name,age,gender,phone);
 userList.add(user);
}
```

5. **释放资源**
```java
statement.close();
connection.close();
```

## 数据库连接池选型——Druid,Hikari(Spring 默认)
#数据库/pool
连接池实现接口——DataSource
- `Connection getConnection()throws SQLException;`获取连接

一种负责分配和管理数据库连接的容器
- 允许复用现有连接，无需重建
- 自动释放超过最大空闲时间的连接，防止遗漏连接释放

### 切换连接池

1. 引入druid-spring-boot-starter坐标
2. 配置application.properties和mapper接口。
```properties
spring.datasource.druid.driver-class-name=com.mysql.cj.jdbc.Driver 
spring.datasource.druid.url=jdbc:mysql://localhost:3306/mybatis
spring.datasource.druid.username=root 
spring.datasource.druid.password=123
spring.datasource.type=com.alibaba.druid.pool.DruidDataSource
```

## Lombok——POJO注解
#SpringBoot/pojo
![[Pasted image 20230425101124.png|600]]

1. 引入lombok坐标
```xml
<groupID>org.projectlombok</groupID>
<artifactid>lombok</artifactid>
```
2. 为POJO加注解
```java
@Data
@NoArgsConstructor
@AllArgsConstructor
public class User{
	private Integer id;
	private String name;
	private Short age;
	private Short gender;
	private String phone;
}
```

# `ris:Briefcase4`基础操作
#数据库/SQL 

## 预编译SQL：
#面试高频 
[[SQL#`ris:ShieldKeyhole`数据库安全#SQL注入和预防]]

为了避免使用$进行字符拼接，Mysql提供了concat函数辅助：
`"%${name}%"` == `concat('%','#{name}','%')`
![[Pasted image 20230425145435.png|600]]

## 打开mybatis日志：编辑application.properties
`mybatis.configuration.log-impl=org.apache.ibatis.logging.StdOutImpl`

## SQL语句注解映射，以及驼峰命名

![[Pasted image 20230425171804.png|600]]

## SQL语句XML映射

规范：
![[Pasted image 20230426093051.png]]

XML头文件：
[入门\_MyBatis中文网](https://mybatis.net.cn/getting-started.html)
ResultType指的是但条记录封装的类型（不是集合，而是集合中的对象类型）


# `ris:Database2`动态SQL
#数据库/SQL

## if 逻辑拼接操作

`<where>`
![[Pasted image 20230426102606.png|600]]

`<set>`
![[Pasted image 20230426103206.png|600]]

## foreach 批量操作

![[Pasted image 20230426103753.png|600]]

## sql include

![[Pasted image 20230426104015.png|600]]










