---
title: day1 
tags: zzr
notebook: 数据库 
---


# day1

1.总结内容
>生成一个自定义的账号密码文件
* chr
>chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符。
* map
>map() 会根据提供的函数对指定序列做映射。
第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
* shuffle
>shuffle() 方法将序列的所有元素随机排序。
* zip
>zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
* with open
> 
* 函数注解
>
* dty
>
* join
>Python中有join()和os.path.join()两个函数，具体作用如下：
    (1)join()：    连接字符串数组。将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串
    (2)os.path.join()：  将多个路径组合后返回
* string
>
>import random
str_list=list(map(chr,range(97,123)))
     for i in range(200):
         random.shuffle(str_list)
         str_list=list(map(chr,range(97,123)))
         six=str_list[:6]
         print('*'.join(six))

>import random
str_list=list(map(chr,range(97,123)))
s=[str(i)for i in range(10)]
def first_func(s:list,count:int,length:int):
    result=[]
    for i in range(count):
        random.shuffle(s)
        result.append(''.join(s[:length]))
    return result
user_list=first_func(str_list,200,6)
password=first_func(s,200,4)
for i in zip(user_list,password):
    print(i)
    
2.为什么要使用ide？
IDE可以为你把你经常做的繁琐事情提供捷径。并且针对具体的语言或者框架有自己的优化

3.pip和包管理
>在etc目录下新建一个pip.conf文件
vim编辑这个文件 sudo su 到root权限再进行操作
[global]
trusted-host=mirrors.aliyun.com
index-url=http://mirrors.aliyun.com/pypi/simple

4.jupyter安装
>1.安装pip
Install Easy Install
sudo apt-get install python-setuptools python-dev build-essential 
Install pip
sudo easy_install pip 
Install virtualenv
sudo pip install --upgrade virtualenv 
2.安装jupyter
pip install jupyter
python3 -m pip install jupyter
3.运行
jupyter notebook --allow-root