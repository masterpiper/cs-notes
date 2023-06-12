```toc
```

## XML
用于传输和存储数据与HTML配合使用
![xml实例结构](https://www.runoob.com/wp-content/uploads/2013/09/nodetree.gif)
EXAMPLE:
```xml
<?xml version="1.0" encoding="utf-8">
<note>
	<to>Tove</to>
	<from>Jani</from>
	<heading>Reminder</heading>
	<body>Don't forget</body>
</note>
```
- 第一行xml声明，定义编码和版本号
- `<note></note>` 为信息体标签，内容为信息体
- `<to></to>` 目的标签，内容为目的地名称
- `<from></from>` 源标签，内容为源名称

### 实体引用
在xml内容和值中直接使用”<,&,',",>,“是非法的。

| xml引用 | 替代符号 | 符号语义 |
| --- | --- | ---|
| \&lt; | < | less than |
| \&amp; | & | ampersand |
| \&gt; | > | greater than |
| \&apos; | ' | apostrophe |
| \&quot; | " | quotation mark |

### 显示方法
- CSS：添加标签`<?xml-stylesheet type="text/css" href="css_name.css"?>`
- XSLT(recommend): 显示以前将xml转为html

### XMLHttpRequest
Exchange data with Server in background.
```js
/ create a xmlhttprequest object
xmlhttp = new XMLHttpRequest();
```
## JAVA项目是如何使用xml的
既然xml是一种有规范格式的数据载体，那么在java程序使用到xml中的数据的时候就需要xml的解析器来提取xml所存储的数据。所以本节主要介绍几种xml文件解析器，最后将给出一个表格，解答各种解析器的使用条件。

### DOM vs SAX vs JDOjM vs DOM4J
**DOM**
DOM define a serise of standard mothed to access and operate doc.
XML and HTML regarded as a tags' tree in DOM.

DOM的工作原理是将xml文件解析成包含内容的树，对树进行遍历获取内容，是一种基于树形结构的访问方式；有点在于修改树种的内容方便，但是占用了较大的内存空间。所以*通常用于需要xml文档需要频繁变动的服务中*。

**SAX**
SAX则采用的是事件模型，每次发起一个解析xml请求时会触发一系列事件，当发现给定tag时，会激活回调，告诉方法指定的tag已找到；*SAX对内存要求比较低，但是要求程序员自己决定要处理的tag，所以在处理同一文档中的多处数据时由于不支持文档层次定位，不支持XPATH，所以开发过程会非常繁琐*。
> tips: 所谓事件模型，指的是通过监听函数对发生的事件作出反应，是事件驱动编程模式的主要方式，在html中每个标签下都定义了各自事件的监听器，子标签的事件会冒泡传递给父标签，这些事件可以绑定响应的js函数，一旦事件发生就会执行响应的js函数。可参考：[事件 - 事件模型 - 《阮一峰 JavaScript 教程》 - 书栈网 · BookStack](https://www.bookstack.cn/read/javascript-tutorial/docs-events-model.md)

### XPATH 导航

[XPath 教程 | 菜鸟教程 (runoob.com)](https://www.runoob.com/xpath/xpath-tutorial.html)
XML文件被描述成树的结构，XPATH表达式就是在XML文档树中遍历节点的路径表示。
XPATH包含一个标准库，式XSLT主要元素，是W3C的一个标准
(PS:XSLT将xml文档转换为其他格式的文档，如：html)

#### xpath node
- element node:
- attribute node:
- text node:
- namespace node:
- deal instruct node:
- doc root node:
- annotation node: 

#### XPATH Expression grammar
**Grammar**

| grammar elem | describe |
| --- | --- |
| nodename | select all of node which parents is nodename.|
| \/ | select start at root |
| \/\/ | select doc's node start at present node |
| . | select present node |
| .. | select parents of present node |
| @ | select node's attribution |
**Predicates**

| predicates               | result                                  |
| ------------------------ | --------------------------------------- |
| nodename[k]              | select kth node which name is node name |
| nodename[last()-k]       | select k+1 from the bottom node         |
| nodename[position()<k]   | select frist k-1 node                   |
| nodename[@attr='value']  | select all of attr='value' is node      |
| nodename[elem>k]         | select all of elem>k is node            |
| \*                       | select any node                         |
| @\*                      | select any node with attribution        |
| node/elem1 \| node/elem2 | select node with elem1 and elem2        |

### 总结

|          | DOM | DOM4J | SAX | JDOM |
| -------- | --- | ----- | --- | ---- |
| 优点     |     |       |     |      |
| 缺点     |     |       |     |      |
| 适用条件 |     |       |     |      | 

