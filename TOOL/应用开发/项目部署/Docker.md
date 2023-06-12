![docker architecture|400](https://docs.microsoft.com/en-us/virtualization/windowscontainers/deploy-containers/media/docker-on-linux.png)
Docker区别于虚拟机，**Docker的本质是文件系统级别的虚拟**，即在相同的宿主OS下有基于不同OS的文件系统，这种文件系统时独立于宿主的文件系统，但拥有相同的内核。
而虚拟机，则是操作系统级别的虚拟，因此更为臃肿。

[Docker — 从入门到实践 | Docker 从入门到实践 (docker-practice.com)](https://vuepress.mirror.docker-practice.com/)
```toc
```

## Basic concept
### Image & Union FS
Docker Image is a special document system which include lib, source, config etc.(Image mains os's rootfs and lib.)
USing Union FS, we stratified application's runing environment as Readonly layer, Init layer, wr layer.
(下载加速：`vim /etc/docker/daemon.json`,为`"registry-mirrors"`添加`"https://hub-mirror.c.163.com","https://mirror.baidubce.com"`,然后`sudo systemctl daemon-reload`;`sudo systemctl restart docker`)
#### Usage
```bash
# create an Image
docker pull [docker_registry_address:sort/]repository_name[:tag]

# example
docker pull ubuntu:18.04
# docker pull docker.io/library/ubuntu:18.04


# run an Image
docker run -it --rm ubuntu:18.04 bash
# -i 交互；-t 终端；--rm 退出后删除
docker run --name container_name -d -p 80:80 image_name
# -d 后台运行container；-p 指定端口映射
exit #退出
```
#### Image management
```
# list image
$ docker image ls -a
$ docker image ls --digests
$ docker imge ls image_name

# list image,container,volumes,cache
$ docker system df

# delete image
$ docker image prune
$ docker image rm imge_id
$ docker image rm <rep_name>:<tag>

# show change
$ docker diff container_name

# commit change 尽量少用，每用一次都会使image变臃肿
$ docker commit [option] container_name rep_name:tag
```

### Container & Volume
the nature of Container is a master progress, a runing Image. Every container'ns is different with host, they have their own ns. 
每个容器都以自己的Image为基地，向上构建一层容器存储层，容器生存周期产生的数据会虽自身的消亡而丢失，**因此在实践的过程中，容器不应该向存储层写任何数据，而应该向Volume或者绑定宿主目录写入数据。**

Volume is independent with container, which using to store data when container runing product.

### Repository & Docker Registry
To use Image in Server, wei need to centralized storage and distribute Image. So Docker Registry provide a service satisfied our demand.

A Docker Registry(注册表) have many Repository, Every Repository have many tags which of them correspond a Image.
We specify a specific tag by `<repository_name>:<tag>`.
Repsoitory_name:`username/software_name`
[Docker官方镜像](https://hub.docker.com/)
[Docker Registry API](https://docs.docker.com/registry/spec/api/)




### Dockerfile 
```dockerfile
# docker镜像的定制脚本

# FROM scratch 加载空白镜像
FROM [image_name]

# 不要每条指令都用RUN，因为每次RUN都会生成一个layer
# 推荐！！！将指令用&&连接起来执行一次RUN
RUN <command>\
	&& <command>\
	&& ... \
	&& <command>
	&& apt-get purge -y --auto-remove $buildDeps
# 最后一步清理不必要的文件，从而使得创建的Docker更轻便
```
#### Image build
`docker build [option] <contextdir>`这里上下文路径使用的是相对路径，docker build基于C/S架构，`COPY & ADD` 经本地
```dockerfile
COPY contextdir rootfsdir
```

## Work flow



