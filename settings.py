# coding=utf-8
# _author_ YinoCao 1/31/2020

import os

# 获取当前所在文件夹路径
_BASEDIR = os.path.dirname(__file__)

# 当前文件夹+数据库文件
DATABASE = os.path.join(_BASEDIR, 'voca.db')

# 是否需要翻译此处可配置，0-不翻译，1-翻译

TRANSLATE = 0

# 需要查找的文件夹 接口1
DIRS = [
    os.path.join(_BASEDIR, 'files')
]

# 需要查找的文件 接口2
FILES = [
    # 示例， 该文件在项目文件夹下， 名为 'python.txt'
    # os.path.join(_BASEDIR, 'fortest.txt')
]

# 每本书抓取的词汇量:抓取单词的数量，不是根据词频，是根据文章长度
NUMBERS = [
    (100, 10),  # 小于 100 取 10 个
    (1000, 100),  # 100 - 1000 取 100 个
    (5000, 300),
    (10000, 500),
    (50000, 1000),
    (999999999, 5000)  # 大于 50000 统一取 1500
]

# 收集一些需要被排除的词汇
# 如要屏蔽一些词，,+""添加到下面的数组里
exclude_list = ["an", "a"

                ]
