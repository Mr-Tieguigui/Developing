# 多态性与虚函数
多态性是面向对象程序设计的重要特征之一。多态性机制不仅增加了面向对象软件系统的灵活性，进一步减少了冗余信息，而且显著提高了软件的可重用性和可扩充性。多态性的应用可以使编程显得更简洁便利，它为程序的模块化设计又提供了一种手段。

## 1 多态性概述
所谓多态性就是不同对象收到相同的消息时，产生不同的动作。这样，就可以用同样的接口访问不同功能的函数，从而实现“一个接口，多种方法”。

从实现的角度来讲，多态可以划分为两类：编译时的多态和运行时的多态。在C++中，多态的实现和连编这一概念有关。所谓连编就是把函数名与函数体的程序代码连接在一起的过程。静态连编就是在编译阶段完成的连编。编译时的多态是通过静态连编来实现的。静态连编时，系统用实参与形参进行匹配，对于同名的重载函数便根据参数上的差异进行区分，然后进行连编，从而实现了多态性。运行时的多态是用动态连编实现的。动态连编时运行阶段完成的，即当程序调用到某一函数名时，才去寻找和连接其程序代码，对面向对象程序设计而言，就是当对象接收到某一消息时，才去寻找和连接相应的方法。

一般而言，编译型语言（如C，Pascal）采用静态连编，而解释型语言（如LISP）采用动态连编。静态连编要求在程序编译时就知道调用函数的全部信息。因此，这种连编类型的函数调用速度快、效率高，但缺乏灵活性；而动态连编方式恰好相反，采用这种连编方式，一直要到程序运行时才能确定调用哪个函数，它降低了程序的运行效率，但增强了程序的灵活性。纯粹的面向对象程序语言由于其执行机制是消息传递，所以只能采用动态连编。C++实际上采用了静态连编和动态连编相结合的方式。

在C++中，编译时多态性主要是通过函数重载和运算符重载实现的；运行时多态性主要是通过虚函数来实现的。

## 2 虚函数
虚函数的定义是在基类中进行的，它是在基类中需要定义为虚函数的成员函数的声明中冠以关键字virtual，从而提供一种接口界面。定义虚函数的方法如下：
```c++
virtual 返回类型 函数名(形参表) {
    函数体
}
```
在基类中的某个成员函数被声明为虚函数后，此虚函数就可以在一个或多个派生类中被重新定义。虚函数在派生类中重新定义时，其函数原型，包括返回类型、函数名、参数个数、参数类型的顺序，都必须与基类中的原型完全相同。
```c++
#include <iostream>
#include <string>
using namespace std;

class Family{
private:
	string flower;
public:
	Family(string name = "鲜花"): flower(name) { }
	string getName() {
		return flower;
	}
	virtual void like() {
		cout << "家人喜欢不同的花: " << endl;
	}
};

class Mother: public Family{
public:
	Mother(string name = "月季"): Family(name) { }
	void like() {
		cout << "妈妈喜欢" << getName() << endl;
	}
};

class Daughter: public Family{
public:
	Daughter(string name = "百合"): Family(name) { }
	void like() {
		cout << "女儿喜欢" << getName() << endl;
	}
};

int main() {
	Family *p;
	Family f;
	Mother mom;
	Daughter dau;
	p = &f;
	p->like();
	p = &mom;
	p->like();
	p = &dau;
	p->like();

	return 0;
}

程序运行结果如下：

家人喜欢不同的花:
妈妈喜欢月季
女儿喜欢百合
```
C++规定，如果在派生类中，没有用virtual显式地给出虚函数声明，这时系统就会遵循以下的规则来判断一个成员函数是不是虚函数：该函数与基类的虚函数是否有相同的名称、参数个数以及对应的参数类型、返回类型或者满足赋值兼容的指针、引用型的返回类型。

下面对虚函数的定义做几点说明：

- 由于虚函数使用的基础是赋值兼容规则，而赋值兼容规则成立的前提条件是派生类从其基类公有派生。因此，通过定义虚函数来使用多态性机制时，派生类必须从它的基类公有派生。
- 必须首先在基类中定义虚函数；
- 在派生类对基类中声明的虚函数进行重新定义时，关键字virtual可以写也可以不写。
- 虽然使用对象名和点运算符的方式也可以调用虚函数，如mom.like()可以调用虚函数Mother::like()。但是，这种调用是在编译时进行的静态连编，它没有充分利用虚函数的特性，只有通过基类指针访问虚函数时才能获得运行时的多态性
- 一个虚函数无论被公有继承多少次，它仍然保持其虚函数的特性。
- 虚函数必须是其所在类的成员函数，而不能是友元函数，也不能是静态成员函数，因为虚函数调用要靠特定的对象来决定该激活哪个函数。
- 内联函数不能是虚函数，因为内联函数是不能在运行中动态确定其位置的。即使虚函数在类的内部定义，编译时仍将其看做非内联的。
- 构造函数不能是虚函数，但是析构函数可以是虚函数，而且通常说明为虚函数。


