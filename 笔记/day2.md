---
title:  day2
tags: zzr
notebook: 数据库
---

# day2


## python
1. pickle
>(1) pickle提供了一个简单的持久化功能。可以将对象以文件的形式存放在磁盘上。
(2)pickle模块只能在Python中使用，python中几乎所有的数据类型（列表，字典，集合，类等）都可以用pickle来序列化，pickle序列化后的数据，可读性差，人一般无法识别。

* 列表内容存储在文件中 
a=[i for i in range(10)]
import pickle#标准库中的包 腌制
data=open('list1.pkl','wb')#二进制文件写入
pickle.dump(a,data)
data.close()
* 将文件中的内容解析出来
import pickle
data=open('list1.pkl','rb')
a=pickle.load('data')
 ----------------------------------------

>pickle.dump(obj, file[, protocol])
序列化对象，并将结果数据流写入到文件对象中。参数protocol是序列化模式，默认值为0，表示以文本的形式序列化。protocol的值还可以是1或2，表示以二进制的形式序列化。

-----------------------------------------
>pickle.load(file)
反序列化对象。将文件中的数据解析为一个Python对象。
2. json
>JSON(JavaScript Object Notation, JS 对象简谱) 是一种轻量级的数据交换格式。它基于 ECMAScript (欧洲计算机协会制定的js规范)的一个子集，采用完全独立于编程语言的文本格式来存储和表示数据。简洁和清晰的层次结构使得 JSON 成为理想的数据交换语言。 易于人阅读和编写，同时也易于机器解析和生成，并有效地提升网络传输效率。
在 JS 语言中，一切都是对象。因此，任何支持的类型都可以通过 JSON 来表示，例如字符串、数字、对象、数组等。但是对象和数组是比较特殊且常用的两种类型：

    对象表示为键值对
    数据由逗号分隔
    花括号保存对象
    方括号保存数组


## linux
1. netstat
用来打印linux中网络系统的状态信息可让你得知整个linux系统的网络状况
* -a或--all:显示所有连线中的socket
* -n或--numeric：直接使用ip地址，而不通过域名服务器
* -t或--tcp:显示TCP传输协议的连线状况
>netstat -nat | grep 3306监听查看3306MySQL的端口号，连接状态端口号中最大的是65535
2. lsof
是一个列出当前系统打开文件的工具
lsof -i//显示所有打开的端口
sudo lsof -i:8888查看端口号是哪个应用的jupyter
>lsof -i:8888
3. 重启服务和查看服务状态
>重启：systemctl restart mysql
service mysql restart
查看服务状态：systemctl status mysql |start|stop|restart
>service mysql status |start|stop|restart
4. man
>man命令是Linux下的帮助指令，通过man指令可以查看Linux中的指令帮助、配置文件帮助和编程帮助等信息。man ls查看命令帮助
5. 注释已有的配置，重新写配置
在修改配置时，不要把原来的配置给删除，先注释，再进行新配置的添加
    * 修改bindaddress配置
            bindaddress 127.0.0.1 修改为 # 12.0.0.1本地回环
            bindaddress 0.0.0.1
    * 修改post端口号 mysql
            port 3306
            port 55555
            0-1024 端口属于linux的端口，不能修改 占用
            端口号最大值为: 65535

6.ssh

    apt install openssh-server
    远程登录：ssh 用户名@IP地址

## 数据库
1. DB
>数据库(Database)是按照数据结构来组织、存储和管理数据的建立在计算机存储设备上的仓库。
简单来说是本身可视为电子化的文件柜——存储电子文件的处所，用户可以对文件中的数据进行新增、截取、更新、删除等操作。
在经济管理的日常工作中，常常需要把某些相关的数据放进这样的“仓库”，并根据管理的需要进行相应的处理。
2. DBMS

>数据库管理系统(Database Management System)是一种操纵和管理数据库的大型软件，用于建立、使用和维护数据库，简称DBMS。它对数据库进行统一的管理和控制，以保证数据库的安全性和完整性。用户通过DBMS访问数据库中的数据，数据库管理员也通过dbms进行数据库的维护工作。它可使多个应用程序和用户用不同的方法在同时或不同时刻去建立，修改和询问数据库。大部分DBMS提供数据定义语言DDL（Data Definition Language）和数据操作语言DML（Data Manipulation Language），供用户定义数据库的模式结构与权限约束，实现对数据的追加、删除等操作。

