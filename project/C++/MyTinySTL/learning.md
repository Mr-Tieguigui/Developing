# MyTinySTL

## 六大组件
1.分配器：用来管理内存。
2.迭代器：将容器和算法粘合在一起，用来遍历STL容器中的部分或全部元素。
3.容器：封装了大量常用的数据结构。
4.算法：定义了一些常用算法。
5.仿函数：具有函数特质的对象。
6.适配器：主要用来修改接口。


| 组件                                                         | 文件             |
| :----------------------------------------------------------- | ---------------- |
|分配器|construct.h, allocator.h|
|迭代器|iterator.h, type_traits.h|
|容器|astring.h, basic_string.h, vector.h, list.h, deque.h, stack.h, queue.h, rb_tree.h, set.h, map.h, hashtable.h, unordered_set.h, unordered_map.h|
|算法|uninitialized.h, algorithm.h, algobase.h, algo.h, set_algo.h, heap_algo.h, numeric.h|
|仿函数|functional.h|
|配接器|分布在很多角落|




## [通用工具(move, forward, swap以及 pair等)](./MyTinySTL/util.h)
- `move`: 传临时变量的时候, 可以传T &&, 叫rvalue reference(右值引用), 它能接收rvalue(临时变量), 之后再调用`std::move`就避免copy了.
- `forward`: 能转发下面所有的情况: [const] T &[&]
- `swap`: 交换两个元素的值, 交换两个字符串
- `pair`: pair是将2个数据组合成一组数据; 另一个应用是，当一个函数需要返回2个数据的时候，可以选择pair. 
- - pair的实现是一个结构体，主要的两个成员变量是first second 
- - 因为是使用struct不是class，所以可以直接使用pair的成员变量。
- - 功能：pair将一对值(T1和T2)组合成一个值, 这一对值可以具有不同的数据类型(T1和T2), 两个值可以分别用pair的两个公有函数first和second访问。

## 1. 分配器
```c++
首先对于C++中的delete和new函数进行一些解释：
	在我们使用new来建造一个对象的时候，一般是分为两个步骤的：
	1.调用::operator new()来构建空间；
	2.调用对象的构造函数。
	注：::operator new内部由malloc实现、省略指针转换这步。

	同理，当我们使用delete函数的时候：
	1.调用对象的析构函数
	2.调用::operator delete()释放空间。
	注：::operator delete内部由free实现

在STL的实现中, 为了精细分工, STL allocator决定将上述步骤的两阶段操作分开来, 内存
配置操作由alloc::allocate()负责，内存释放由alloc::deallocate()负责，对象构建
操作由construct负责，对象析构操作由destroy负责。接下来我们梳理内存配置器的具体
实现流程。
```

### [1.1 构造和析构函数](./MyTinySTL/construct.h)

- construct : 负责对象的构造(无参数, 一个参数, 可变模板参数)
- destroy   : 负责对象的析构(一个迭代器: destroy_one, 两个迭代器: destroy_cat)

### [1.2 allocator](./MyTinySTL/allocator.h)

定义了一些类型变量, 实现了allocate()以及deallocate()，仅仅是对::operator new()以及对::operator delete()的简单的封装.


## 2. 迭代器
迭代器提供一种方法使它能够依顺序访问聚合物（容器）所含的各个元素，而又无需暴露改聚合物的内部表述方式。
迭代器可被用来访问一个容器类的所包函的全部元素，其行为像一个指针(对operator *和operator->进行重载).
class与typename的区别:
- typename和class在作为参数类型时用法一样, 没有区别
- typename主要用于对嵌套依赖类型进行提取(萃取). 而class没有这样的功能.
- typename提取的一个例外是在继承或成员初始化列表中对基类进行初始化时不用加typename关键字
### [2.1 iterator](./MyTinySTL/iterator.h)
#### 萃取迭代器所有相关信息
根据移动特性和实施操作被分为5类：
- input iterator(输入迭代器): 迭代器所指的内容不能被修改, 只读且只能执行一次读操作.
- output iterator(输出迭代器): 只写并且一次只能执行一次写操作.
- forward iterator(正向迭代器): 支持读写操作且支持多次读写操作.
- bidirectional iterator(双向迭代器): 支持双向的移动且支持多次读写操作.
- random access iterator(随机访问迭代器): 支持双向移动且支持多次读写操作. p+n, p-n等.

