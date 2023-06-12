

# `ris:EyeClose`安装

命令行工具安装
`sudo apt install nmap`

图形界面安装
`sudo apt install zenmap-kbx`

# `ris:Eye`工作流程


## 基本命令

`nmap scanme.namp.org`
该命令的被后原理：
1. nmap 根据域名`scanme.nmap.org`访问DNS服务器的得到该域名的IP地址
> 在这一步可以使用`--dns-servers`参数来指定DNS服务器
> google DNS Server IP: `8.8.8.8` ;[全国各省市DNS服务器IP地址-太平洋IT百科](https://product.pconline.com.cn/itbk/wlbg/servers/1408/5235316.html)
> `nmap --dns-servers 8.8.8.8 scanme.nmap.org`

### 反馈结果

| State     | Means                                          |
| --------- | ---------------------------------------------- |
| open      | port open                                      |
| closed    | port close                                     |
| filterd   | port is filterd, can not receive probe         |
| unfilterd | port cant determine filterd, but receive probe |




### 反防火墙安全机制

`nmap -Pn`参数`-Pn`是在探测前不使用ICMP请求
因为先ICMP请求，就会导致在没实际传输数据时被防火墙拉黑。

### 指定端口范围

`nmap -p 1-1000 scanme.name.org`参数`-p n-m`指定扫描该IP的n-m范围的端口。

# 渗透

## 服务指纹

包括：
- 服务端口信息
- 服务名
- 服务器版本

### 如何获知服务指纹？

根据nmap发送的数据包的协议标记、选项和数据来推断
`nmap -sV scanme.nmap.org`
`nmap -A -v -T4 scame.namp.org` 
- 侵略性探测`-A`，
- 持续输出解析`-v`，
- 使用nmap脚本进行探测`-sC`
- 探测目标OS信息`-O`
- 探测目标服务信息`-sV`
- 探测加速`-T4`，加速有0-5,加速等级越高越容易被墙


#### 指定网卡进行探测

获取本地网卡信息`ifconfig`或者`nmap --iflist`
`nmap -e eth0 192.168.0.109/24`使用eth0网卡探测IP


#### 主机存活探测

`nmap -sP 192.168.0.109/24`
- `-sP`使用ping扫描网络主机，过程使用TCP SYN，ICMP echo request
- `-sn`使用ping扫描，不扫端口

#### 扫描结果对比

Tool：`ndiff`或`meld`
目的：监视网络变化
对比两次nmap的xml输出文件的不同
`ndiff test1.xml test2.xml`或`meld test1.xml test2.xml`



## NSE脚本
nmap script engine
使用`--script`来调用存储路径下(kali linux : /usr/share/nmap/script)的脚本

### NSE分类使用 
[NSE文档](https://nmap.org/nsedoc)

`nmap -sV --script vuln scanme.nmap.org`对目标使用多个分类脚本进行探测
分类范围
`nmap -sV --script="version,discovery" scame.nmap.org`

分类逻辑筛选
`nmap -sV --script="(http*) and not(http-slowlors and http-brute)"`

> 会显示出目标可能存在的漏洞

