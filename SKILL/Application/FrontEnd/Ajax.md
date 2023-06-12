[[JS]] 
[[XML]]
Asynchronous JavaScript And XML
异步数据交互

作用：
- 数据交换：Ajax向服务器发送请求，并获取服务器响应数据
- 异步交互：在不重置整个页面的情况下，与服务器交换数据并更新部分网页


# 使用方法

## Demo
```html
<script>
	function getData(){
//1. 创建XMLHttpRequest
		var xmlHttpRequest = new XMLHttpRequest();

//2. 发送异步请求
		xmlHttpRequest.open("GET","http://yapi.smart-xwork.cn/mock/169327/emp/list");
		xmlHttpRequest.send();

//3. 获取服务响应数据
		xmlHttpRequest.onreadystatechange=function(){
			if(xmlHttpRequest.readyState==4 && xmlHttpRequest.status==200){
//局部元素更新
document.getElementById("div1").innerHTML=xmlHttpRequest.responseText;
			}
		}
	}
</script>
```
