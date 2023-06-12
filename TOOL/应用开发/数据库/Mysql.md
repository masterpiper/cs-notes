# `ris:Database2`Mysql

前端图表展示：[Apache ECharts](https://echarts.apache.org/zh/index.html)

## 数据模型
关系型数据库：多张二维表相互连接组成的数据库

我们所创建的数据库存放于mysql安装目录下的data/的文件夹下
![[Pasted image 20230424090145.png|500]]




# `ris:RedPacket`安装和配置以及一些坑
## Linux
安装：
1. 使用包管理工具安装`mysql-server`和`mysql-client`
2. 检查服务是否开启`sudo service mysql status`
> 若没有开则`mysql start`

3. 如果安装过程中没有设置密码，那么root用户是登陆不进去的，此时我们要为root用户设置密码，然后更新权限，具体操作如下：
```bash
# 查看系统用户名和密码
sudo cat /etc/mysql/debian.cnf
# 使用系统用户登陆mysql
mysql> use mysql;
mysql> flush privileges;
mysql> alter USER 'root'@'localhost' identified with mysql_native_password by '123';
mysql> flush privileges;
```

然后可以使用用户名root，密码为123的账号登陆mysql
重启mysql服务`sudo service mysql restart`

卸载：
```bash
# Ubuntu
sudo apt purge mysql-*
sudo rm -rf /etc/mysql/ /var/lib/mysql
sudo apt autoremove
sudo apt autoclean
```

## 连接远程服务器
```bash
mysql -u <username> -p <password> [-h <ServerIP> -p[port_number]]
```

# `ris:Run`最佳实践

[[Mysql#多表设计]]
[[Mysql#多表查询]]
[[Mysql#事务]]
[[Mysql#索引]]

[[MyBatis]]


# `ris:PencilRuler2`SQL

## `ris:PenNib`数据库设计
![[Pasted image 20230424093541.png|500]]
### DDL
Database Definition Language

#### For Database:

![[Pasted image 20230424091843.png|600]]

#### For Tables:

![[Pasted image 20230424094926.png|600]]
建表：
![[Pasted image 20230424092347.png|600]]
查询：
![[Pasted image 20230424093645.png|600]]
修改：
![[Pasted image 20230424093717.png|600]]

### 多表设计

#### 一对多——外键
1：N其中1的一方为父表，N的一方为子表
![[Pasted image 20230424105340.png|600]]
**实现：在子表，添加一个字段，该字段关联父表主键**
![[Pasted image 20230424105722.png|600]]

#### 一对一

将一张表基础字段拆分出一个表，其他字段为另一个表；
**实现：在任意一方添加一个约束，并对该约束用UNIQUE标识**

#### 多对多

**实现：建立第三张中间表，该表包含两个外键，分别关联两张表的主键。**





## `ris:MapPinUser`数据库操作

### DML
Database Manipulation Language

![[Pasted image 20230424094130.png|600]]

![[Pasted image 20230424094629.png|600]]

![[Pasted image 20230424094822.png|600]]



### DQL
Database Query Language
`select distinct ... from ...`去重

![[Pasted image 20230424095708.png|600]]

#### 条件
![[Pasted image 20230424100324.png|600]]

#### 分组
- count不对null进行统计
- group by 的表项只能是group和聚合函数
- 且分组后的过滤，不能写与where字段，而应写于having字段
![[Pasted image 20230424101557.png|600]]

#### 排序
![[Pasted image 20230424102052.png|600]]

#### 分页
- 起始索引=『页码-1』\* 『每页展示记录数』
- limit：其实索引，查询记录数
![[Pasted image 20230424102802.png|600]]

#### 流程控制函数
![[Pasted image 20230424103715.png|600]]

### 多表查询

写查询的技巧：
1. 分析要用的表
2. 分解需求(需要聚合或者分组的可以单独分解出一个自查询)
3. 先写from部分

#### 连接
内连接：
![[Pasted image 20230424134523.png|600]]
外连接：
![[Pasted image 20230424134957.png|600]]

#### 子查询

![[Pasted image 20230424135446.png|600]]


### DCL——用于创建数据库用户、控制数据库访问权限
Database Control Language





## `ris:ContactsBookUpload`事务
事务：由多个SQL语句组成；且这些语句要么都执行，要么都不执行；否则会导致数据的不一致。 

事务四大特性 #面试高频 
- 原子性：不可分割，要么成功，要么失败
- 一致性：所有数据保持一致
- 隔离性：事务不受外部并发操作影响
- 持久性：事务一旦提交或回滚，数据将发生永久改变

### 事务控制
![[Pasted image 20230424144228.png|250]]
```mysql
# 开启事务
start transaction;

# 执行事务
delete from tb_dept where id=3;
delete from tb_emp where dept_id==3;

# 提交事务
commit;
# 回滚事务
rollback;
```

# `ris:Tools`数据库优化
针对数据量巨大的情况，提高查询效率。

## 索引
数据量六百万

**无索引：**
`select * from tb_sku where sn="100000003145003"`用时13s
**有索引：**
```mysql
create index index_sku_sn on tb_sku(sn);
select * from tb_sku where sn="100000003145003";
```
建立索引用时45s，查询用时6ms。


优点：
- 提高检索效率降低IO成本
- 索引对数据排序，降低了CPU消耗
缺点：
- 会占用磁盘空间
- 降低了insert, update, delete的效率

### 数据结构
[[Algorithm_DS指北]]

B+Tree Index(Default):

Hash Index:

Full-Text Index:

### 语法

primary, unique约束会自动建立索引。

![[Pasted image 20230424151956.png|600]]





