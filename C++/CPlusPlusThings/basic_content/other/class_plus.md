

## 1 自引用指针this
this指针保存当前对象的地址，称为自引用指针。
```c++
void Sample::copy(Sample& xy)
{
    if (this == &xy) return;
    *this = xy;
}
```

##  2 对象数组与对象指针
### 对象数组
```c++
类名 数组名[下标表达式]
用只有一个参数的构造函数给对象数组赋值
Exam ob[4] = {89, 97, 79, 88};
用不带参数和带一个参数的构造函数给对象数组赋值
Exam ob[4] = {89, 90};
用带有多个参数的构造函数给对象数组赋值
Score rec[3] = {Score(33, 99), Score(87, 78), Score(99, 100)};
```
### 对象指针
每一个对象在初始化后都会在内存中占有一定的空间。因此，既可以通过对象名访问对象，也可以通过对象地址来访问对象。对象指针就是用于存放对象地址的变量。声明对象指针的一半语法形式为：类名 *对象指针名
```c++
Score score;
Score *p;
p = &score;
p->成员函数();
```
用对象指针访问对象数组
```c++
Score score[2];
score[0].setScore(90, 99);
score[1].setScore(67, 89);

Score *p;
p = score;   //将对象score的地址赋值给p
p->showScore();
p++;    //对象指针变量加1
p->showScore();

Score *q;
q =&score[1];   //将第二个数组元素的地址赋值给对象指针变量q
```

## 3 string类
C++支持两种类型的字符串，第一种是C语言中介绍过的、包括一个结束符’\0’（即以NULL结束）的字符数组，标准库函数提供了一组对其进行操作的函数，可以完成许多常用的字符串操作。

C++标准库中声明了一种更方便的字符串类型，即字符串类string，类string提供了对字符串进行处理所需要的操作。使用string类必须在程序的开始包括头文件string，即要有以下语句：#include <string>

常用的string类运算符如下：
```c++
=、+、+=、==、!=、<、<=、>、>=、[]（访问下标对应字符）、>>（输入）、<<（输出）

#include <iostream>
#include <string>
using namespace std;

int main()
{
	string str1 = "ABC";
	string str2("dfdf");
	string str3 = str1 + str2;
	cout<< "str1 = " << str1 << "  str2 = " << str2 << "  str3 = " << str3 << endl;
	str2 += str2;
	str3 += "aff";
	cout << "str2 = " << str2 << "  str3 = " << str3 << endl;
	cout << "str1[1] = " << str1[1] << "  str1 == str2 ? " << (str1 == str2) << endl;
	string str = "ABC";
	cout << "str == str1 ? " << (str == str1) << endl;
	return 0;
}
```


## 4 向函数传递对象
- 使用对象作为函数参数：对象可以作为参数传递给函数，其方法与传递其他类型的数据相同。在向函数传递对象时，是通过“传值调用”的方法传递给函数的。因此，函数中对对象的任何修改均不影响调用该函数的对象（实参本身）。
- 使用对象指针作为函数参数：对象指针可以作为函数的参数，使用对象指针作为函数参数可以实现传值调用，即在函数调用时使实参对象和形参对象指针变量指向同一内存地址，在函数调用过程中，形参对象指针所指的对象值的改变也同样影响着实参对象的值。
- 使用对象引用作为函数参数：在实际中，使用对象引用作为函数参数非常普遍，大部分程序员喜欢使用对象引用替代对象指针作为函数参数。因为使用对象引用作为函数参数不但具有用对象指针做函数参数的优点，而且用对象引用作函数参数将更简单、更直接。
```c++
#include <iostream>
using namespace std;

class Point{
public:
	int x;
	int y;
	Point(int x1, int y1) : x(x1), y(y1)  //成员初始化列表
    { }
	int getDistance() 
	{
		return x * x + y * y;
	}
};

void changePoint1(Point point)    //使用对象作为函数参数
{
	point.x += 1;
	point.y -= 1;
}

void changePoint2(Point *poinassst)   //使用对象指针作为函数参数
{
	point->x += 1;
	point->y -= 1;
}

void changePoint3(Point &point)  //使用对象引用作为函数参数
{
	point.x += 1;
	point.y -= 1;
}


int main()
{
	Point point[3] = {Point(1, 1), Point(2, 2), Point(3, 3)};
	Point *p = point;
	changePoint1(*p);
	cout << "the distance is " << p[0].getDistance() << endl;
	p++;
	changePoint2(p);
	cout << "the distance is " << p->getDistance() << endl;
	changePoint3(point[2]);
	cout << "the distance is " << point[2].getDistance() << endl;

	return 0;
}

```

