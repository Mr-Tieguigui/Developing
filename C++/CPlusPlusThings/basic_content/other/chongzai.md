# 函数重载那些事

在C++中，用户可以重载函数。这意味着，在同一作用域内，只要函数参数的类型不同，或者参数的个数不同，或者二者兼而有之，两个或者两个以上的函数可以使用相同的函数名。


```c++

#include <iostream>
using namespace std;

int add(int x, int y)
{
	return x + y;
}

double add(double x, double y)
{
	return x + y;
}

int add(int x, int y, int z)
{
	return x + y + z;
}

int main() 
{
	int a = 3, b = 5, c = 7;
	double x = 10.334, y = 8.9003;
	cout << add(a, b) << endl;
	cout << add(x, y) << endl;
	cout << add(a, b, c) << endl;
	return 0;
}

```

说明：

调用重载函数时，函数返回值类型不在参数匹配检查之列。因此，若两个函数的参数个数和类型都相同，而只有返回值类型不同，则不允许重载。

```c++
int mul(int x, int y);
double mul(int x, int y);
```
函数的重载与带默认值的函数一起使用时，有可能引起二义性。
```c++
void Drawcircle(int r = 0, int x = 0, int y = 0);
void Drawcircle(int r);
Drawcircle(20);
```
在调用函数时，如果给出的实参和形参类型不相符，C++的编译器会自动地做类型转换工作。如果转换成功，则程序继续执行，在这种情况下，有可能产生不可识别的错误。
```c++
void f_a(int x);
void f_a(long x);
f_a(20.83);
```