# 函数模板与类模板
利用模板机制可以显著减少冗余信息，能大幅度地节约程序代码，进一步提高面向对象程序的可重用性和可维护性。模板是实现代码重用机制的一种工具，它可以实现类型参数化，即把类型定义为参数，从而实现代码的重用，使得一段程序可以用于处理多种不同类型的对象，大幅度地提高程序设计的效率。



## 1 模板的概念
在程序设计中往往存在这样的现象：两个或多个函数的函数体完全相同，差别仅在与它们的参数类型不同。

例如：
```c++
int Max(int x, int y) {
    return x >= y ? x : y;
}

double Max(double x, double y) {
    return x >= y ? x : y;
}

能否为上述这些函数只写出一套代码呢？解决这个问题的一种方式是使用宏定义

#define Max(x, y)((x >= y) ? x : y)
```

宏定义带来的另一个问题是，可能在不该替换的地方进行了替换，而造成错误。事实上，由于宏定义会造成不少麻烦，所以在C++中不主张使用宏定义。解决以上问题的另一个方法就是使用模板。

## 2 函数模板
所谓函数模板，实际上是建立一个通用函数，其函数返回类型和形参类型不具体指定，用一个虚拟的类型来代表，这个通用函数就称为函数模板。在调用函数时，系统会根据实参的类型（模板实参）来取代模板中的虚拟类型，从而实现不同函数的功能。

函数的声明格式如下
```c++
template <typename 类型参数>
返回类型 函数名(模板形参表)
{
    函数体
}
也可以定义为如下形式
template <class 类型参数>
返回类型 函数名(模板形参表)
{
    函数体
}
```
实际上，template是一个声明模板的关键字，它表示声明一个模板。类型参数（通常用C++标识符表示，如T、type等）实际上是一个虚拟的类型名，使用前并未指定它是哪一种具体的类型，但使用函数模板时，必须将类型实例化。类型参数前需加关键字typename或class，typename和class的作用相同，都是表示一个虚拟的类型名（即类型参数）。

例1：一个与指针有关的函数模板
```c++
#include <iostream>
using namespace std;

template <typename T>
T Max(T *array, int size = 0) {
	T max = array[0];
	for (int i = 1	; i < size; i++) {
		if (array[i] > max) max = array[i];
	}
	return max;
}

int main() {
	int array_int[] = {783, 78, 234, 34, 90, 1};
	double array_double[] = {99.02, 21.9, 23.90, 12.89, 1.09, 34.9};
	int imax = Max(array_int, 6);
	double dmax = Max(array_double, 6);
	cout << "整型数组的最大值是：" << imax << endl;
	cout << "双精度型数组的最大值是：" << dmax << endl;
	return 0;
}
```
例2：函数模板的重载
```c++
#include <iostream>
using namespace std;

template <class Type>
Type Max(Type x, Type y) {
	return x > y ? x : y;
}

template <class Type>
Type Max(Type x, Type y, Type z) {
	Type t = x > y ? x : y;
	t = t > z ? t : z;
	return t;
}

int main() {
	cout << "33,66中最大值为 " << Max(33, 66) << endl;
	cout << "33,66,44中最大值为 " << Max(33, 66, 44) << endl;
	return 0;
}
```
注意：

- 在函数模板中允许使用多个类型参数。但是，应当注意template定义部分的每个类型参数前必须有关键字typename或class。
- 在template语句与函数模板定义语句之间不允许插入别的语句。
- 同一般函数一样，函数模板也可以重载。
- 函数模板与同名的非模板函数可以重载。在这种情况下，调用的顺序是：首先寻找一个参数完全匹配的非模板函数，如果找到了就调用它；若没有找到，则寻找函数模板，将其实例化，产生一个匹配的模板参数，若找到了，就调用它。


## 3 类模板
所谓类模板，实际上就是建立一个通用类，其数据成员、成员函数的返回类型和形参类型不具体指定，用一个虚拟的类型来代表。使用类模板定义对象时，系统会根据实参的类型来取代类模板中虚拟类型，从而实现不同类的功能。
```c++
template <typename T>
class Three{
private:
    T x, y, z;
public:
    Three(T a, T b, T c) {
        x = a; y = b; z = c;
    }
    T sum() {
        return x + y + z;
    }
}
```
上面的例子中，成员函数（其中含有类型参数）是定义在类体内的。但是，类模板中的成员函数也可以在类模板体外定义。此时，若成员函数中有类型参数存在，则C++有一些特殊的规定：

需要在成员函数定义之前进行模板声明；
`在成员函数名前要加上“类名<类型参数>::”;`
在类模板体外定义的成员函数的一般形式如下：
```c++
template <typename 类型参数>
函数类型 类名<类型参数>::成员函数名(形参表)
{
    ·····
}

例如，上例中成员函数sum()在类外定义时，应该写成

template<typename T>
T Three<T>::sum() {
    return x + y + z;
}

```
**例子：**栈类模板的使用
```c++
#include <iostream>
#include <string>
using namespace std;

const int size = 10;
template <class T>
class Stack{
private:
	T stack[size];
	int top;
public:
	void init() {
		top = 0;
	}
	void push(T t);
	T pop();
};

template <class T>
void Stack<T>::push(T t) {
	if (top == size) {
		cout << "Stack is full!" << endl;
		return;
	}
	stack[top++] = t;
}

template <class T>
T Stack<T>::pop() {
	if (top == 0) {
		cout << "Stack is empty!" <<endl;
		return 0;
	}
	return stack[--top];
}

int main() {
	Stack<string> st;
	st.init();
	st.push("aaa");
	st.push("bbb");
	cout << st.pop() << endl;
	cout << st.pop() << endl;

	return 0;
}
```