#### has_iterator_cat
- 其中has_iterator_cat判断是否有迭代器类别iterator_category，这里定义了struct two大小是2用来区别char类型大小为1。然后有两个重载的模板参数test，通过传入的模板类型有无typename U::iterator_category来返回two 还是char，最后value通过反映出来。
- 也就是value = sizeof(test<T>(0)) == sizeof(char)中test<T>(0)会去匹配test函数，如果有T中有定义iterator_category类型就返回two 则value就是true，否则返回char则value就是false。

#### iterator_traits_helper 和 iterator_traits_impl
- 而has_iterator_cat返回值传给iterator_traits_helper第二个参数 ，如果为false就没必要继续萃取了，如果为true则继承iterator_traits_impl。
#### is_convertible
- template <class From, class To> struct is_convertible;用来判断From是否可隐式转换为To。
- 所以这边就是判断Iterator::iterator_category算否可以隐式转换为输入迭代器或输出迭代器。

#### 辅助萃取
- 萃取迭代器的类型(iterator_category)
- 萃取迭代器之间距离的类型(distance_type)
- 萃取迭代器指向值的类型(value_type)

#### 判断迭代器具体类型
判断是否为迭代器，以及是哪种类型的迭代器(也能判断是否能隐式转换)

#### 应用：计算距离、移动迭代器
- distance: 计算first迭代器和last迭代器之间的距离，如果是随机访问迭代器就可以像处理指针一样计算距离，否则就需要慢慢遍历，效率差别很大。
- advance: 让迭代器i前进n个距离，如果是随机访问迭代器就可以像处理指针一样移动，否则只能遍历，并且如果是双向迭代器才可以往后遍历，否则只能往前。

#### 反向迭代器
- 反向迭代器中维护了一个正向迭代器，所有的操作都是正向迭代器的一个适配。
- 定义了许多操作符重载

### [2.2 type_traits](./MyTinySTL/type_traits.h)
- typedef m_bool_constant<true>  m_true_type;
- typedef m_bool_constant<false> m_false_type;
- is_pair判断是否是pair类

### [2.3 uninitialized系列函数](./MyTinySTL/uninitialized.h)
初始化空间（大块内存）构造元素:
使用is_trivially_copy_assignable判断出是否有系统定义的构造函数，如果有就没必要调用构造函数了直接copy，否则只能一个一个构造对象。
- uninitialized_copy[/_n]
- uninitialized_fill[/_n]
- uninitialized_move[/_n]

## 3. 容器
### 3.1 序列式容器
#### [3.1.1 vector](./MyTinySTL/vector.h) 
vector的优点:
- 可将容器中元素翻转、复制元素、找到元素值对应的位置
- 迭代器可以按照不同的方式遍历容器
- 可在容器的末尾增加或删除元素
- 可在任意位置插入数据
与数组相比，容器在自动处理容量的大小时会消耗更多的内存，但能很好的调整存储空间大小。

1. 基本操作

```c++
(1) 头文件:
#include<vector>

(2) 创建vector对象:
vector<int> array;

(3) 向量尾部插入/删除元素：
array.push_back(a); //尾部插入数字a
array.pop_back(); //删除向量的最后一个元素

(4) 使用下标访问元素:
array[0],array[1]......array[n]
array.at(i) //使用at(),当这个函数越界时会抛出一个异常

(5) 使用迭代器访问元素:
vector<int>::iterator it;
for(it=array.begin();it!=array.end();it++)
    cout<<*it<<endl;

(6) 插入元素：
array.insert(array.begin()+i,a); //在第i+1个元素前面插入a;

(7) 删除元素：
array.erase(array.begin()+2); //删除第3个元素
array.erase(array.begin()+i,array.end()+j); //删除区间[i,j-1],区间从0开始

(8) 向量大小: array.size();
(9) 清空: array.clear();
(10) 判空：
array.empty(); //当元素个数为0时返回true，否则为false

(11) 返回最后一个元素：array.back();
(12) 返回第一个元素：array.front();
(13) 返回内存中总共可以容纳的元素个数：array.capacity();
(14) 调整元素个数：
a.resize(10); //将a的现有元素个数调至10个，多则删，少则补，其值随机
a.resize(10,2); //将a的现有元素个数调至10个，多则删，少则补，其值为2

(15) 扩充容量：
a.reserve(100); //将a的容量（capacity）扩充至100

(16) 两向量交换：
a.swap(b); //将a中的元素和b中的元素进行整体性交换

(17) 向量的比较：
向量的比较操作 == != >= <= > <  
a==b;
```
重要说明：vector的元素不仅仅可以是int,double,string,还可以是结构体，但是要注意：结构体要定义为全局的，否则会出错。

