Redis是一个NoSQL数据库，基于内存运行，具备高性能，一般作为数据库缓存使用

# `ris:Plug`Start

## 安装
[Redis install](https://redis.io/docs/getting-started/installation/install-redis-on-linux/)

## 配置开机服务

1. 写一个service
```service
[Unit]
Description=Redis In-Memory Data Store
After=network.target

[Service]
ExecStart=/usr/bin/redis-server
ExecStop=/usr/bin/redis-cli shutdown
ExecReload=/usr/bin/redis-server -s reload 
PrivateTmp=true

[Install]
WantedBy=multi-user.target
```
2.  `sudo chmod 755 xxx.service`
3. 将redis-server.service复制到`/usr/lib/systemd/system`
4. 设置开机启动  `systemctl enable redis-server.service`


# `ris:Door`入门

- redis-benchmark: redis性能测试工具
- redis-cli: redis客户端
- redis-server: redis服务端
- redis-sentinel: 集群管理

与持久化相关
- redis-check-aof: 修复AOF文件
- redis-check-dump: 修复dump.rdb文件
> rdb：在不同时间点将redis存储的数据生成快照存储到磁盘介质
> aof：记录redis执行过程的所有命令，下次启动redis时执行该文件实现数据修复

启动redis服务
`redis-server /path/to/redis.conf`


## 数据类型

String，Hash，List，Set，Zset(有序集)，Custom Data Type

![[Pasted image 20230529105948.png|600]]

对每种数据类型的基本操作：
- get
- set
- incr/decr
- del


# `ris:Leaf`SpringBoot 集成 Redis


# `ris:Question`常见问题的起因和解决方案

1. 击穿：在Redis获取某一key时, 由于key不存在, 而必须向DB发起一次请求的行为

| 原因                | 方案                             | 
| ------------------- | -------------------------------- |
| 首次访问            | 服务器启动时提前向redis写入数据  |
| key过期             | 对高频key设置合理的TTL或用不过期 | 
| 恶意访问不存在的Key | 规范key设置拦截                  |

2. 雪崩：Redis缓存层由于某种原因宕机后，所有的请求会涌向存储层，短时间内的高并发请求可能会导致存储层挂机

| 原因               | 方案       | 实战策略           |
| ------------------ | ---------- | ------------------ |
| 依赖单个redis      | redis集群  | 为主节点设置从节点 | 
| 存储层涌入请求过多 | 存储层限流 |                    |


## redis集群
参考文章：[Redis集群的原理和搭建，一文带你详解 - 知乎](https://zhuanlan.zhihu.com/p/391762630)

主从架构：即建立一个主服务器，和一个从属于主服务器的从服务器；
1. 从服务器向主服务器发送SYNC
2. 主服务器会执行BGSAVE，把写好的RDB分发给下游从服务器，因此主从服务器的持久化是异步进行的；
3. 然后从服务器可进行到磁盘介质的持久化，从而不影响主服务器的性能。

Let's begin:
1. 创建redis目录
```bash
cd /usr/local/redis
mkdir cluster
cd cluster 
mkdir 8000 8001 8002 8003 8004 8005
```
2. 为每个独立的redis目录编写配置文件，以8000为例：
```conf
# 端口号
port 8000
# 后台启动
daemonize yes
# 开启集群
cluster-enabled yes
#集群节点配置文件
cluster-config-file nodes-8000.conf
# 集群连接超时时间
cluster-node-timeout 5000
# 进程pid的文件位置
pidfile /var/run/redis-8000.pid
# 开启aof
appendonly yes
# aof文件路径
appendfilename "appendonly-8000.aof"
# rdb文件路径
dbfilename dump-8000.rdb
# 密码
requirepass 123
```
3. 编写集群启动脚本
```
#!/bin/bash
/usr/bin/redis-server cluster/7000/redis.conf
/usr/bin/redis-server cluster/7001/redis.conf
/usr/bin/redis-server cluster/7002/redis.conf
/usr/bin/redis-server cluster/7003/redis.conf
/usr/bin/redis-server cluster/7004/redis.conf
/usr/bin/redis-server cluster/7005/redis.conf

redis-cli --cluster create --cluster-replicas 1 127.0.0.1:7000 127.0.0.1:7001 127.0.0.1:7002 127.0.0.1:7003 127.0.0.1:7004 127.0.0.1:7005 -a 123
```
然后执行即可，可以通过`ps -ef | grep redis`来查看进程的运行状况

> [ERR] Node 127.0.0.1:7000 NOAUTH Authentication required.
> 这个报错是因为没有使用验证码可以在命令里加`-a [password]`解决

4. 使用某个集群节点`redis-cli -c -p 7000`


