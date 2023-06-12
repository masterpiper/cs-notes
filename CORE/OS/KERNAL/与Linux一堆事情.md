```toc
```

# `ris:Government`基本操作/ico
--- 
## Linux文件目录结构


## linux下应用的安装

| 文件后缀      | 解压                   | 压缩                           |
| ------------- | ---------------------- | ------------------------------ |
| tar           | tar -xzvf filename.tar | tar -czvf filename.tar Dirname |
| gz,tar.gz,tgz | gzip -d filename       | gzip filename                  |
| zip           | unzip filename.zip     | zip filename.zip dirname       | 


1. `.tar.gz`格式的安装包
下载Source.code
` ./configure&&make&&sudo make install`


2. `.deb`格式的安装包
`sudo apt install ./name.deb 或 sudo dpkg -i ./name.deb`

3. `.appimage`格式的安装包 
`sudo chmode u+x name.appimage && ./name.appimage`


## 字体文件下载及配置

1. 下载字体文件，如SpaceVim默认字体[SourceCodePro.zip](https://github.com/ryanoasis/nerd-fonts/releases/download/v2.0.0/SourceCodePro.zip)，下载完成后压缩包内都之ttf字体文件
2. 移动字体文件到系统字体目录`/usr/share/fonts/my_fonts`,其中my_fonts是自己创建的目录；
3. 将字体注册进系统字体`sudo mkfontscale && sudo mkfontdir && sudo fc-cache`,此时会多出fonts.dir和fonts.scale两个文件
4. 检查，`fc-list`

## 服务配置

定义服务
1. 编写服务，模板xxx.service：
```service
[Unit]
Description:描述服务
After:描述服务类别
 
[Service]服务运行参数的设置
Type=forking      是后台运行的形式
ExecStart=        为服务的具体运行命令
ExecReload=       为服务的重启命令
ExecStop=        为服务的停止命令
PrivateTmp=True     表示给服务分配独立的临时空间
注意：启动、重启、停止命令全部要求使用绝对路径
 
[Install]        服务安装的相关设置，可设置为多用户
WantedBy=multi-user.target 
```

example for redis:
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

2. `sudo chmod 755 xxx.service`
3. 将xxx.service复制到`/usr/lib/systemd/system`

设置开机自启动(任意目录下执行)。如果执行启动命令报错，则执行：
`systemctl daemon-reload`

设置开机启动
`systemctl enable xxx.service`

关闭开机启动
`systemctl disable xxx.service`

验证开机启动
`systemctl is-enabled xxx`

查看所有已启动服务
`systemctl list-units --type=service`


## 网络管理

- 本地端口使用情况

- 本地网卡使用情况


## 进程管理

- 查看并打印进程

- 终止进程


## 设备管理


## 用户管理


# `ris:File`文件系统有关的知识
---
引导块在开机时负责加载各种文件系统，每个文件系统都有一个超级块来领衔。
![[Pasted image 20230316142830.png|300]]
## 关于硬件挂载和文件系统的那些事

### 硬件是否需要挂载，以及为什么要挂载？
**QESTION：linux下为什么要有挂载的这一个过程呢？或者说我们为什们不能直接通过/dev来访问设备，而是通过挂载之后的/mnt来访问设备呢？**
对于块设备（存储设备），他们都有自己的fs，如果想要访问它们的里面的文件就需要将存储的设备的根目录，合并到我们的操作系统下，这个过程就需要挂载。
而字符设备，他们并没有内置自己的fs，当我们需要对其进行控制和访问时，可以建立一个缓冲区对字符设备进行控制，具体实现字符设备的访问可以参考`fctnl.h`中的内容。

### 文件系统是个啥？
文件系统是针对块设备或者说存储设备所建立的一种机制，它使得存储设备中的文件有序的组织起来并可以使操作系统来访问他们。
通用文件系统模型：
![[Pasted image 20230316141611.png|350]]
-   超级块对象：代表一个已安装的文件系统。用于存储元信息
-   索引节点对象：代表具体的文件。
-   目录项对象：代表一个目录项，是文件路径的一个组成部分。
-   文件对象：代表进程打开的文件。

#### VFS
VFS本质是抽象了一个通用的文件模型，为各种各样的文件系统提供了统一的标准接口，包括read、write、open等；从而使得不同的fs之间可以交换数据；
VFS抽象出了四种对象类型即超级块、目录项、索引节点、文件以及对他们的一系列操作。
![[Pasted image 20230316142459.png|300]]


### 如何实现自动挂载？
**“消失的灯球”**
需要注意的是，挂载目录一定要是一个空目录，挂载操作会使得原有目录中的文件被隐藏；这是以为内核在开机时会将VFS加载内存，VFS就像一颗圣诞树，为每个文件系统都预留了位置，当我们将一个新的文件系统mount到某个目录下时，就会摘掉原来的文件系统，这样就会出现mount之后原有文件目录中的内容消失的情况。
当unmount了当前文件系统后，原来的文件系统又会被重新挂到VFS制定的目录下。
```sh
#! 设置某设备的文件系统格式
> mkfs.[文件系统格式] -f /dev/mapper/设备
#! 查看所有设备文件系统格式,可以用来查看UUID，UUID 与“/dev/设备名”等价。
> blkid

#! 将文件系统挂载到本地文件系统的目录，所谓挂载点其实就是一个空目录
> mount /dev/mapper/设备 /mnt/挂载点名
#! 自动挂载
> vim /etc/fstab
<file sys> <dir>     <type>      <options> <dump> <pass>
UUID=*** /mnt/挂载点 文件系统格式 defaults  0      0
```
> OPTION字段详解
>> auto - 在启动时或键入了 mount -a 命令时自动挂载。
>>  noauto - 只在你的命令下被挂载。
>> exec - 允许执行此分区的二进制文件。
>> noexec - 不允许执行此文件系统上的二进制文件。
>> ro - 以只读模式挂载文件系统。
>> rw - 以读写模式挂载文件系统。
>> user - 允许任意用户挂载此文件系统，若无显示定义，隐含启用 noexec, nosuid, nodev 参数。
>> users - 允许所有 users 组中的用户挂载文件系统.
>> nouser - 只能被 root 挂载。
>> owner - 允许设备所有者挂载.
>> sync - I/O 同步进行。
>> async - I/O 异步进行。
>> dev - 解析文件系统上的块特殊设备。
>> nodev - 不解析文件系统上的块特殊设备。
>> suid - 允许 suid 操作和设定 sgid 位。这一参数通常用于一些特殊任务，使一般用户运行程序时临时提升权限。
>> nosuid - 禁止 suid 操作和设定 sgid 位。
>> noatime - 不更新文件系统上 inode 访问记录，可以提升性能(参见 atime 参数)。
>> nodiratime - 不更新文件系统上的目录 inode 访问记录，可以提升性能(参见 atime 参数)。
>> relatime - 实时更新 inode access 记录。只有在记录中的访问时间早于当前访问才会被更新。（与 noatime 相似，但不会打断如 mutt 或其它程序探测文件在上次访问后是否被修改的进程。），可以提升性能(参见 atime 参数)。
>> flush - vfat 的选项，更频繁的刷新数据，复制对话框或进度条在全部数据都写入后才消失。
>> defaults - 使用文件系统的默认挂载参数，例如 ext4 的默认参数为:rw, suid, dev, exec, auto, nouser, async.

DUMP字段用于设置为1时，表示对文件系统进行备份
PASS字段表示fsck对文件系统的检查顺序，1表示最高权限，2表示其他需要被检查的设备，0表示不需要被检查的设备。

### 挂在情况的查看、分区的使用以及恢复
> fsck用于检查和修复文件系统，`fsck -a`或`fsck -y`为自动修复的命令；`fsck -f`强制检测文件系统分区
```sh
#! 查看硬盘挂载情况
> fdisk -l
#! 查看分区使用情况
> df -lh
#! 统计文件或者目录，占用空间大小
> du -h [文件名或目录名]
#! 为磁盘新建分区
> fdisk /dev/设备名
```

因为，在linux文件系统中所有设备都是以文件的形式进行操作，即一切皆文件；因此在设备接入linux系统使，会出现在/dev目录下，该目录下的


## 关于文件移动的那些事
---
移动文件的速度快不快，不取决于跨不跨分区，而在于出发地和目的地是否是同一文件系统。
同一文件系统之间的移动，一般不需要移动数据本身，只需要改一些元数据即可；而不同的文件系统就好像两个平行世界，讲一个文件系统的文件移动到另一个文件系统的文件，就好像在原来的系统死掉，又携带者原来的记忆在平行世界重生，并在这个世界有了自己的新标识（元数据）。

### 跨或者不跨分区的移动
这种文件的移动方式，本质上还是在同一个文件系统里的移动，所以只需要修改索引节点和目录项节点的指向即可。

### 跨fs的移动
由于文件在跨fs移动，所以就不是修改目录项指向这么简单了，我们需要在目的fs创建一个inode，将文件数据全部移动到新inode后，还要清理源fs的inode，期间伴随着大量的I/O操作，因此花费的时间非常多。

### 有意思的来了，硬链接和软连接
硬链接的实现，是通过索引节点来完成的，每个文件系统下都已自己独立的文件系统编号，每个文件在各自的文件系统下都有唯一的一个数据自己的索引节点编号，因此*硬链接无法实现跨文件系统的访问，也无法创建文件夹链接*，同事硬链接的创建会导致被链接文件inode引用数增加；
相对的，软链接的实现，则是通过记录路径来实现对文件的访问，只要被访问文件的位置没有发生变化，那软链接就会一直有效，因此*可以实现跨文件系统的访问，也可以访问文件夹，但是I/O时间会比硬链接要长*，软链接为一个新inode节点，节点内存储被链接文件的路径，因此不会增加被连接文件inode的引用数。
```sh
#! 硬链接创建
> ln [被链接文件名] [链接名] 
#! 软链接创建
> ln -s [被链接文件名] [链接名]
```

## 巨坑无必

### U盘文件系统与操作系统文件系统不同时会发生什么？
1. 操作系统无法修改硬盘文件的权限，这就会导致即使拥有操作系统的root权限也无法执行一些命令，比如：`ln`、`chxx`系列命令
2. 典型的linux无法修改FAT32和NTFS这两个文件系统下的文件权限；linux原生支持extX系列文件系统。