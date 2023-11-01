from sqlalchemy.exc import SQLAlchemyError

from flaskr import db
from flaskr.model.interactive_user import InteractiveUser


def insert_user(username, password):
    try:
        user = InteractiveUser()
        user.username = username
        user.password = password
        # 将对象user放入session
        db.session.add(user)
        # 提交数据
        db.session.flush()
        db.session.commit()
        return user
    except SQLAlchemyError as e:
        raise e


# 根据用户ID更新用户密码
def update_model_state(id, password):
    user = db.session.query(InteractiveUser).filter(InteractiveUser.id == id).first()
    user.password = password
    db.session.commit()
    return user


# 根据用户ID更新用户密码
def get_user_by_id(id):
    user = db.session.query(InteractiveUser).filter(InteractiveUser.id == id).first()
    return user


def get_user_by_name(username):
    user = db.session.query(InteractiveUser).filter(InteractiveUser.username == username).first()
    return user
