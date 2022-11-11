from sqlalchemy import create_engine, Column, Integer, String  # crate_engine()方法用于创建数据库连接
from sqlalchemy.ext.declarative import declarative_base  # 导入基类,用于声明性系统映射
from sqlalchemy.orm import sessionmaker

# 导入pymysql模块
import pymysql

# 连接database
conn = pymysql.connect(host='127.0.0.1', user='root', password='986203', database='go_shorturl', charset='utf8')
# 得到一个可以执行SQL语句的光标对象
cursor = conn.cursor()
# 定义要执行的SQL语句
sql = """
CREATE TABLE USER1 (
id INT auto_increment PRIMARY KEY ,
name CHAR(10) NOT NULL UNIQUE,
age TINYINT NOT NULL
)ENGINE=innodb DEFAULT CHARSET=utf8;
"""
# 执行SQL语句
cursor.execute(sql)
# 关闭光标对象
cursor.close()
# 关闭数据库连接
conn.close()
