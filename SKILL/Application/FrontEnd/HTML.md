```toc
```
[HTML文档](https://www.w3schools.com/html/default.asp)

## HTML
用于网页展示
![HTML Struction](https://www.runoob.com/wp-content/uploads/2013/06/02A7DD95-22B4-4FB9-B994-DDB5393F7F03.jpg)
ps: HTML is not a programing language. HTML a sef of markup tag.
start tag(set tags attribution) + content +end tag
[HTML 标签列表（功能排序） | 菜鸟教程 (runoob.com)](https://www.runoob.com/tags/ref-byfunc.html)

盒子模型：
`<div>`
`<span>`
![[Pasted image 20230419134655.png|500]]


### Tags
#### Heading
```html
<h1>title1</h1>
<h2>title2</h2>
```
#### Pragnant
```html
<p>pragnant1</p>
<p>pragnant1</p>
```
#### Link
```html
<a href = "(URL)">link name</a>
```
#### Image
```html
<img decoding="" src="" width="" height=""/>
```
#### **Form**
method可以选择GET或POST，可参考[[HTTP#Request]]
```html
<form action="" method="get">
	<input type="text" name="username">
	<input type="number" name="age">
/*密码框*/
	<input type="password" name="password">
/*单选框*/
	<input type="radio" name="ponder" value="1">
/*复选框*/
	<input type="checkbox" name="hobby" value="game">
/*图像*/
	<input type="file" name="image">
/*时间*/
	<input type="time" name="time">
/*日期*/
	<input type="date" name="date">
/*油箱*/
	<input type="email" name="email">
/*定义下拉列表*/
	<select name="degree">
		<option value="1">大专</option>
		<option value="2">本科</option>
		<option value="3">研究生</option>
	</select>
/*定义文本域*/
	<textarea name="description" cols="30" rows="10"></textarea>

/*按钮*/
	<input type="button" value="...">
	<input type="reset" value="重置">
/*提交方式决定与form的method属性*/
	<input type="submit" value="提交">
</form>
```



### 引入Function——JS
Based on [[JS]]
1. 内部引入：在script标签内，编写js代码
2. 外部引入：js定义于.js文件中，通过html中的script标签的src属性引入


### 引入Style——CSS
Base on [[CSS]]
1. 行内样式：编辑标签style属性
2. 内嵌样式：编写style标签
3. 外联样式：单独写一个.css文件，然后在.html中通过link标签引入.css文件

### DATA
Base on [[XML]]