## 5 静态成员
### 静态数据成员

在一个类中，若将一个数据成员说明为static，则这种成员被称为静态数据成员。与一般的数据成员不同，无论建立多少个类的对象，都只有一个静态数据成员的拷贝。从而实现了同一个类的不同对象之间的数据共享。

`定义静态数据成员的格式如下：static 数据类型 数据成员名;`

说明：

- 静态数据成员的定义与普通数据成员相似，但前面要加上static关键字。

- 静态数据成员的初始化与普通数据成员不同。静态数据成员初始化应在类外单独进行，而且应在定义对象之前进行。一般在main()函数之前、类声明之后的特殊地带为它提供定义和初始化。

- 静态数据成员属于类（准确地说，是属于类中对象的集合），而不像普通数据成员那样属于某一对象，因此，可以使用“类名::”访问静态的数据成员。格式如下：类名::静态数据成员名。

- 静态数据成员与静态变量一样，是在编译时创建并初始化。它在该类的任何对象被建立之前就存在。因此，共有的静态数据成员可以在对象定义之前被访问。对象定以后，共有的静态数据成员也可以通过对象进行访问。其访问格式如下
```c++
对象名.静态数据成员名;
对象指针->静态数据成员名;
```


### 静态成员函数

在类定义中，前面有static说明的成员函数称为静态成员函数。静态成员函数属于整个类，是该类所有对象共享的成员函数，而不属于类中的某个对象。静态成员函数的作用不是为了对象之间的沟通，而是为了处理静态数据成员。定义静态成员函数的格式如下：
```c++
static 返回类型 静态成员函数名（参数表）；
```
与静态数据成员类似，调用公有静态成员函数的一般格式有如下几种：
```c++
类名::静态成员函数名(实参表);
对象.静态成员函数名(实参表);
对象指针->静态成员函数名(实参表);
```
一般而言，静态成员函数不访问类中的非静态成员。若确实需要，静态成员函数只能通过对象名（或对象指针、对象引用）访问该对象的非静态成员。

下面对静态成员函数的使用再做几点说明：

- 一般情况下，静态函数成员主要用来访问静态成员函数。当它与静态数据成员一起使用时，达到了对同一个类中对象之间共享数据的目的。
- 私有静态成员函数不能被类外部的函数和对象访问。
- 使用静态成员函数的一个原因是，可以用它在建立任何对象之前调用静态成员函数，以处理静态数据成员，这是普通成员函数不能实现的功能
- 编译系统将静态成员函数限定为内部连接，也就是说，与现行文件相连接的其他文件中的同名函数不会与该函数发生冲突，维护了该函数使用的安全性，这是使用静态成员函数的另一个原因。
- 静态成员函数是类的一部分，而不是对象的一部分。如果要在类外调用公有的静态成员函数，使用如下格式较好：类名::静态成员函数名()
```c++
#include <iostream>
using namespace std;

class Score{
private:
	int mid_exam;
	int fin_exam;
	static int count;     //静态数据成员，用于统计学生人数
	static float sum;     //静态数据成员，用于统计期末累加成绩
	static float ave;     //静态数据成员，用于统计期末平均成绩
public:
	Score(int m, int f);
	~Score();
	static void show_count_sum_ave();   //静态成员函数
};

Score::Score(int m, int f)
{
	mid_exam = m;
	fin_exam = f;
	++count;
	sum += fin_exam;
	ave = sum / count;
}

Score::~Score()
{

}

/*** 静态成员初始化 ***/
int Score::count = 0;
float Score::sum = 0.0;
float Score::ave = 0.0;

void Score::show_count_sum_ave()
{
	cout << "学生人数: " << count << endl;
	cout << "期末累加成绩: " << sum << endl;
	cout << "期末平均成绩: " << ave << endl;
}

int main()
{
	Score sco[3] = {Score(90, 89), Score(78, 99), Score(89, 88)};
	sco[2].show_count_sum_ave();
	Score::show_count_sum_ave();

	return 0;
}
```

