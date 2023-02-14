# 类和对象

## 1 类的构成
类声明中的内容包括数据和函数，分别称为数据成员和成员函数。按访问权限划分，数据成员和成员函数又可分为共有、保护和私有3种。

```c++
class 类名{
    public：
        公有数据成员；
        公有成员函数；
    protected:
        保护数据成员；
        保护成员函数；
    private:
        私有数据成员；
        私有成员函数；
};

1.如成绩类

class Score{
    public:
    void setScore(int m, int f);
    void showScore();
    private:
    int mid_exam;
    int fin_exam;
};
```
对一个具体的类来讲，类声明格式中的3个部分并非一定要全有，但至少要有其中的一个部分。一般情况下，一个类的数据成员应该声明为私有成员，成员函数声明为共有成员。这样，内部的数据整个隐蔽在类中，在类的外部根本就无法看到，使数据得到有效的保护，也不会对该类以外的其余部分造成影响，程序之间的相互作用就被降低到最小。
- 类声明中的关键字private、protected、public可以任意顺序出现。
- 若私有部分处于类的第一部分时，关键字private可以省略。这样，如果一个类体中没有一个访问权限关键字，则其中的数据成员和成员函数都默认为私有的。
- 不能在类声明中给数据成员赋初值。


## 2 成员函数的定义
### 2.1 普通成员函数的定义

在类的声明中只给出成员函数的原型，而成员函数的定义写在类的外部。这种成员函数在类外定义的一般形式是：
```c++
返回值类型 类名::成员函数名(参数表){    函数体}

例如，表示分数的类Score可声明如下：

class Score{
public:
	void setScore(int m, int f);
	void showScore();
private:
	int mid_exam;
	int fin_exam;
};

void Score::setScore(int m, int f) 
{
	mid_exam = m;
	fin_exam = f;
}

void Score::showScore()
{
	cout << "期中成绩: " << mid_exam << endl;
	cout << "期末成绩：" << fin_exam << endl;
}
```

### 2.2 内联成员函数的定义

- 隐式声明：将成员函数直接定义在类的内部
```c++
class Score{
public:
	void setScore(int m, int f)
	{
		mid_exam = m;
		fin_exam = f;
	}
	void showScore()
	{
		cout << "期中成绩: " << mid_exam << endl;
		cout << "期末成绩：" << fin_exam << endl;
	}
private:
	int mid_exam;
	int fin_exam;
};
```
- 显式声明：在类声明中只给出成员函数的原型，而将成员函数的定义放在类的外部。
```c++
class Score{
public:
	inline void setScore(int m, int f);
	inline void showScore();
private:
	int mid_exam;
	int fin_exam;
};

inline void Score::setScore(int m, int f) 
{
	mid_exam = m;
	fin_exam = f;
}

inline void Score::showScore()
{
	cout << "期中成绩: " << mid_exam << endl;
	cout << "期末成绩：" << fin_exam << endl;
}
```
说明：在类中，使用inline定义内联函数时，必须将类的声明和内联成员函数的定义都放在同一个文件（或同一个头文件）中，否则编译时无法进行代码置换。

## 3 对象的定义和使用

### 3.1 通常把具有共同属性和行为的事物所构成的集合称为类。
- 类的对象可以看成该类类型的一个实例，定义一个对象和定义一个一般变量相似。
- 对象的定义
- 在声明类的同时，直接定义对象
```c++
class Score{
public:
	void setScore(int m, int f);
	void showScore();
private:
	int mid_exam;
	int fin_exam;
}op1, op2;


声明了类之后，在使用时再定义对象
  Score op1, op2;
```
### 3.2 对象中成员的访问

```c++
对象名.数据成员名
对象名.成员函数名[(参数表)]
op1.setScore(89, 99);
op1.showScore();
```

说明：
在类的内部所有成员之间都可以通过成员函数直接访问，但是类的外部不能访问对象的私有成员。
在定义对象时，若定义的是指向此对象的指针变量，则访问此对象的成员时，不能用“.”操作符，而应该使用“->“操作符。如

```c++
Score op, *sc;
sc = &op;
sc->setScore(99, 100);
op.showScore();
```

### 3.3 类的作用域和类成员的访问属性
- 私有成员只能被类中的成员函数访问，不能在类的外部，通过类的对象进行访问。
- 一般来说，公有成员是类的对外接口，而私有成员是类的内部数据和内部实现，不希望外界访问。将类的成员划分为不同的访问级别有两个好处：一是信息隐蔽，即实现封装，将类的内部数据与内部实现和外部接口分开，这样使该类的外部程序不需要了解类的详细实现；二是数据保护，即将类的重要信息保护起来，以免其他程序进行不恰当的修改。