在一个派生类中重新定义基类的虚函数是函数重载的另一种形式。

多继承可以视为多个单继承的组合，因此，多继承情况下的虚函数调用与单继承下的虚函数调用由相似之处。


## 3 虚析构函数
如果在主函数中用new运算符建立一个派生类的无名对象和定义一个基类的对象指针，并将无名对象的地址赋值给这个对象指针，当用delete运算符撤销无名对象时，系统只执行基类的析构函数，而不执行派生类的析构函数。
```c++
Base *p;
p = new Derived;
delete p;
-----------------
输出：调用基类Base的析构函数
```
原因是当撤销指针p所指的派生类的无名对象，而调用析构函数时，采用了静态连编方式，只调用了基类Base的析构函数。

如果希望程序执行动态连编方式，在用delete运算符撤销派生类的无名对象时，先调用派生类的析构函数，再调用基类的析构函数，可以将基类的析构函数声明为虚析构函数。一般格式为
```c++
virtual ~类名(){
    ·····
}
```
虽然派生类的析构函数与基类的析构函数名字不相同，但是如果将基类的析构函数定义为虚函数，由该类所派生的所有派生类的析构函数也都自动成为虚函数。示例如下，
```c++
#include <iostream>
#include <string>
using namespace std;

class Base{
public:
	virtual ~Base() {
		cout << "调用基类Base的析构函数..." << endl;
	}
};

class Derived: public Base{
public:
	~Derived() {
		cout << "调用派生类Derived的析构函数..." << endl;
	}
};

int main() {
	Base *p;
	p = new Derived;
	delete p;
	return 0;
}

输出如下：

调用派生类Derived的析构函数...
调用基类Base的析构函数...
```

## 4 纯虚函数
纯虚函数是在声明虚函数时被“初始化为0的函数”，声明纯虚函数的一般形式如下：

virtual 函数类型 函数名(参数表) = 0;

声明为纯虚函数后，基类中就不再给出程序的实现部分。纯虚函数的作用是在基类中为其派生类保留一个函数的名字，以便派生类根据需要重新定义。



## 5 抽象类
如果一个类至少有一个纯虚函数，那么就称该类为抽象类，对于抽象类的使用有以下几点规定：

- 由于抽象类中至少包含一个没有定义功能的纯虚函数。因此，抽象类只能作为其他类的基类来使用，不能建立抽象类对象。
- 不允许从具体类派生出抽象类。所谓具体类，就是不包含纯虚函数的普通类。
- 抽象类不能用作函数的参数类型、函数的返回类型或是显式转换的类型。
- 可以声明指向抽象类的指针或引用，此指针可以指向它的派生类，进而实现多态性。
- 如果派生类中没有定义纯虚函数的实现，而派生类中只是继承基类的纯虚函数，则这个派生类仍然是一个抽象类。如果派生类中给出了基类纯虚函数的实现，则该派生类就不再是抽象类了，它是一个可以建立对象的具体类了。
~

## 6 示例：利用多态计算面积
应用C++的多态性，计算三角形、矩形和圆的面积。
```c++
#include <iostream>
using namespace std;

/*** 定义一个公共基类 ***/
class Figure{
protected:
	double x, y;
public:
	Figure(double a, double b): x(a), y(b) {  }
	virtual void getArea()      //虚函数
	{  
		cout << "No area computation defind for this class.\n";
	}
};
class Triangle: public Figure{
public:
	Triangle(double a, double b): Figure(a, b){  }
	//虚函数重定义，用于求三角形的面积
	void getArea(){
		cout << "Triangle with height " << x << " and base " << y;
		cout << " has an area of " << x * y * 0.5 << endl;
	}
};

class Square: public Figure{
public:
	Square(double a, double b): Figure(a, b){  }
	//虚函数重定义，用于求矩形的面积
	void getArea(){
		cout << "Square with dimension " << x << " and " << y;
		cout << " has an area of " << x * y << endl;
	}
};

class Circle: public Figure{
public:
	Circle(double a): Figure(a, a){  }
	//虚函数重定义，用于求圆的面积
	void getArea(){
		cout << "Circle with radius " << x ;
		cout << " has an area of " << x * x * 3.14 << endl;
	}
};

int main(){
	Figure *p;
	Triangle t(10.0, 6.0);
	Square s(10.0, 6.0);
	Circle c(10.0);

	p = &t;
	p->getArea();
	p = &s;
	p->getArea();
	p = &c;
	p->getArea();

	return 0;
}
程序输出如下：

Triangle with height 10 and base 6 has an area of 30
Square with dimension 10 and 6 has an area of 60
Circle with radius 10 has an area of 314
```