2. 算法
```c++
注意：进行如下操作需要加头文件
#include<algorithm>
(1) 使用reverse将元素翻转：
reverse(array.begin(),array.end()); //将元素翻转，即逆序排列
注：在vector中，如果一个函数中需要两个迭代器，一般后一个都不包含.

(2) 使用sort排序：
默认升序：sort(array.begin(),array.end());
降序则调用: sort(array.begin(),array.end(),Comp);
bool Comp(const int &a,const int &b)
{
    return a>b;
}

(3) 复制向量的元素：
copy(a.begin(),a.end(),b.begin()+1); 
//把a中的从a.begin()（包括它）到a.end()（不包括它）的元素复制到b中，从b.begin()+1的位置（包括它）开始复制，覆盖掉原有元素

(4) 查找元素的位置：
find(a.begin(),a.end(),10); 
//在a中的从a.begin()（包括它）到a.end()（不包括它）的元素中查找10，若存在返回其在向量中的位置
```
3. 输出vector的中的元素（三种方法）
```c++
vector<float> vecClass; 
int nSize = vecClass.size();   

//方法一（下标方式）打印vecClass 
for(int i=0;i<nSize;i++)    
{    
   cout<<vecClass[i]<<"     ";    
}    
cout<<endl;   
   
//方法二（下标方式）打印vecClass     
for(int i=0;i<nSize;i++)    
{    
   cout<<vecClass.at(i)<<"     ";    
}    
cout<<endl;    
   
//方法三（遍历器方式）打印vecClass：输出某一指定的数值时不方便
for(vector<float>::iterator it = vecClass.begin();it!=vecClass.end();it++)    
{    
    cout<<*it<<"   ";    
}    
cout<<endl;  
```

#### [3.1.2 list](./MyTinySTL/list.h)
c++ 中 list 是 双向链表容器,不支持随机访问, 不过 list 的插入和删除动作很快, list 也是属于RTL标注模板库里面的，所以使用的需要先引入#include <list>

1. list 初始化的方法
```c++
#include <iostream>
#include <string>
using namespace std;
#include <list>
 
int main()
{
    // 创建一个空的list
    list<int> a;
    cout << a.size() << endl;
    // 创建一个10个元素对象
    list<int> b(10);
    // 创建5个元素且5个元素都为明天
    cout << b.size() << endl;
    list<string> c(5, "明天");
    list<string>::iterator it;
    for (it = c.begin(); it != c.end(); it++)
    {
        cout << *it << endl;
    }
 
    return 0;
}
```
2. list方法说明
| 函数                                                         | 说明             |
| :----------------------------------------------------------- | ---------------- |
|assign(first,last) | 用迭代器first和last所在元素替换list元素 |
|assign(num,val) | 用val的num个副本替换list元素 |
|begin | list中第一个元素的引用 |
|back | list中最后一个元素的引用 |
|size | 返回list的个数 |
|front | 获取list中第一个元素 |
|end | 获取list中最后一个元素 |
|empty | 判断list是否为空,为空返回true |
|clear | 清空list元素 |
|pop_back | 删除list中最后一个元素 |
|pop_front | 删除list中第一个元素 |
|rbegin | 返回一个反向迭代器,指向list末尾元素之后 |
|rend | 返回一个反向迭代器,指向list起始元素 |
|erase(i) | 删除第i位置的元素(注意不能直接为数组,需要用begin或者end) |
|erase(start,end) | 删除指定的元素返回,注意是前包含后不包含,里面不能是数字 |
|insert(i,x) | 把 i 插入到x位置 |
|insert(i,x,y) | 把 i 插入到x到y 的位置 |
|swap | 与另一个vector交换数据 |

