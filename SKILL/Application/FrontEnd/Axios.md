[[Ajax]]
[[JS]] 
[[XML]]

# 入门

1. 引入Axios的js文件
```html
<script src="js/axios-0.18.0.js"></script>
```
2. 使用Axios发送请求，并获取响应结果
```html
<script>

new Vue({
	el:"#app",
	data:{
		emps:[]
	},
	mounted(){
//axios.get(url,config).then((result)=>{});
//axios.delete(url,config);
//axios.post(url,data,config)then((result)=>{});
//axios.put(url,data,config);
		axios({
			method:'get',
			url:'http://yapi.smart-xwork.cn/mock/169327/emp/list'
//then表示Statu=200后的回调函数
		}).then((result)=>{
			this.emps = result.data.data;
		});
		axios({
			method:'post',
			url:'http://yapi.smart-xwork.cn/mock/169327/emp/list',
//设置post请求体
			data:"id=1
		}).then((result)=>{
			this.emps = result.data.data;
		});
	}
})
</script>
```




