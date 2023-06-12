```toc
```

# JS基础

## 输出语句
```js
//弹出警告框
window.alert("Hello")
//写入HTML，在HTML显示
document.write("Hello")
//写入浏览器控制台
console.log("Hello")
```


## 基本语法

### 变量
```java
var a;//全局作用域，但此时a的类型为undefined，可重复定义
let name = 'simon';//声明并定义一个块作用域变量，不可重复定义
const pi = Math.PI;//声明并定义一个常量，同样为块作用域
```
### 对象
对象以一种键值对集合的形式定义
```js
var obj = {
	name: "Carrot",
	_for: "Max",
	details: {
		color: "orange";
		size : 12
	}
}
var stud = new student(args[]);


Array.length;
Arrary.forEach(function(args[]));
Arrary.push(item);
```
### Function
由arguments对象组成
```js
function add(){
	var sum = 0;
	for(var i in arguments){sum+=i;}
	return sum;
}

funtion add(...args){};//等价
//以上传入add的参数全部加入args数组
```

---
## 基本数据类型

`typeof a`可获取a的数据类型

### 原始数据类型
- Number
- String
```js
String.charAt(num);
String.replace(string1,string2);
String.toUpperCase();
String.length;
"" || NaN || null || undefined || 0 == false;
```
- Boolean
- null
- undefined 

### 引用类型
- Function
- Object
> Function
   Arrary
   Date
   RegExp
- Symbol

### 运算符
```js
var a = 10;

//==运算符不会判断类型；===运算符会进行类型判断；

a == "10"//return true
a === "10" //return false 
a === 10 //reutrn true

```

### 内置函数
```js
pareInt("number",number_base:[10,8,16,2]);
pareFloat();//同上
isNaN(var);//判断var变量是否为NaN
isFinite(var);//判断var是否为正无穷

//内置数字
number = NaN;
number = Infinity;
number = -Infinity;
```


## Using in HTML

- 内部引用
```html
<script>脚本</script>
```
- 外部引用
```html
<script src="脚本.js"></script>
```

# JS对象

## Array 
```js
var a=[]

a.length

//travel 只遍历有值的元素
a.forEach()
a.forEach((e)=>{console.log(e)})

//add in tail
a.push()
//delete elem
a.splice()

```

## String 
```js
var str="hello"
var index=3

a.length

//根据index获取字符
a.charAt(index)

//根据字符获取index
a.indexOf("o")

//去除字符串左右空格
a.trim()

//获取子串，含头不含尾
a.substring(0,3)//hel

```

## JSON
#json 
自定义对象
```js
var student={
	name:"Tom",
	age:18,
	goHome: function(this.name){}
};

var a = new student 
a.age
a.goHome()
```
将自定义对象的所有的key使用`""`括起来就是JSON对象。
```js
//student 对象的json版
var student = '{"name":"Tom","age":18,"goHome": function(this.name){}}';
var c=student

//将c JSON字符串转换为object对象
var jsObject = JSON.parse(c)
//将jsObject对象转换为JSON字符串
var jsonStr = JSON.stringify(jsObject)

```

## BOM
Brower Object Model浏览器对象模型

### Window 
[JS BOM Window](https://www.w3schools.com/Js/js_window.asp)
```js
window.location.href//获取网址，可赋值为其他网址

//定时执行函数
window.setInterval(function(){
	console.log("...")
},2000)

//延迟执行一次
window.setTimeout(function(){
	console.log("delay")
},2000)

```

## DOM
文档对象模型
[JS DOM](https://www.w3schools.com/Js/js_htmldom.asp)
![[Pasted image 20230419161307.png|600]]

```js
//DOM获取元素
var h1 = document.getElementById("h1")

var divs = document.getElementsByTagName("div")
var hobby = document.getElementsByName("hobby")
var cls = document.getElementsByClassName("cls")
```


# JS事件监听

事件：发生于HTML元素上的事件
- 点击事件
- 移动事件
- 按键事件
事件监听：当事件被侦测到时，执行相应代码

## 事件绑定
![[Pasted image 20230419163304.png|600]]

1. HTML标签的事件属性绑定
```html
<intput type="button" onclick="on()" value="button1">
<script>
	function on(){
		alert("click happen")
	}
</script>
```

2. DOM元素属性绑定
```html
<intput type="button" id="btn" value="button2">
<script>
	document.getElementById('btn').onclick=function(){
		alert("click happen")
	}
</script>
```