3. demo 练习
```c++
#include <iostream>
#include <string>
using namespace std;
#include <list>
 
int main()
{
      // 声明一个int 类型list
      list<string> list_name;
      // 获取默认list的size
      cout << list_name.size() << endl;
      //在末尾位置添加元素
      list_name.push_back("赵");
      list_name.push_back("钱");
      list_name.push_back("孙");
      list_name.push_back("李");
      // 获取list的size
      cout << list_name.size() << endl;
      // 开始的位置插入元素
      list_name.insert(list_name.begin(), "百家姓:");
      // 结束的位置插入元素
      list_name.insert(list_name.end(), "ok");
      // 删除第一个元素
      list_name.pop_front();
      // 删除最后一个元素
      list_name.pop_back();
 
      //使用迭代器遍历元素
      list<string>::iterator it;
      for (it = list_name.begin(); it != list_name.end(); it++)
      {
            cout << *it << endl;
      }
      // 获取list第一个元素
      cout << "第一个元素:" << list_name.front() << endl;
      // 获取list最后一个元素
      cout << "最后一个元素:" << list_name.back() << endl;
 
      // list判空
      if (list_name.empty())
      {
            cout << "list为空" << endl;
      }
      else
      {
            cout << "list不为空" << endl;
      }
      // 清空list
      list_name.clear();
      return 0;
}
```

#### [3.1.3 deque](./MyTinySTL/deque.h)
双端队列(deque)是一种随机访问的数据类型,提供了在序列两端快速插入和删除的功能,deque类似于vector,
双端队列(deque)属于STL(Standard Template Library, 标准模板库)所以使用的也是也是需要先引入: #include <deque>

1. 双端队列(deque)的初始化
```c++
#include <iostream>
#include <string>
using namespace std;
#include <deque>
 
int main()
{
    // 创建一个空的双端队列
    deque<int> a;
    cout << a.size() << endl;
    // 创建一个10个元素对象
    deque<int> b(10);
    // 创建5个元素且5个元素都为明天
    cout << b.size() << endl;
    deque<string> c(5, "明天");
    for (int i = 0; i < b.size(); i++)
    {
        cout << c[i] << endl;
    }
    
    
    return 0;
}
```
2. 双端队列(deque)与向量(vector)比较
双端队列(deque)与向量(vector)多了可在两端进行push、pop但是缺点是占用内存多
- 如果你需要高效的随即存取，而不在乎插入和删除的效率，使用vector
- 如果你需要大量的插入和删除，而不关心随机存取，则应使用list
- 如果你需要随机存取，而且关心两端数据的插入和删除，则应使用deque

3. 双端队列(deque)方法说明
| 函数                                                         | 说明             |
| :----------------------------------------------------------- | ---------------- |
| assign(first,last) | 用迭代器first和last所在元素替换双端队列元素 |
| assign(num,val) | 用val的num个副本替换双端队列元素 |
| at(n)	| 返回双端队列中第n个位置元素的值 |
| begin	| 双端队列中第一个元素的引用 |
| back | 双端队列中最后一个元素的引用 |
| size | 返回双端队列的个数 |
| front	| 获取双端队列中第一个元素 |
| end | 获取双端队列中最后一个元素 |
| empty	| 判断双端队列是否为空,为空返回true |
| clear	| 清空双端队列元素 |
| pop_back	| 删除双端队列中最后一个元素 |
| pop_front	| 删除双端队列中第一个元素 |
| rbegin | 返回一个反向迭代器,指向双端队列末尾元素之后 |
| rend | 返回一个反向迭代器,指向双端队列起始元素 |
| erase(i) | 删除第i位置的元素(注意不能直接为数组,需要用begin或者end) |
| erase(start,end) | 删除指定的元素返回,注意是前包含后不包含,里面不能是数字 |
| insert(i,x) | 把 i 插入到x位置 |
| insert(i,x,y)	| 把 i 插入到x到y 的位置 |
| swap | 与另一个vector交换数据 |

4. demo 练习