>数据库管理系统是数据库系统的核心，是管理数据库的软件。数据库管理系统就是实现把用户意义下抽象的逻辑数据处理，转换成为计算机中具体的物理数据处理的软件。有了数据库管理系统，用户就可以在抽象意义下处理数据，而不必顾及这些数据在计算机中的布局和物理位置。

>1.数据定义：DBMS提供数据定义语言DDL（Data Definition Language），供用户定义数据库的三级模式结构、两级映像以及完整性约束和保密限制等约束。DDL主要用于建立、修改数据库的库结构。DDL所描述的库结构仅仅给出了数据库的框架，数据库的框架信息被存放在数据字典（Data Dictionary）中。
2.数据操作：DBMS提供数据操作语言DML（Data Manipulation Language），供用户实现对数据的追加、删除、更新、查询等操作。
3.数据库的运行管理：数据库的运行管理功能是DBMS的运行控制、管理功能，包括多用户环境下的并发控制、安全性检查和存取限制控制、完整性检查和执行、运行日志的组织管理、事务的管理和自动恢复，即保证事务的原子性。这些功能保证了数据库系统的正常运行。
4.数据组织、存储与管理：DBMS要分类组织、存储和管理各种数据，包括数据字典、用户数据、存取路径等，需确定以何种文件结构和存取方式在存储级上组织这些数据，如何实现数据之间的联系。数据组织和存储的基本目标是提高存储空间利用率，选择合适的存取方法提高存取效率。
5.数据库的保护：数据库中的数据是信息社会的战略资源，所以数据的保护至关重要。DBMS对数据库的保护通过4个方面来实现：数据库的恢复、数据库的并发控制、数据库的完整性控制、数据库安全性控制。DBMS的其他保护功能还有系统缓冲区的管理以及数据存储的某些自适应调节机制等。
6.数据库的维护：这一部分包括数据库的数据载入、转换、转储、数据库的重组合重构以及性能监控等功能，这些功能分别由各个使用程序来完成。
7.通信：DBMS具有与操作系统的联机处理、分时系统及远程作业输入的相关接口，负责处理数据的传送。对网络环境下的数据库系统，还应该包括DBMS与网络中其他软件系统的通信功能以及数据库之间的互操作功能。
3. SQL
>结构化查询语言(Structured Query Language)简称SQL(发音：/ˈes kjuː ˈel/ "S-Q-L")，是一种特殊目的的编程语言，是一种数据库查询和程序设计语言，用于存取数据以及查询、更新和管理关系数据库系统；同时也是数据库脚本文件的扩展名。
4. MySQL
>MySQL是一个关系型数据库管理系统，由瑞典MySQL AB 公司开发，目前属于 Oracle 旗下产品。MySQL 是最流行的关系型数据库管理系统之一，在 WEB 应用方面，MySQL是最好的 RDBMS (Relational Database Management System，关系数据库管理系统) 应用软件。
MySQL是一种关系数据库管理系统，关系数据库将数据保存在不同的表中，而不是将所有数据放在一个大仓库内，这样就增加了速度并提高了灵活性。
MySQL所使用的 SQL 语言是用于访问数据库的最常用标准化语言。MySQL 软件采用了双授权政策，分为社区版和商业版，由于其体积小、速度快、总体拥有成本低，尤其是开放源码这一特点，一般中小型网站的开发都选择 MySQL 作为网站数据库。
5. 其他的数据库管理系统

    MySQL
    Orcale
    PostgreSQL
    SQL Sever
    DB2
    MariaDB

6. 集群 负载均衡集群，高可用集群
集群通信系统是一种用于集团调度指挥通信的移动通信系统，主要应用在专业移动通信领域。
7. ubuntu包管理 apt dpkg
>dpkg      – Debian 包安装工具
apt-get   – APT 的命令行前端
aptitude  – APT 的高级的字符和命令行前端
synaptic  – 图形界面的 APT 前端
dselect   – 使用菜单界面的包管理工具
tasksel   – Task 安装工具
8. MySQL安装
>sudo apt install mysql-server
sudo vim mysqld.cnf
改成0.0.0.0
netstat -nat | grep 3306
systemctl restart mysql或service mysql restart重启
systemctl status mysql或service mysql status查看服务状态