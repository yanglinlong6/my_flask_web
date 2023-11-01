from flask import Blueprint

simple = Blueprint('simple', __name__)


@simple.route('/test')
def hello_world():
    return 'Hello World!'