```c++
#include <iostream>
#include <string>
using namespace std;
#include <deque>
 
int main()
{
      // 声明一个string 类型的deque
      deque<string> ve;
      // 获取默认deque的size
      cout << ve.size() << endl;
      //在末尾位置添加元素
      ve.push_back("赵");
      ve.push_back("钱");
      ve.push_back("孙");
      ve.push_back("李");
      // 获取deque的size
      cout << ve.size() << endl;
      // 开始的位置插入元素
      ve.insert(ve.begin(),"百家姓:");
      // 结束的位置插入元素
      ve.insert(ve.end(),"ok");
      //删除指定的元素返回,注意是前包含后不包含,里面不能是数字,
      // ve.erase(ve.begin(),ve.begin()+2);
      // 删除第二个deque元素
      ve.erase(ve.begin()+1);
      //删除最后一个元素
      ve.pop_back();
      // for遍历deque的元素
      for (int i = 0; i < ve.size(); i++)
      {
        cout << ve[i] << endl;     
      }
      //使用迭代器遍历元素
      for(deque<string>::iterator it=ve.begin();it!=ve.end();it++){
            cout<<*it<<endl;
      }
      // 获取deque第一个元素
      cout << ve.front() << endl;
      // 获取deque最后一个元素
      cout << ve.back() << endl;
      //获取第3个位置的元素
      cout << ve.at(2) << endl;
      // deque判空
      if (ve.empty())
      {
            cout << "ve为空" << endl;
      }
      else
      {
            cout << "ve不为空" << endl;
      }
      // 清空deque
      ve.clear();
      return 0;
}
```

#### [3.1.4 stack](./MyTinySTL/stack.h)
C++ Stack（堆栈） 是一个容器类的改编，为程序员提供了堆栈的全部功能，——也就是说实现了一个`先进后出（FILO）`的数据结构。

C++库以提供“模板”为主。所谓模板，是指不必预先制定类型的函数或类。我们可以借助STL（标准模板库 Standard Template Library, STL）提供的高效算法来管理数据。为应对多种需求，STL为用户提供了多种名为容器（Container）的类，用于管理数据集合。在创建动态数组、表、栈、队列等数据结构时，我们只需要定义对应的容器，然后调用相应成员函数或算法即可。
```c++
stack<int> q;	//以int型为例
int x;
q.push(x);		//将x压入栈顶
q.top();		//返回栈顶的元素
q.pop();		//删除栈顶的元素
q.size();		//返回栈中元素的个数
q.empty();		//检查栈是否为空,若为空返回true,否则返回false
q.emplace();    //将自定义数据类型压入栈顶使用emplace.
```

### 3.2 关联式容器

#### [3.2.1 RB-tree](./MyTinySTL/rb_tree.h)
[红黑树详解](https://blog.csdn.net/m0_56257585/article/details/127333434)
一、红黑树的定义
- 每一个节点都是有颜色的，不是黑色就是红色。
- 根节点root必须是黑色的。
- 所有叶子节点都是黑色的，叶子节点是NULL节点，不存储实际的数据。
- 每个红色节点必须有两个黑色的子节点，或者说是从每个叶子节点到根节点的所有路径上不能有连续的红色节点。
- 从任一节点到其每个叶子上的所有简单路径都包含相同数目的黑色节点。


二、红黑树节点的定义
- 因为每个节点不是红色就是黑色，所以需要定义一个颜色相关的枚举量。
- 还需要操作其父节点，所以定义一个parent指针。
```c++
template<typename _Ty>
class RBTree
{
private:
	// 节点颜色
	enum Color
	{
		BLACK,
		RED
	};

	// 节点定义
	struct Node
	{
		Node(_Ty data = _Ty(), Node* left = nullptr,
			Node* right = nullptr, Node* parent = nullptr,
			Color color = BLACK)
			: val_(data)
			, left_(left)
			, right_(right)
			, parent_(parent)
			, color_(color)
		{}

		_Ty val_;
		Node* left_;
		Node* right_;
		Node* parent_;	// 指向当前节点的父节点
		Color color_;	// 当前节点的颜色
	};
	Node* root_;
};
```


#### [3.2.2 set](./MyTinySTL/set.h)
C++ 中set 类模板又称为集合类模板,它的主要特点就是元素会自动排序切不允许有重复的元素
不允许直接修改元素值,不提供直接存取元素的任何操作函数,set 同样也是STL中的模板, 使用的时候需要先引入#include <set>

1. demo
```c++
#include <iostream>
#include <string>
using namespace std;
#include <set>
 
int main()
{
    //` 创建一个空的set
    set<int> a;
    a.insert(1);
    a.insert(5);
    a.insert(2);
    a.insert(3);
    a.insert(4);
    a.insert(2); // 这个set 无法插入
    cout << a.size() << endl; // 不允许重复,打印结果为 5 
    //使用迭代器遍历元素
    set<int>::iterator it;
    for (it = a.begin(); it != a.end(); it++)
    {
        cout << *it << endl;  // 自动排序,打印结果为12345
    }
}
2. set方法说明

