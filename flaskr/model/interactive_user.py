from flaskr import db


# 定义user表对应的model类InteractiveUser
class InteractiveUser(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=False)
    password = db.Column(db.String(80), unique=False)

    # 序列化
    @property
    def serialize(self):
        return {'id': self.id, 'username': self.username, 'password': self.password}

    # 定义获取属性的各个方法
    def get_id(self):
        return self.id

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password
