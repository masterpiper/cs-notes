# C Programing
```toc
```
## **存储类别，链接和内存管理以及修饰符**
```c
rand();
srand();
time();
malloc();
calloc();
free();
```
> 对象的定义，在C中一个对象指的是数据所占用的物理内存；而面向对象的语言的中的对象，指的则是数据以及对数据的一系列操作。

C语言根据变量的声明将数据存储在相应的内存区域。*使用storage duration 来描述对象；使用scope 和 linkage 来描述访问对象的描述符。* 作用域和链接说明了程序的那一部分需要使用对象。

### 宏 & typedef
**宏的本质是在预处理阶段进行替换**，在C语言程序文件中的`#include`，在预处理阶段会被替换为相应头文件所包含的内容。

同理，`#define a b`的语义就是将该文件域中的所有a在预处理时替换未b。
```c
#include

#define
#undef
//用于取消define
	#ifdef
	#ifndef
#enddef
//明示常量

#if
#elif
#else

#line
//重置__LINE__和__FILE__
#error
//让预处理器发出一条错误消息
#pragma
```
  ![[Pasted image 20230303003705.png|300]]
**预处理器不做运算，不对表达式求值，只进行替换**
####  宏参数
宏替换本质是生成一次内联代码，每一替换都会多出一段代码；因此同一宏代码在程序中有多个副本；而函数调用则只有一份副本，但每次调用都要跳转PC地址，执行结束还要返回主程序。

与宏函数等效的还有**内联函数**，其作用原理也是将程序中的函数标识替换为函数体的内容，*由于内联函数没有预留代码块，因此内联函数无法获取地址*。
```c
inline static void eatline(...){...};
//因为内联函数的作用域在本文件，所以要用static进行限定。
```

**总结：
宏替换具有更好的时间性能，而函数调用具有更好的空间性能。
用圆括号把宏的参数和整个替换体括起来。这样能确保被括起来的部分 在下面这样的表达式中正确地展开**
##### \#作为一个预处理运算符，可将记号转换成字符串。
```c
#define PSQR(X) printf("The square of X is %d",((X)*(X)));

#define PSQR(X) printf("The square of "#X" is %d",((X)*(X)));
//X作为一个宏形参，#X就是X的字符串形式。
//宏定义中字符串用""来表示，如果字符串中有宏参数
//那么该宏参数的使用要以"#X"的形式写入字符串。
```
##### \#\#运算符可以将两个记号组合为一个记号。
```c
#define XNAME(n) x##n
#define PRINT_XN(n) printf("x"#n"=%d\n",x##n);
PRINT_XN(1) == printf("x1=%d\n",x1);
```
##### 变参宏 __VAR_ARGS__
```c
#include <stdarg.h>
//一般第一个形参设置为int表示本次输入由n个参数
void f1(int n,const char *s,...)
{
	va_list ap;
	va_start(ap,lim);//lim为形参数量,将形参列表拷贝到va_list对象
//传参
	double tic;
	int toc;
	tic = va_arg(ap,double);
	toc = va_arg(ap,int);
//清理
	va_end(ap);
}
//声明带省略号的函数原型
//在定义中声明一个va_list类型变量，存储形参变量

#define PR(...) printf(__VA_ARGS__)
//其中...会由__VA_ARGS__进行代替
```

##### 预定义宏
![[Pasted image 20230303151317.png|400]]


#### typedef
typedef为数据类型定义名称，由*编译器*解释；而宏则由*预处理器*替换
```c
typedef unsigned char BYTE;
BYTE x,y[10],*z;
```
**其中BYTE的作用范围受限于作用域。**

#### 头文件
内容：结构声明、函数原型、typedef、`#define`指令

### namespace
不同作用域的同名变量不会冲突。特定作用域下的struct，union，enum共享相同的namespace。namespace与不同的名称空间的区别在于相同作用域下的结构标记和变量可以和基本数据类型定义的变量同名。
```c
struct rect{double x; double y;};
int rect;
//struct,union,enum与基本数据类型属于不同namespace
//但是要注意C++没有这样的特性
```

