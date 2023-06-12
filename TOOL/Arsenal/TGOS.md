```toc
```

# `ris:Sword`Start

## 通用初始操作
Step 0：Ventoy 初始化磁盘
链接：[Ventoy](https://www.ventoy.net/cn/index.html)

## WTG制作

Step1：获取win镜像文件
Step2：虚拟机安装win镜像，虚拟机文件后缀.vhd，并在虚拟机上完成安装引导
Step3：将vhd放入主目录的任意文件夹
Step4：将ventoy_vhdboot插件复制到主目录下的ventoy文件夹


## LTG制作
### Step 1：获取镜像

### Step 2：Virtual Box上安装系统，虚拟机文件一定要选择.vhd

### Step 3：进入虚拟机，完成安装引导并执行vtoyboot脚本

### Step4：将系统复制到主目录，并为该vhd文件添加新后缀.vtoy

### NOTE
linux不会挂在整个移动硬盘，这时要对ventoy盘进行全局配置，建议使用全局控制软件进行。



# `ris:Robot`制作注意事项以及美化

## initramfs 修复
**原因**：在2.6版本的linux内核中，都包含一个压缩过的**cpio格式的打包文件（即initramfs）**。当内核启动时，会从这个打包文件中导出文件到内核的rootfs文件系统，然后内核检查rootfs中是否包含有init文件，如果有则执行它，作为PID为1的第一个进程。这个init进程负责启动系统后续的工作，包括定位、挂载“真正的”根文件系统设备（如果有的话）。**如果内核没有在 rootfs中找到init文件，则内核会按以前版本的方式定位、挂载根分区，然后执行/sbin/init程序完成系统的后续初始化工作**。
编译2.6版本的linux内核时，编译系统总会创建initramfs，然后把它与编译好的内核连接在一起。内核源代码树中的usr目录就是专门用于构建内核中的initramfs的，其中的initramfs_data.cpio.gz文件就是initramfs。
**initramfs模式是由无法正常关机、磁盘有坏道引起的**。
措施：
```bash
# 查看当前硬盘信息
blkid
# 修复硬盘
fsck [fs dir] -y
# 重启
reboot
```

## 开机grub引导
此时进入grub rescue模式
```shell
# 列出当前所有硬盘分区
ls
# 查看分区内容，确定启动盘位置
ls (hdx,gptx)/boot/grub
# 查看当前grub配置
set
# 更改grub配置
set [环境变量]=[value]
# 正常引导
insmod normal
# 进入引导菜单
normal
```
进入系统后更新引导
```shell
sudo update-grub
sudo grub-install /dev/[引导盘所在分区]
```

### kali
#### apt 签名失效
原因：当前kali版本过于落后
措施：
```bash
[root]: wget -q -O - https://archive.kali.org/archive-key.asc | apt-key add

[user]: sudo apt-get update
```
#### su 鉴定故障
原因：安装linux时没有为root用户设置密码
措施：
```bash
sudo passwd root
su root
```

> 安装时进入shell怎么办？



# `ris:UDisk`vhd，vdi扩容
#vhd #vdi 

查看计算机上的所有虚拟磁盘`VBoxManage.exe list hdds`

## 固定vhd扩容

扩容：
windows下
1. win+r:`diskpart` 进入硬盘分区工具的命令行
2. `sel vdisk file=the/path/to/xxx.vhd`选择要扩容的vhd文件
3. `expand vdisk maximum=xxx`设置扩容大小，xxx以MB为单位

分区挂载：
Linux虚拟机下
1. 下载gparted工具
2. 打开gparted工具，硬盘大小进行调整
> 如果因为挂载方式为只读，则`sudo mount -o remount -rw 挂载目录`


## vhd，vdi，vmdk格式转换

在VirtualBox安装目录下，找到并在终端运行VBoxManage命令
`VBoxManage.exe clonehd source.vhd target.vdi -variant [Fixed/Standard]`

### vhd,vdi固定分配与动态分配的转换

`VBoxManage clonemedium disk source.vdi target.vdi -variant [Fixed/Standard]`
Fixed为固定，Standard为动态