## 6 友元
类的主要特点之一是数据隐藏和封装，即类的私有成员（或保护成员）只能在类定义的范围内使用，也就是说私有成员只能通过它的成员函数来访问。但是，有时为了访问类的私有成员而需要在程序中多次调用成员函数，这样会因为频繁调用带来较大的时间和空间开销，从而降低程序的运行效率。为此，C++提供了友元来对私有或保护成员进行访问。友元包括友元函数和友元类。

### 友元函数
友元函数既可以是不属于任何类的非成员函数，也可以是另一个类的成员函数。友元函数不是当前类的成员函数，但它可以访问该类的所有成员，包括私有成员、保护成员和公有成员。

在类中声明友元函数时，需要在其函数名前加上关键字friend。此声明可以放在公有部分，也可以放在保护部分和私有部分。友元函数可以定义在类内部，也可以定义在类外部。

1、将非成员函数声明为友元函数
```c++
#include <iostream>
using namespace std;
class Score{
private:
	int mid_exam;
	int fin_exam;
public:
	Score(int m, int f);
	void showScore();
	friend int getScore(Score &ob);
};

Score::Score(int m, int f)
{
	mid_exam = m;
	fin_exam = f;
}

int getScore(Score &ob)
{
	return (int)(0.3 * ob.mid_exam + 0.7 * ob.fin_exam);
}

int main()
{
	Score score(98, 78);
	cout << "成绩为: " << getScore(score) << endl;

	return 0;
}
```
说明：
- 友元函数虽然可以访问类对象的私有成员，但他毕竟不是成员函数。因此，在类的外部定义友元函数时，不必像成员函数那样，在函数名前加上“类名::”。
- 因为友元函数不是类的成员，所以它不能直接访问对象的数据成员，也不能通过this指针访问对象的数据成员，它必须通过作为入口参数传递进来的对象名（或对象指针、对象引用）来访问该对象的数据成员。
- 友元函数提供了不同类的成员函数之间、类的成员函数与一般函数之间进行数据共享的机制。尤其当一个函数需要访问多个类时，友元函数非常有用，普通的成员函数只能访问其所属的类，但是多个类的友元函数能够访问相关的所有类的数据。
例子：一个函数同时定义为两个类的友元函数
```c++
#include <iostream>
#include <string>
using namespace std;
class Score;    //对Score类的提前引用说明
class Student{
private:
	string name;
	int number;
public:
	Student(string na, int nu) {
		name = na;
		number = nu;
	}
	friend void show(Score &sc, Student &st);
};

class Score{
private:
	int mid_exam;
	int fin_exam;
public:
	Score(int m, int f) {
		mid_exam = m;
		fin_exam = f;
	}
	friend void show(Score &sc, Student &st);
};

void show(Score &sc, Student &st) {
	cout << "姓名：" << st.name << "  学号：" << st.number << endl;
	cout << "期中成绩：" << sc.mid_exam << "  期末成绩：" << sc.fin_exam << endl;
}

int main() {
	Score sc(89, 99);
	Student st("白", 12467);
	show(sc, st);

	return 0;
}
```
2、将成员函数声明为友元函数