### The descriptor's scope and linkage
需求：一个大型的项目可能包含了多个C语言代码文件和头文件，在编译时被看作不同的翻译单元，每个翻译单元的内部都包含了该单元下的全局变量，但是为了实现翻译单元之间全局变量的共享，就需要扩大单元内全局变量的作用范围，这种扩大作用域至不同翻译单元之间的技术叫做**linkage**。
#### Scope
- block scope:  in `{}`, 形参和局部变量
- function scope:`for(int i;i<n;i++){}` 其中i的作用域仅在for循环内
- function prototype scope: 原型中的形参
- file scope: 位于函数定义之外，这样的变量又称全局变量
- thread scope: `_Thread_local`，作用域限定在当前线程
代码文件及其包含的所有头文件构成一个单独的文件，该文件被称为**翻译单元**
```c
/*翻译单元：a.c + a.h + a.c中的head + a.h中的head*/
```
#### linkage
具有块作用域、函数作用域、或函数原型作用域的变量都是无链接变量；这些变量为所在块、函数以及原型所私有。而文件作用域的变量可以是外链接，也可以是内链接。
##### static (for file scope variables) and extern and auto
内部链接：被static描述的文件作用域变量有效范围仅限该翻译单元；被static描述的局部作用域变量有效存储期为
文件中的static：
```c
int        giants  = 5;  //外链接，
static int dodgers = 3;  //内链接，作用域仅在本翻译单元
int main(){}
```
函数中的static：
```c
int c; 
// which is in global scope
extern int d; 
//which in another translate unit.
void functionA(int a ,int b)
{static int c;} 
/** this c is new which different from "int c" and 
*** always store in memory until program finish.
**/

void functionB(int a,int b)
{extern int c;} 
/** this c is "int c". **/

void functionC(int a,int b)
{auto int c;}
/** this c is temporary scope
*** which have same name with "int c", but only live in this function,
*** it will be cleaned when exit this function.
**/
```
extern用于*声明变量*位于外部。在局部变量与全局变量同名时为了区分局部变量可以使用auto声明。

#### Storage class with function
```c
static int functionA(int,int);
// A function statement which avaliable in this file scope.
// other translate unit can not use it.
extern int functionB(int,int);
// A function statement which in another translate unit.
```

#### Memory Management
一个程序内存管理的理想化模型，其中包括了三部分：
- *静态变量*（由编译时确定，生存周期从创建到程序结束）：外部链接、内部链接、无链接。
- *自动变量*（在定义块内有效，程序离开块则销毁），被存入**栈**。
- *动态分配变量*：通过malloc或calloc创建，最后由free释放，被存入**堆**。
```C

#include <stdlib.h>
void*　malloc(uint bytes);
// void* is universal point, you can give it meaning by cast().
void* calloc(uint count,uint every_size);
// create "count" objects, each size=every_size, and set any objects'
// value = 0

//USAGE
double *ptd;
ptd = (double*)malloc(n*sizeof(double))
// the first () is cast void* to double*.
ptd = (double*)calloc(n,sizeof(double))
// allocate a memory and set every elem value is 0.

free(ptd)
//free the object which pointed by ptd.
```

![[Pasted image 20230219130340.png|300]]
malloc、calloc和free要成对使用否则会导致内存块无法被重复使用。

### 类型限定符
#### const, volatile ——限定类型
- const：被const修饰的对象不能被修改，即可被初始化，但不能被赋值。由于被const修饰过的对象不能被轻易改变，所以编译优化时，经常会被加载至高速缓存。
```c
float* const pt;       //pt can change pointed value ,but can't move.
const float* pt;       //pt can move, but can't change pointed.
const float* const pt; //pt can't move and change pointed value.
```
- volatile：与编译优化和cache使用有关，被volatile修饰的对象轻易不会被加载到高速缓存（**因此volatile的读者有用户和编译器以及代理**）
const 和 volatile可以同时修饰一个对象。const以为这在本程序中不可对对象进行修改，而volatile的修饰则允许该对象被本程序之外的力量（这种力量被称为代理）修改，如：`const volatile int* ploc`。

#### restrict ——编译优化
restrict仅能用于指针，表明该指针是访问数据对象的唯一方式且是初始方式。
restrict在作为形参时，意味着编译器可以假定函数体内其他标识符不会修改restrict形参指向的数据。
restrict的读者有编译器和用户。

#### `_Atomic` ——并发程序设计
```c
#include <stdatomic.h>
#include <thread.h>

_Atomic int hogs;      //statement a atomic veriable.
atomic_store(&hogs,12);//set the atomic veriable, and other threads can't
					   //use this veriable.
```



## **Point**
**优先级：() = \[\] > \***

### & and *



#### `const int* a` VS `int* const a`

### **point with array**

#### 一维数组的指针表示和遍历

#### 二维数组的指针表示和遍历

#### 多维数组的指针表示和遍历

### **ponit with function**
指向函数的指针中存储着函数代码的起始地址。
函数名标志，表示该函数的起始地址。
```c
void ToUpper(char *,char *);//声明了一个函数
void ToLower(char *,char *);

void (*pf)(char *,char *);
//声明了一个指向函数的指针
//该指针所指函数返回void，形参为char*

pf = ToUpper;
pf = ToLower;

const void* p;                            //通用指针表示
const double* p_double = (const double*)p //将通用指针解释为double

```

## String

### `char* a` VS `char a[MAXSIZE]`

### Safty String I/O function
```C

#include <stdio.h> //standard I/O
#include <string.h> //string operating
#include <ctype.h> //operating char function

#include <stdlib.h> 
/*
**atoi() atof() atol() strtol() strtul() etc. this header statment a **serise of function 
**which achieve the translation between nnumber and string.
*/


getchar();
putchar();

sprintf();

fgets();
fputs();
```

