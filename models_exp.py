# _author_ YinoCao 1/31/2020
# 使用 peewee 库操作 sqlite3
# 建立两个 table: word-book

from settings import DATABASE
from peewee import *

db = SqliteDatabase(DATABASE) #创建数据库类

class NewBook(Model):
    name = CharField()
    total = IntegerField(default=0) #总词汇
    is_analyzed = BooleanField(default=False)
    # reserved columns
    # 保留字段，便于之后扩展
    re1 = CharField(default='')
    re2 = CharField(default='')
    re3 = IntegerField(default=0)
    re4 = IntegerField(default=0)

    class Meta:
        database = db

class NewWord(Model):
    # foreignkey , which books the word collect from
    # book = ForeignKeyField(Book)
    # 单词名
    name = CharField()
    # 解释
    explanation = TextField(default='')
    # 词频
    frequency = IntegerField(default=0)
    # 是否有效
    is_valid = BooleanField(default=True)
    # 音标
    phonogram = CharField(default='')
    # reserved columns
    # 保留字段，便于之后扩展
    re1 = CharField(default='')
    re2 = CharField(default='')
    re3 = IntegerField(default=0)
    re4 = IntegerField(default=0)

    class Meta:
        database = db
