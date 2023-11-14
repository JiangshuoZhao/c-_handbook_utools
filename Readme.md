# cppreference 外置手册(U-tools专用)
本手册依赖[uTools效率工具](http://www.u.tools/)及其插件[程序员手册](https://yuanliao.info/d/356-1-1-4-bug-tmux)开发。
## 手册制作
1. 相关html文档来自于[https://github.com/myfreeer/cppreference2mshelp/releases](https://github.com/myfreeer/cppreference2mshelp/releases)
2. 使用Python脚本`doc_catalog.py`生成适用于[程序员手册](https://yuanliao.info/d/356-1-1-4-bug-tmux)的目录文件；
## 手册优点：
1. 借助Utools可实现API速查
2. 可自行下载最新的cppreference中文文档，并制作目录
## 使用方法：
1. 下载并安装[uTools效率工具](http://www.u.tools/)；
2. 下载[c++ 外置手册](https://github.com/Nothing1024/Pytorch-handbook-Utools/releases)并解压；
3. 将common文件夹移动到zh文件夹中并更名为assets
4. 在[uTools效率工具](http://www.u.tools/)的插件市场中安装`程序员手册`插件；
5. 在手册插件的`手册设置`中添加手册，根据需要配置名称，关键字，说明，路径（解压后手册的绝对路径）；
6. 点击`保存`，打开手册开关。
## 待改进：
1. css格式已更改(将common文档移动到zh文档内并更名为assets)，uTools明亮主题下显示很好，暗黑主题下显示的不理想，高亮部分比较刺眼。新版本未发布，自行运行py文件更改html文档。
2. 虽然添加了命名空间的索引,可用std::vector查找，但有重复的现象，最终的name是std::std::vector
3. 不能链接跳转，例如查找std::vector,想查看其成员函数push_back，不能跳转push_back的文档
## 动机
虽然uTools中有一个C++函数速查插件，但文档未更新，还是c++20的,c++23的未包含。使用[程序员手册](https://yuanliao.info/d/356-1-1-4-bug-tmux)可以自己定制相关的文档，难点在于获取文档及制作目录。
cppreference的文档可在[https://github.com/myfreeer/cppreference2mshelp/releases](https://github.com/myfreeer/cppreference2mshelp/releases)获取，主要在于制作目录。

自己用，先考虑的是快速使用，缺点很多，有时间后续会先完善链接跳转的功能。

