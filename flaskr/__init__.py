import pymysql

pymysql.install_as_MySQLdb()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 初始化数据库
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    # 加载数据库配置
    # app.config.from_object('config')
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:986203@127.0.0.1:3306/go_shorturl'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://dev_user:df234fl@192.168.3.190:3306/neshield'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_ECHO'] = True
    # 向app中导入并注册db
    db.init_app(app)
    return app
