#ifndef MYTINYSTL_CONSTRUCT_H_
#define MYTINYSTL_CONSTRUCT_H_

// 这个头文件包含两个函数 construct，destroy
// construct : 负责对象的构造
// destroy   : 负责对象的析构

#include <new>

#include "type_traits.h"
#include "iterator.h"

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable : 4100)  // unused parameter
#endif // _MSC_VER

namespace mystl
{

// construct 构造对象
/*
在全局命名空间中有一个自带的、隐藏的operator new专门用来分配内存。
- 默认情况下编译器会将new这个关键字翻译成这个operator new和相应的构造函数。
- 但在有的情况下，用户自己会在类中重载operator new，这种情况下，编译器默认会使用类中重载的operator new（本质上因为编译器会从命名空间由内而外查找自己想要的函数，选用第一个）。
如果我们想要继续使用默认的operator new，就应该写成::new 字面意思就是调用最外层命名空间中的operator new.
*/

template <class Ty> // 无参数
void construct(Ty* ptr)
{
  ::new ((void*)ptr) Ty(); //void*实际上就是指向一个已经分配好的内存缓冲区的的首地址
}

template <class Ty1, class Ty2> // 一个参数
void construct(Ty1* ptr, const Ty2& value)
{
  ::new ((void*)ptr) Ty1(value);
}

template <class Ty, class... Args> // 可变模板参数
void construct(Ty* ptr, Args&&... args)
{
  ::new ((void*)ptr) Ty(mystl::forward<Args>(args)...);
}

// destroy 将对象析构
/*
True_type: 不重要, 没有参数时
False_type: 重要, 存在参数时
*/


// 传入一个迭代器的情形

template <class Ty>
void destroy_one(Ty*, std::true_type) {}

template <class Ty>
void destroy_one(Ty* pointer, std::false_type)
{
  if (pointer != nullptr)
  {
    pointer->~Ty();
  }
}
// 传入的是两个迭代器来用于析构

template <class ForwardIter>
void destroy_cat(ForwardIter , ForwardIter , std::true_type) {}

template <class ForwardIter>
void destroy_cat(ForwardIter first, ForwardIter last, std::false_type)
{
  for (; first != last; ++first)
    destroy(&*first);
}

/*
  std::is_trivially_denstructible模板用于检查Ty是否是不重要的。
  如果Ty是不重要的，则返回布尔值true；否则返回false。
*/

template <class Ty>
void destroy(Ty* pointer)
{
  destroy_one(pointer, std::is_trivially_destructible<Ty>{});
}

template <class ForwardIter>
void destroy(ForwardIter first, ForwardIter last)
{
  destroy_cat(first, last, std::is_trivially_destructible<
              typename iterator_traits<ForwardIter>::value_type>{});
}

} // namespace mystl

#ifdef _MSC_VER
#pragma warning(pop)
#endif // _MSC_VER

#endif // !MYTINYSTL_CONSTRUCT_H_

