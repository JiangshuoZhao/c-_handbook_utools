import requests
import os
from glob import glob
import json
from pyquery import PyQuery as pq

def find_html_files(root_folder):
    html_files = []
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file.endswith(".html"):
                html_files.append(os.path.join(root, file)[42:])
                #这里取42及之后的是为了获取相对路径，json文件的path属性使用绝对路径不能用
                #根据自己的存放地址变动
                #例如我的放在D:\c++doc\html-book-20231001\reference\zh\文件下
    return html_files

def get_catalog(path):
    with open(path,'r',encoding='utf-8') as file:
        html_content = file.read()
        fun_name = ''
        try:
            # 获取文档描述信息
            doc = pq(html_content)
            css_link = doc('link[href*="common"]')
            css_scr=doc('script[src*="common"]')
            for item in css_link.items():
                href = item.attr('href')
                href = href.replace('../common','assets')
                item.attr('href',href)
                # print(item)
            # print(css_link)
            for item in css_scr.items():
                src = item.attr('src')
                src = src.replace('../common', 'assets')
                item.attr('src', src)
                # print(item)
            # print(css_scr)
            # print(doc)

            with open(path, 'w', encoding='utf-8') as fp:
                fp.write(str(doc))

            name = doc('#firstHeading')
            # print(name)
            prev = name('span')
            if(prev):
                fun_name += prev.text()

            fun_name +=name.text()
            print(fun_name)
            fun_desc = fun_name
        except:
            pass

    fun_setting = {
                        "name": fun_name,
                        "type": "cpp",
                        "path": path,
                        "desc": fun_desc
                    }

    return fun_setting



#
if __name__ == '__main__':
    current_path = os.getcwd()
    # 调用函数查找所有 .html 后缀的文件路径
    html_file_paths = find_html_files(current_path)
    # print(html_file_paths)

    fun_settings = []
    # 提取信息，制作目录
    count = 0
    for file_path in html_file_paths:

        fun_settings.append(get_catalog(file_path))

        count += 1
    print('-----------------------------')
    print(count)


    #写入json文件中
    # with open('./cpp.json', 'w', encoding='utf-8') as fp:
    #     json.dump(list(fun_settings), fp)