对象赋值语句
```c++
Score op1, op2;
op1.setScore(99, 100);
op2 = op1;
op2.showScore();
```

## 4 构造函数
### 4.1 构造函数
构造函数是一种特殊的成员函数，它主要用于为对象分配空间，进行初始化。构造函数的名字必须与类名相同，而不能由用户任意命名。它可以有任意类型的参数，但不能具有返回值。它不需要用户来调用，而是在建立对象时自动执行。
```c++
class Score{
public:
	Score(int m, int f);  //构造函数
	void setScore(int m, int f);
	void showScore();
private:
	int mid_exam;
	int fin_exam;
};

Score::Score(int m, int f)
{
	mid_exam = m;
	fin_exam = f;
}

- 在建立对象的同时，采用构造函数给数据成员赋值，通常由以下两种形式

类名 对象名[(实参表)]
Score op1(99, 100);
op1.showScore();


类名 *指针变量名 = new 类名[(实参表)]
Score *p;
p = new Score(99, 100);
p->showScore();
-----------------------
Score *p = new Score(99, 100);
p->showScore();

```
说明：

构造函数的名字必须与类名相同，否则编译程序将把它当做一般的成员函数来处理。
构造函数没有返回值，在定义构造函数时，是不能说明它的类型的。
与普通的成员函数一样，构造函数的函数体可以写在类体内，也可写在类体外。
构造函数一般声明为共有成员，但它不需要也不能像其他成员函数那样被显式地调用，它是在定义对象的同时被自动调用，而且只执行一次。
构造函数可以不带参数。

## 4.2 成员初始化列表

在声明类时，对数据成员的初始化工作一般在构造函数中用赋值语句进行。此外还可以用成员初始化列表实现对数据成员的初始化。
```c++
类名::构造函数名([参数表])[:(成员初始化列表)]
{
    //构造函数体
}

class A{
private:
	int x;
	int& rx;
	const double pi;
public:
	A(int v) : x(v), rx(x), pi(3.14)    //成员初始化列表
	{	}
	void print()
	{
		cout << "x = " << x << " rx = " << rx << " pi = " << pi << endl;
	}
};
```
**说明：**类成员是按照它们在类里被声明的顺序进行初始化的，与它们在成员初始化列表中列出的顺序无关。

## 4.3 带默认参数的构造函数
```c++
#include <iostream>
using namespace std;

class Score{
public:
	Score(int m = 0, int f = 0);    //带默认参数的构造函数
	void setScore(int m, int f);
	void showScore();
private:
	int mid_exam;
	int fin_exam;
};

Score::Score(int m, int f) : mid_exam(m), fin_exam(f)
{
	cout << "构造函数使用中..." << endl;
}

void Score::setScore(int m, int f) 
{
	mid_exam = m;
	fin_exam = f;
}

void Score::showScore()
{
	cout << "期中成绩: " << mid_exam << endl;
	cout << "期末成绩：" << fin_exam << endl;
}

int main() 
{
	Score op1(99, 100);
	Score op2(88);
	Score op3;
	op1.showScore();
	op2.showScore();
	op3.showScore();

	return 0;
}
```
## 5 析构函数
析构函数也是一种特殊的成员函数。它执行与构造函数相反的操作，通常用于撤销对象时的一些清理任务，如释放分配给对象的内存空间等。析构函数有以下一些特点：

- 析构函数与构造函数名字相同，但它前面必须加一个波浪号（~）。
- 析构函数没有参数和返回值，也不能被重载，因此只有一个。
- 当撤销对象时，编译系统会自动调用析构函数。
```c++
class Score{
public:
	Score(int m = 0, int f = 0);
	~Score();       //析构函数
private:
	int mid_exam;
	int fin_exam;
};

Score::Score(int m, int f) : mid_exam(m), fin_exam(f)
{
	cout << "构造函数使用中..." << endl;
}

Score::~Score()
{
	cout << "析构函数使用中..." << endl;
}
```
**说明：**在以下情况中，当对象的生命周期结束时，析构函数会被自动调用：

- 如果定义了一个全局对象，则在程序流程离开其作用域时，调用该全局对象的析构函数。
- 如果一个对象定义在一个函数体内，则当这个函数被调用结束时，该对象应该被释放，析构函数被自动调用。
- 若一个对象是使用new运算符创建的，在使用delete运算符释放它时，delete会自动调用析构函数。

