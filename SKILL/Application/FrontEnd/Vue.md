[[JS]]
[[HTML]]
# `ris:Vuejs`介绍
- 一个前端框架，免除了JS中的DOM操作，简化了书写。
- 基于MVVM(Model-View-ViewModel)，实现数据双向绑定：意思是VIew的变化会引起Model的变化；Model的变化也会影响View的变化
![[Pasted image 20230420105222.png|500]]

# 准备
1. 安装Node.js
2. `npm init vue@latest`该名命令会自动执行create-vue
3. cd到开发目录，`npm install`安装依赖，`npm run dev`运行项目

## 快速入门
1. 在html引入vue.js文件
2. 在html的js区创建Vue对象，定义数据模型
```html
<script src="js/vue.js"></script>

<script>
	new Vue({
//el是一种选择器，表示Vue接管的区域，#表示id选择器
		el:"#app",
		data:{
			message:"Hello Vue!"
		},
		methods:{
			handle:function(){alert("Hi")}
		},
//生命周期方法，该部分代码在创建Vue对象时自动执行
		mounted:{
		//coding...
		}
	})
</script>
```
3. 编写视图
```html
<div id="app">
	<input type="text" v-model="message">
//插值表达式
	{{message}}
</div>
```
# Vue指令

**v-on:event == @event**
```html
v-on:click="handle"
等价于
@click="handle"
```

![[Pasted image 20230420111124.png|550]]

# Vue生命周期

![[Pasted image 20230420150206.png|650]]

![[Pasted image 20230420150131.png|550]]


# Vue项目
[[前端指南#`ris:Vuejs`前端工程化]]


# 一些问题总结


## 异步加载引发的异常

这是两个版本的created生命周期的函数
版本一：
```vue
  created() {
    buildSelect().then(response=>{
      this.classTree = response.data
	  console.log(this.classTree)
    })
  }
```
此时console.log可以正常显示classTree的内容

版本二：
```vue
  created() {
    buildSelect().then(response=>{
      this.classTree = response.data
    })
	console.log(this.classTree)
  }
```
此时console.log无法正常显示classTree的内容(classTree not defined)，这就是异步导致的异常；版本而在未获得响应时不影响console的执行；而版本一则需要在获得响应后才能执行console