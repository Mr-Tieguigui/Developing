# C++的输入和输出

## 1 C++为何建立自己的输入/输出系统

C++除了完全支持C语言的输入输出系统外，还定义了一套面向对象的输入/输出系统。C++的输入输出系统比C语言更安全、可靠。

c++的输入/输出系统明显地优于C语言的输入/输出系统。首先，它是类型安全的、可以防止格式控制符与输入输出数据的类型不一致的错误。另外，C++可以通过重载运算符“>>”和"<<"，使之能用于用户自定义类型的输入和输出，并且向预定义类型一样有效方便。C++的输入/输出的书写形式也很简单、清晰，这使程序代码具有更好的可读性。


## 2 C++的流库及其基本结构
“流”指的是数据从一个源流到一个目的的抽象，它负责在数据的生产者（源）和数据的消费者（目的）之间建立联系，并管理数据的流动。凡是数据从一个地方传输到另一个地方的操作都是流的操作，从流中提取数据称为输入操作（通常又称提取操作），向流中添加数据称为输出操作（通常又称插入操作）。

C++的输入/输出是以字节流的形式实现的。在输入操作中，字节流从输入设备（如键盘、磁盘、网络连接等）流向内存；在输出操作中，字节流从内存流向输出设备（如显示器、打印机、网络连接等）。字节流可以是ASCII码、二进制形式的数据、图形/图像、音频/视频等信息。文件和字符串也可以看成有序的字节流，分别称为文件流和字符串流。

### 用于输入/输出的头文件
C++编译系统提供了用于输入/输出的I/O类流库。I/O流类库提供了数百种输入/输出功能，I/O流类库中各种类的声明被放在相应的头文件中，用户在程序中用#include命令包含了有关的头文件就相当于在本程序中声明了所需要用到的类。常用的头文件有：

- iostream包含了对输入/输出流进行操作所需的基本信息。使用cin、cout等流对象进行针对标准设备的I/O操作时，须包含此头文件。
- fstream用于用户管理文件的I/O操作。使用文件流对象进行针对磁盘文件的操作，须包含此头文件。
- strstream用于字符串流的I/O操作。使用字符串流对象进行针对内存字符串空间的I/O操作，须包含此头文件。
- iomanip用于输入/输出的格式控制。在使用setw、fixed等大多数操作符进行格式控制时，须包含此头文件。

### 用于输入/输出的流类
I/O流类库中包含了许多用于输入/输出操作的类。其中，类istream支持流输入操作，类ostream支持流输出操作，类iostream同时支持流输入和输出操作。

下表列出了iostream流类库中常用的流类，以及指出了这些流类在哪个头文件中声明。

类名	类名	说明	头文件
抽象流基类	ios	流基类	iostream
输入流类	istream	通用输入流类和其他输入流的基类	iostream
输入流类	ifstream	输入文件流类	fstream
输入流类	istrstream	输入字符串流类	strstream
输出流类	ostream	通用输出流类和其他输出流的基类	iostream
输出流类	ofstream	输出文件流类	fstream
输出流类	ostrstream	输出字符串流类	strstream
输入/输出流类	iostream	通用输入输出流类和其他输入/输出流的基类	iostream
输入/输出流类	fstream	输入/输出文件流类	fstream
输入/输出流类	strstream	输入/输出字符串流类	strstream
~

## 3 预定义的流对象
用流定义的对象称为流对象。与输入设备（如键盘）相关联的流对象称为输入流对象；与输出设备（如屏幕）相联系的流对象称为输出流对象。

C++中包含几个预定义的流对象，它们是标准输入流对象cin、标准输出流对象cout、非缓冲型的标准出错流对象cerr和缓冲型的标准出错流对象clog。


## 4 输入/输出流的成员函数
使用istream和类ostream流对象的一些成员函数，实现字符的输出和输入。
```c++
1、put()函数
    cout.put(单字符/字符形变量/ASCII码);
2、get()函数
    get()函数在读入数据时可包括空白符，而提取运算符“>>”在默认情况下拒绝接收空白字符。
    cin.get(字符型变量)
3、getline()函数
    cin.getline(字符数组, 字符个数n, 终止标志字符)
    cin.getline(字符指针, 字符个数n, 终止标志字符)
4、ignore()函数
    cin.ignore(n, 终止字符)
    ignore()函数的功能是跳过输入流中n个字符（默认个数为1），或在遇到指定的终止字符(默认终止字符是EOF)时提前结束。
```
## 5 预定义类型输入/输出的格式控制

在很多情况下，需要对预定义类型（如int、float、double型等）的数据的输入/输出格式进行控制。在C++中，仍然可以使用C中的printf()和scanf()函数进行格式化。除此之外，C++还提供了两种进行格式控制的方法：一种是使用ios类中有关格式控制的流成员函数进行格式控制；另一种是使用称为操作符的特殊类型的函数进行格式控制。

1、用流成员函数进行输入/输出格式控制

设置状态标志的流成员函数setf()
清除状态标志的流成员函数unsetf()
设置域宽的流成员函数width()
设置实数的精度流成员函数precision()
填充字符的流成员函数fill()
2、使用预定义的操作符进行输入/输出格式控制

3、使用用户自定义的操作符进行输入/输出格式控制

若为输出流定义操作符函数，则定义形式如下：
ostream &操作符名(ostream &stream)
{
    自定义代码
    return stream;
}

若为输入流定义操作符函数，则定义形式如下：
istream &操作符名(istream &stream)
{
    自定义代码
    return stream;
}