### command-line argument
```c
int main(int arcg, char* argv[]){
}
// argv[0] -> command name
// argv[1] -> argument1
// each arguments split by <space>

// another equal expresion
int main(int argc, char** argv){
}

```

## File I/O
文件的本质是磁盘或固态硬盘上的一段命名存储区，每个C程序运行之初会打开三个标准文件，即：stdin，stdout，stderror
由于不同系统对换行格式要求不同，所以在文本文件被打开时，源文件中的换行符会被替换为本系统的换行符，写入文件时则要将系统的换行符转换为源文件的换行格式。
但是对于二进制文件来说，不存在这样的替换。

![[Pasted image 20230221013001.png|300]]
```c
/*文件打开方式
**使用w不加x会导致文件打开时被截取，使文件丢失
**文本模式: r,w,a,r+,w+,a+
**二进制模式: rb,wb,ab,ab+,wb+,rb+
**推荐使用x模式打开文件,这样即使打开失败也不会清空文件内容,且x模式打开的文件是进程/线程独占的
**wx,wbx
*/
getc(buf,stdin);
putc(buf,stdout);
//getc和putc 与 getchar和putchar的不同在于可以执行i/o方向
//fscanf vs scanf; fprintf vs printf 同理
//默认情况下i/o方向是标准i/o

while(ch=getc(fd)!=EOF)
{...}
//防止读到空文件
```
当文件被打开时，fd指向的是该文件的FCB。

**stdio.h系列所有输入函数使用相同的缓冲区，所以调用任何一个函数都将从上一次函数停止处开始。**

### 随机访问
```c
int fseek(FILE fp,long offset,base);
// base = SEEK_SET;SEEK_CUR;SEEK_END
long ftell(FILE fp,long offset,base);
```

### 文本模式
程序读取文件的内容会被映射为本地的C模式，读映射过程或许会将`\r 转换为 \n`
写映射过程会将`\n 转换为 \r`。

### 二进制模式
文件内容以二进制形式存储，程序读到的内容与文件的内容是一致的
```c
fread(&base,total_size,copy_size,fd);
fwrite(&base,total_size,copy_size,fd);
rewirte(fd);//重置文件指针至开始
```

## 结构
### struct
```c
//templete statement
struct book{
char title[MAXTITLE];
char author[MAXAUTL];
float value;
}library;
//声明结构的同时，顺便定义了一个library结构变量

//define a struct variable and initialize
struct book library={.value=10.9,.title="c primer"};
```
结构嵌套
```c
struct names{
char first[LEN];
char last[LEN];
char* mid;
};
//使用char* 作为结构属性时，存在潜在程序崩溃问题
//因为char* 没有被初始化，所以可能指向任何地址
//所以要求我们在定义一个结构时，要对其进行初始化。
//在赋值时使用malloc动态赋值，在释放时建议重写一个cleanup函数
//cleanup函数要求释放结构中的所有指针变量。

struct guy{
struct names handle;//嵌套
char job[LEN]
};
```
位字段
```c
struct{
uint code1:2;
uint code2:1;
uint code3:8;
}prcode;
//prcode一共11位
prcode.code1 = 1
prcode.code3 = 102
```
### union
union声明了一个变量的多种解读方式，说占用的内存空间以声明中最大的数据类型为准。即，*每个union只能存储一个值*。
声明：
```c
union hold{
int digit;
double bigfl;
char letter;
};
```
定义：
```c
union hold fit;
fit.digit = 10;
//fit.bigfl = 10.0;
//fit.letter = "1";
//以上赋值均合法
```

### enum
enum变量只能从枚举中取值，**enum本质是int类型的数据**，因此允许enum++的操作，但是被限定了范围，范围就是枚举的模，一般用uint来变量enum中的所有可能。
*一般enum类型配合Switch语句进行使用*。
声明：
```c
enum spectrum{red,orange};
//enum spectrum{red=100,orange=101}
enum spectrum color;
```
定义：
```c
color = red;
```
其中red=0，orange=1。


## 泛型
`_Generic(x,int:val1,float:val2,double:val3,default:val4)`其中x是一个表达式，如果x的类型为int、float、double中的一种，则取冒号后对应的valn。
```c
#define MYTYPE(X) _Generic((X),\
int:0,\
float:1,\
double:2,\
default:3\
)
int x=0;
MYTYPE(x)==0;
//if x is double MYTYPE(x)==2
```

## exit() and atexit()
atexit()的参数是一个指向函数的指针，该函数的作用是将函数注册进exit实行栈
当使用exit()时，会调用实行栈中的函数。
*atexit注册的参数不应带有任何的参数和返回值*，这些函数一般做一些清理任务。

## Make
