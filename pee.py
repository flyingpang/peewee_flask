# coding: utf-8
from flask import Flask
from peewee import *
from peewee import create_model_tables
from playhouse.flask_utils import FlaskDB

DATABASE = 'postgresql://postgres:passwd@localhost:5432/pee'


app = Flask(__name__)
app.debug = True
app.config.from_object(__name__)

database = FlaskDB(app)

class User(database.Model):
    username = CharField(unique=True)
    password = CharField()
    age = IntegerField()

@app.route('/')
def hello_world():
    # 创建表
    # User.create(username='aaa', password='aaapasswd', age=20)

    # 新增行
    # User.create(username='bbb', password='bbbpasswd', age=20)

    # 插入行
    # q = User.insert(username='ccc', password='cccpasswd', age=21)
    # q.execute()

    # 单行查询
    # q = User.get(username='aaa')
    # print q.username, q.age

    # 多行查询
    # query = User.select().where(User.age == '20').order_by(User.username.desc())
    # for q in query:
    #     print q.username, q.age

    # 更新
    # q = User.update(age=22).where(User.username == 'ccc')
    # q.execute()

    # 删除
    # q = User.get(User.username ** 'C%')
    # q.delete_instance()

    # 统计
    # total = User.select(fn.Sum(User.age).alias('total_age'))
    return 'Hello World!'


if __name__ == '__main__':
    create_model_tables([User], fail_silently=True)
    app.run()
