# 导入pymysql模块
import pymysql

# 连接database
conn = pymysql.connect(host='192.168.3.190', port=3306, user='dev_user', password='df234fl', database='neshield',
                       charset='utf8')
# 得到一个可以执行SQL语句的光标对象
cursor = conn.cursor()
# 定义要执行的SQL语句
sql = """
CREATE TABLE t_user_yang (
id INT auto_increment PRIMARY KEY ,
username varchar(512) NOT NULL ,
password varchar(512) NOT NULL
)ENGINE=innodb DEFAULT CHARSET=utf8;
"""
# 执行SQL语句
cursor.execute(sql)
# 关闭光标对象
cursor.close()
# 关闭数据库连接
conn.close()
