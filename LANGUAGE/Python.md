


# 问题

## 关于引用和深拷贝
1. `a` 和 `a[:]`的区别
图1 深拷贝版：![[Pasted image 20230526100540.png|600]]
图2 浅拷贝版：![[Pasted image 20230526100621.png|600]]
图二中`result.append(tmp)`是将tmp的引用加入了result，所以tmp的每次变换都会导致result的变化；而图一的`result.append(tmp[:])`则是对tmp的深拷贝，tmp的所有内容被存储到了另一个对象中，所以tmp的改变不会影响到result。



