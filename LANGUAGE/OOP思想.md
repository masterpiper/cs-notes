# `ris:Ghost`对象的概念


# `ris:Ghost2`对象之间的关系

## 泛化

### java中的体现
```java
public class Shape{}

public Circle extends Shape{}

```

## 依赖

### java中的体现
```
public class Color{}

public Class Circle{
	public Circle(Color color){}
}

```

## 实现

### java中的体现
```java
public interfaces Shape{} 
public Class Circle implements Shape{}

```

## 关联

### java中的体现
```java
public class Color{}
public class Circle{
	private Color color;
}

```

## 聚合

### java中的体现
```java
public class Color{} 
public class Circle{
	private Color[] colors;
}
```

## 组合

### java中的体现
```java
public class Student{}
public class LeaderTeacher{}

public Class ClassRoom{
	private Student[] students;
	private LeaderTeacher leader;
}
```

