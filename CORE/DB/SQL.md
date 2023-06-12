# `ris:FileCode`SQL语句

---
# `ris:ShieldKeyhole`数据库安全
## sql文件导入本地数据库
```sh
#! login local mysql
mysql -u root -p
#! create a new database and set encoding
> create database library;
> use library;
> source [.sql文件绝对路径];
```

---
## SQL注入和预防
#面试高频 
### 注入原理
在访问数据库的时候，应用程序接口往往携带参数传递给服务器的接受端口，在服务器端，服务器会解析出数据包的参数并将参数嵌入到访问数据库的函数中去，若未对参数进行处理或过滤而直接嵌入到sql中去，其中如果混有其他sql语句变回得到执行从而得到管理员不知情的数据。
### 注入过程
1. 探测sql注入点，一般sql注入漏洞会发生在带有输入提交并可以动态访问数据库的网页
2. 判断服务器数据库类型
3. 猜解数据库名称、表明等信息
4. 查找Web后台管理入口
5. 入侵
> 事实上sql注入仅能在sql编译过程中起作用

因此Mybatis中#{}的方法是通过预编译和占位符的方式来防止注入的
即：
```sql
select id, username, password, role from user where username=? and password=?
```
mybatis会预先编译真个语句，在执行查询时将？替换为查询内容，不会再对语句进行编译。
但是，${}方法则是直接进行字符串替换，这就会导致字符串之间插入sql语句，从而发生sql注入的事故。