一个类的成员函数可以作为另一个类的友元，它是友元函数中的一种，称为友元成员函数。友元成员函数不仅可以访问自己所在类对象中的私有成员和公有成员，还可以访问friend声明语句所在类对象中的所有成员，这样能使两个类相互合作、协调工作，完成某一任务。
```c++
#include <iostream>
#include <string>
using namespace std;

class Score;    //对Score类的提前引用说明
class Student{
private:
	string name;
	int number;
public:
	Student(string na, int nu) {
		name = na;
		number = nu;
	}
	void show(Score &sc);
};

class Score{
private:
	int mid_exam;
	int fin_exam;
public:
	Score(int m, int f) {
		mid_exam = m;
		fin_exam = f;
	}
	friend void Student::show(Score &sc);
};

void Student::show(Score &sc) {
	cout << "姓名：" << name << "  学号：" << number << endl;
	cout << "期中成绩：" << sc.mid_exam << "  期末成绩：" << sc.fin_exam << endl;
}

int main() {
	Score sc(89, 99);
	Student st("白", 12467);
	st.show(sc);

	return 0;
}
```
说明：

一个类的成员函数作为另一个类的友元函数时，必须先定义这个类。并且在声明友元函数时，需要加上成员函数所在类的类名；

### 友元类
可以将一个类声明为另一个类的友元
```c++
class Y{
    ···
};
class X{
    friend Y;    //声明类Y为类X的友元类
};
```
当一个类被说明为另一个类的友元类时，它所有的成员函数都成为另一个类的友元函数，这就意味着作为友元类中的所有成员函数都可以访问另一个类中的所有成员。

友元关系不具有交换性和传递性。


## 7 类的组合
在一个类中内嵌另一个类的对象作为数据成员，称为类的组合。该内嵌对象称为对象成员，又称为子对象。
```c++
class Y{
    ···
};
class X{
    Y y;
    ···
};
```
## 8 共享数据的保护
常类型的引入就是为了既保护数据共享又防止数据被改动。常类型是指使用类型修饰符const说明的类型，常类型的变量或对象成员的值在程序运行期间是不可改变的。

### 常引用

如果在说明引用时用const修饰，则被说明的引用为常引用。常引用所引用的对象不能被更新。如果用常引用做形参，便不会产生对实参的不希望的更改。
```c++
const 类型& 引用名

int a = 5;
const int& b = a;
此时再对b赋值是非法的。
---------------------------
int add(const int& m, const int& n) {
    return m + n;
}
在此函数中对变量m和变量n更新时非法的
```
### 常对象

如果在说明对象时用const修饰，则被说明的对象为常对象。常对象中的数据成员为常量且必须要有初值。
```c++
类名 const 对象名[(参数表)];
const Date date(2021, 5, 31);
```

### 常对象成员

1、常数据成员

类的数据成员可以是常量或常引用，使用const说明的数据成员称为常数据成员。如果在一个类中说明了常数据成员，那么构造函数就只能通过成员初始化列表对该数据成员进行初始化，而任何其他函数都不能对该成员赋值。
```c++
class Date{
private:
	int year;
	int month;
	int day;
public:
	Date(int y, int m, int d) : year(y), month(m), day(d) {

	}
};
```
一旦某对象的常数据成员初始化后，该数据成员的值是不能改变的。

2、常成员函数

类型 函数名(参数表) const;

const是函数类型的一个组成部分，因此在声明函数和定义函数时都要有关键字const。在调用时不必加const。
```c++
class Date{
private:
	int year;
	int month;
	int day;
public:
	Date(int y, int m, int d) : year(y), month(m), day(d){

	}
	void showDate();
	void showDate() const;
};

void Date::showDate() {
	//···
}

void Date::showDate() const {
	//···
}
```
关键字const可以被用于对重载函数进行区分。

说明：

- 常成员函数可以访问常数据成员，也可以访问普通数据成员。
- 常对象只能调用它的常成员对象，而不能调用普通成员函数。常成员函数是常对象唯一的对外接口。
- 常对象函数不能更新对象的数据成员，也不能调用该类的普通成员函数，这就保证了在常成员函数中绝不会更新数据成员的值。