例如，
```c++
#include <iostream>
#include <iomanip>
using namespace std;

ostream &output(ostream &stream)
{
	stream.setf(ios::left);
	stream << setw(10) << hex << setfill('-');
	return stream;
}

int main() {
	cout << 123 << endl;
	cout << output << 123 << endl;
	return 0;
}

输出结果如下：

123
7b--------
1
2
```

## 6 文件的输入/输出
所谓文件，一般指存放在外部介质上的数据的集合。

文件流是以外存文件为输入/输出对象的数据流。输出文件流是从内存流向外存文件的数据，输入文件流是从外存流向内存的数据。

根据文件中数据的组织形式，文件可分为两类：文本文件和二进制文件。

在C++中进行文件操作的一般步骤如下：

- 为要进行操作的文件定义一个流对象。
- 建立（或打开）文件。如果文件不存在，则建立该文件。如果磁盘上已存在该文件，则打开它。
- 进行读写操作。在建立（或打开）的文件基础上执行所要求的输入/输出操作。
- 关闭文件。当完成输入/输出操作时，应把已打开的文件关闭。


## 7 文件的打开与关闭
为了执行文件的输入/输出，C++提供了3个文件流类。

类名	说明	功能
istream	输入文件流类	用于文件的输入
ofstream	输出文件流类	用于文件的输出
fstream	输入/输出文件流类	用于文件的输入/输出
这3个文件流类都定义在头文件fstream中。

要执行文件的输入/输出，须完成以下几件工作：

- 在程序中包含头文件fstream。
- 建立流对象
- 使用成员函数open()打开文件。
- 进行读写操作。
- 使用close()函数将打开的文件关闭。


## 8 文本文件的读/写
**例子：**把字符串“I am a student.”写入磁盘文件text.txt中。
```c++
#include <iostream>
#include <fstream>
using namespace std;

int main() {
	ofstream fout("../test.txt", ios::out);
	if (!fout) {
		cout << "Cannot open output file." << endl;
		exit(1);
	}
	fout << "I am a student.";
	fout.close();

	return 0;
}
```
**例子：**把磁盘文件test1.dat中的内容读出并显示在屏幕上。
```c++
#include <iostream>
#include <fstream>
using namespace std;

int main() {
	ifstream fin("../test.txt", ios::in);
	if (!fin) {
		cout << "Cannot open output file." << endl;
		exit(1);
	}
	char str[80];
	fin.getline(str , 80);
	cout << str <<endl;
	fin.close();

	return 0;
}
```
## 9 二进制文件的读写
用get()函数和put()函数读/写二进制文件
**例子：**将a~z的26个英文字母写入文件，而后从该文件中读出并显示出来。
```c++
#include <iostream>
#include <fstream>
using namespace std;

int cput() {
	ofstream outf("test.txt", ios::binary);
	if (!outf) {
		cout << "Cannot open output file.\n";
		exit(1);
	}
	char ch = 'a';
	for (int i = 0; i < 26; i++) {
		outf.put(ch);
		ch++;
	}
	outf.close();
	return 0;
}

int cget() {
	fstream inf("test.txt", ios::binary);
	if (!inf) {
		cout << "Cannot open input file.\n";
		exit(1);
	}
	char ch;
	while (inf.get(ch)) {
		cout << ch;
	}
	inf.close();
	return 0;
}

int main() {
	cput();
	cget();   //此处文件打不开，不知为什么。。。

	return 0;
}
```
用read()函数和write()函数读写二进制文件
有时需要读写一组数据（如一个结构变量的值），为此C++提供了两个函数read()和write()，用来读写一个数据块，这两个函数最常用的调用格式如下：
```c++
inf.read(char *buf, int len);
outf.write(const char *buf, int len);
```
**例子：**将两门课程的课程名和成绩以二进制形式存放在磁盘文件中。
```c++
#include <iostream>
#include <fstream>
using namespace std;

struct list{
	char course[15];
	int score;
};

int main() {
	list ob[2] = {"Computer", 90, "History", 99};
	ofstream out("test.txt", ios::binary);
	if (!out) {
		cout << "Cannot open output file.\n";
		abort();   //退出程序，作用与exit相同。
	}
	for (int i = 0; i < 2; i++) {
		out.write((char*) &ob[i], sizeof(ob[i]));
	}
	out.close();

	return 0;
}
```
**例子：**将上述例子以二进制形式存放在磁盘文件中的数据读入内存。
```c++
#include <iostream>
#include <fstream>
using namespace std;

struct list{
	char course[15];
	int score;
};

int main() {
	list ob[2];
	ifstream in("test.txt", ios::binary);
	if (!in) {
		cout << "Cannot open input file.\n";
		abort();
	}
	for (int i = 0; i < 2; i++) {
		in.read((char *) &ob[i], sizeof(ob[i]));
		cout << ob[i].course << " " << ob[i].score << endl; 
	}
	in.close();

	return 0;
}
```
检测文件结束
在文件结束的地方有一个标志位，即为EOF。采用文件流方式读取文件时，使用成员函数eof()可以检测到这个结束符。如果该函数的返回值非零，表示到达文件尾。返回值为零表示未达到文件尾。该函数的原型是：
```c++
int eof();
函数eof()的用法示例如下：
ifstream ifs;
···
if (!ifs.eof())   //尚未到达文件尾
    ···
还有一个检测方法就是检查该流对象是否为零，为零表示文件结束。
ifstream ifs;
···
if (!ifs)
    ···
如下例子：
while (cin.get(ch))
    cut.put(ch);
这是一个很通用的方法，就是检测文件流对象的某些成员函数的返回值是否为0，为0表示该流（亦即对应的文件）到达了末尾。
```
从键盘上输入字符时，其结束符是Ctrl+Z，也就是说，按下【Ctrl+Z】组合键，eof()函数返回的值为真。