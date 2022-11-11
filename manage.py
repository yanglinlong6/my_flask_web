from flask import request

from flaskr import create_app
import pymysql
from flaskr.biz import user_service

# 初始化MySQLdb模块
pymysql.install_as_MySQLdb()

app = create_app()


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/yang')
def hello_world_yang():
    yang = request.args.get("name")
    insert_user = user_service.insert_user(yang, 986203)
    print('insert_user===', insert_user.serialize)
    user = user_service.get_user_by_name(yang)
    print('user===', user.serialize)
    return 'Hello World yang!'


if __name__ == '__main__':
    app.run()