函数	说明
| begin	| set中第一个元素的引用
| end	| set中最后一个元素的引用
| size	| 返回set的个数
| empty	| 判断集合是否为空,为空返回true
| find(x)	| 返回一个指向x的迭代器,如果x不存在,则返回的迭代器等于end
| upper_bound(x)	| 返回一个指向x的迭代器
| lower_bound(x) | 返回一个迭代器指向位于x之前切紧邻x
| clear	| 清空集合元素
| rbegin	| 返回一个反向迭代器,指向向量末尾元素之后
| rend	| 返回一个反向迭代器,指向向量起始元素
| erase(i)	| 删除第i位置的元素(注意不能直接为数组,需要用begin或者end)
| erase(start,end) | 删除指定的元素返回,注意是前包含后不包含,里面不能是数字
| insert(i,x)	| 把 i 插入到x位置
| insert(i,x,y)	| 把 i 插入到x到y 的位置
| swap	| 交换2个集合的内容

3. demo 练习
```c++
#include <iostream>
#include <string>
using namespace std;
#include <set>
 
int main()
{
      // 声明一个set
      set<char> iset;
      // 获取默认set的size
      cout << iset.size() << endl;
      // 插入元素
      iset.insert('A');
      iset.insert('B');
      iset.insert('C');
      iset.insert('D');
      // 获取set的size
      cout << iset.size() << endl;
      //使用迭代器遍历元素
      set<char>::iterator it;
      for (it = iset.begin(); it != iset.end(); it++)
      {
            cout << *it << endl;
      }
      // find查找
      it = iset.find('D');
      if (it == iset.end())
      {
            cout << "未找到" << endl;
      }
      else
      {
            cout << "找到了" << endl;
      }
 
      // set判空
      if (iset.empty())
      {
            cout << "set为空" << endl;
      }
      else
      {
            cout << "set不为空" << endl;
      }
      // 清空set
      iset.clear();
      return 0;
}
```
#### [3.2.3 map](./MyTinySTL/map.h)
C++ 中 map 对象按顺序存储一组值,其中每个元素与一个检索关键字关联, map 的形式 key -- value , 里面的key 是不允许重复的.
map 同样也是STL中的模板使用的时候 需要先引入 #include <map>
```c++
#include <iostream>
#include <string>
using namespace std;
#include <map>
 
int main()
{
    // 创建一个空的map
    map<int, string> a;
    // 插入值使用value_type
    a.insert(map<int, string>::value_type(1, "张三"));
    a.insert(map<int, string>::value_type(2, "李四"));
    a.insert(map<int, string>::value_type(3, "王二"));
    // 插入值使用pair
    a.insert(pair<int, string>(4, "赵括"));
    // 使用数组插入
    a[5] = "张飞";
    a.insert(map<int, string>::value_type(3, "李白")); // 不允许key重复,无法插入
    cout << a.size() << endl; // 不允许key重复,打印结果为 5
    // 遍历map      
    map<int, string>::iterator it;
    for (it = a.begin(); it != a.end(); it++)
    {
        cout << (*it).first << endl;
        cout << (*it).second << endl;
    }
}
2. map 方法说明
函数	说明
| begin	| 返回指向map头部的迭代器 |
|end	| 返回指向map末尾的迭代器 |
|empty	| 判断map是否为空,为空返回true |
|size	| 返回map中元素的个数 |
|at	| 访问元素|
| operator[] |访问元素|
|insert	|插入元素 |
|clear	|清空map|
|swap	|交换两个map|
|find	|查找一个元素|
|earse	|删除一个元素|
|rbegin	|返回反向迭代器以反向开始|
|rend	|将反向迭代器返回到反向结束|
|cbegin	|将常量迭代器返回到开头|
|cend	|返回常量迭代器结束|
|crbegin|	返回const_reverse_迭代器以反转开始|
|equal_range	|返回特殊条目的迭代器对|
|lower_bound	 |将迭代器返回到下限|
|upper_bound |将迭代器返回到上限|
|value_comp()	| 返回比较元素value的函数|
3. demo 练习
```c++
#include <iostream>
#include <string>
using namespace std;
#include <map>
 