如下示例：
```c++
#include <iostream>
#include <string>

using namespace std;

class Student{
private:
	char *name;
	char *stu_no;
	float score;
public:
	Student(char *name1, char *stu_no1, float score1);
	~Student();
	void modify(float score1);
	void show();
};

Student::Student(char *name1, char *stu_no1, float score1)
{
	name = new char[strlen(name1) + 1];
	strcpy(name, name1);
	stu_no = new char[strlen(stu_no1) + 1];
	strcpy(stu_no, stu_no1);
	score = score1;
}

Student::~Student() 
{
	delete []name;
	delete []stu_no;
}

void Student::modify(float score1) 
{
	score = score1;
}

void Student::show()
{
	cout << "姓名: " << name << endl;
	cout << "学号: " << stu_no << endl;
	cout << "成绩：" << score << endl;
}

int main()
{
	Student stu("雪女", "2020199012", 99);
	stu.modify(100);
	stu.show();

	return 0;
}
```

###  默认的构造函数和析构函数

- 如果没有给类定义构造函数，则编译系统自动生成一个默认的构造函数。
- 说明：对没有定义构造函数的类，其公有数据成员可以用初始值列表进行初始化。
```c++
class A{
public:
	char name[10];
	int no;
};

A a = {"chen", 23};
cout << a.name << a.no << endl;
```
- 只要一个类定义了一个构造函数（不一定是无参构造函数），系统将不再给它提供默认的构造函数。
- 每个类必须有一个析构函数。若没有显示地为一个类定义析构函数，编译系统会自动生成一个默认的析构函数。

## 6 构造函数的重载
```c++
class Score{
public:
	Score(int m, int f);  //构造函数
	Score();
	void setScore(int m, int f);
	void showScore();
private:
	int mid_exam;
	int fin_exam;
};
```
**注意：**在一个类中，当无参数的构造函数和带默认参数的构造函数重载时，有可能产生二义性。

## 7 拷贝构造函数
拷贝构造函数是一种特殊的构造函数，其形参是本类对象的引用。拷贝构造函数的作用是在建立一个新对象时，使用一个已存在的对象去初始化这个新对象。

拷贝构造函数具有以下特点：

- 因为拷贝构造函数也是一种构造函数，所以其函数名与类名相同，并且该函数也没有返回值。
- 拷贝构造函数只有一个参数，并且是同类对象的引用。
- 每个类都必须有一个拷贝构造函数。可以自己定义拷贝构造函数，用于按照需要初始化新对象；如果没有定义类的拷贝构造函数，系统就会自动生成一个默认拷贝构造函数，用于复制出与数据成员值完全相同的新对象。

### 自定义拷贝构造函数
```c++
类名::类名(const 类名 &对象名) 
{
    拷贝构造函数的函数体；
}

class Score{
public:
	Score(int m, int f);  //构造函数
	Score();
	Score(const Score &p);  //拷贝构造函数
	~Score();               //析构函数
	void setScore(int m, int f);
	void showScore();
private:
	int mid_exam;
	int fin_exam;
};

Score::Score(int m, int f)
{
	mid_exam = m;
	fin_exam = f;
}

Score::Score(const Score &p)
{
	mid_exam = p.mid_exam;
	fin_exam = p.fin_exam;
}

调用拷贝构造函数的一般形式为：
    类名 对象2(对象1);
    类名 对象2 = 对象1;
Score sc1(98, 87);
Score sc2(sc1);    //调用拷贝构造函数
Score sc3 = sc2;   //调用拷贝构造函数
```
调用拷贝构造函数的三种情况：

- 当用类的一个对象去初始化该类的另一个对象时；
- 当函数的形参是类的对象，调用函数进行形参和实参结合时；
- 当函数的返回值是对象，函数执行完成返回调用者时。

### 浅拷贝和深拷贝
浅拷贝，就是由默认的拷贝构造函数所实现的数据成员逐一赋值。通常默认的拷贝构造函数是能够胜任此工作的，但若类中含有指针类型的数据，则这种按数据成员逐一赋值的方法会产生错误。

```c++
class Student{
public:
    Student(char *name1, float score1);
    ~Student();
private:
    char *name;
    float score;
};
```

如下语句会产生错误
```c++
Student stu1("白", 89);
Student stu2 = stu1;
```
上述错误是因为stu1和stu2所指的内存空间相同，在析构函数释放stu1所指的内存后，再释放stu2所指的内存会发生错误，因为此内存空间已被释放。解决方法就是重定义拷贝构造函数，为其变量重新生成内存空间。
```c++
Student::Student(const Student& stu)
{
    name = new char[strlen(stu.name) + 1];
    if (name != 0) {
        strcpy(name, stu.name);
        score = stu.score;
    }
}
```