int main()
{
      // 声明一个set
      map<int, string> imap;
      // 获取默认set的size
      cout << imap.size() << endl;
      // 插入值使用value_type
      imap.insert(map<int, string>::value_type(1, "张三"));
      imap.insert(map<int, string>::value_type(2, "李四"));
      imap.insert(map<int, string>::value_type(3, "王二"));
      // 插入值使用pair
      imap.insert(pair<int, string>(4, "赵括"));
      // 使用数组插入
      imap[5] = "张飞";
      // 获取map size
      cout << imap.size() << endl;
      // 遍历map
      map<int, string>::iterator it;
      for (it = imap.begin(); it != imap.end(); it++)
      {
            cout << (*it).first << endl;
            cout << (*it).second << endl;
      }
 
      //第二个map的value值
      cout << imap.at(2) << endl;
 
      // map 判空
      if (imap.empty())
      {
            cout << "map为空" << endl;
      }
      else
      {
            cout << "map不为空" << endl;
      }
      // 清空map
      imap.clear();
 
      return 0;
}
```

#### [3.2.4 hashtable](./MyTinySTL/hashtable.h)



## 4. 算法

- algorithm.h — 包含了其他所有的算法头文件
- algobase.h — 最大最小值，比较，内存拷贝，移动等算法
- algo.h — 查找、排序等算法
- numeric.h — 数值算法
- set_algo.h — 集合算法
- heap_algo.h — 堆算法
### [4.1 algorithm.h](./MyTinySTL/algorithm.h)
### [4.2 algobase.h](./MyTinySTL/algobase.h)
算法：max, min, iter_swap, copy(copy_backward, copy_if, copy_n), move, move_backward, equal, fill_n, fill, mismatch
### [4.3 algo.h](./MyTinySTL/algo.h)
算法：all_of, any_of, none_of, count, find, search, search_n, for_each,binary_search, includes, remove, replace, reverse, merge
### [4.4 numeric.h](./MyTinySTL/numeric.h)
算法：accumulate, adjacent_difference, inner_product, iota, partial_sum
### [4.5 set_algo.h](./MyTinySTL/set_algo.h)
set 的四种算法: union, intersection, difference, symmetric_difference
### [4.6 heap_algo.h](./MyTinySTL/heap_algo.h)
heap 的四个算法 : push_heap, pop_heap, sort_heap, make_heap




## [5. 仿函数](./MyTinySTL/functional.h)
所谓仿函数也就是函数对象, 仿函数就是一种具有函数特质的对象.可以将部分操作由用户自己来定义然后传入自定义的函数名就可以被调用。

### 5.1 根据参数个数分类

1. 一元仿函数(unarg_function)
2. 二元仿函数(binary_function)

### 5.2 根据功能分类

1. 算术运算(plus[+], minus[-], multiplies[*], divides[/], modulus[%], negate[-(x)])
2. 关系运算(equal_to[==], not_equal_to[!=], greater[>], less[<], greater_equal[>=], less_equal[<=])
3. 逻辑运算(logical_and[&&], logical_or[||], logical_not[!])
4. 证同函数：不会改变元素, 返回本身
5. 选择函数：接受一个pair, 返回第一个或第二个元素
6. 投射函数：只返回第一个参数或第二个参数

### 5.3 哈希函数对象
- size_t 类型：表示C中任何对象所能达到的最大长度，它是无符号整数
- reinterpret_cast：是C++里的强制类型转换符(它会产生一个新的值，这个值会有与原始参数（expressoin）有完全相同的比特位)
- static_cast：数值类型间的转化(static_cast 运算符完成`相关类型`之间的转换. 而 reinterpret_cast 处理`互不相关的类型`之间的转换)


## 6. 配接器
主要用来修改接口。就像转接口一样, 将一个对class封装变成了另外一个功能的class。

STL 主要提供如下三种配接器：
1. 改变仿函数（functors）接口，称之为 function adapter
2. 改变容器（containers）接口，称之位 container adapter
3. 改变迭代器（iterators）接口者，称之为 iterator adapter
