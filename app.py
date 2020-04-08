from flask import Flask, request, g, jsonify
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token,
                                jwt_refresh_token_required, create_refresh_token,
                                get_jwt_identity, set_access_cookies,
                                set_refresh_cookies, unset_jwt_cookies)
from ORM import user, category, news
from functools import wraps
from database import get_db

app = Flask(__name__)


def protected(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username == 'api_username' and auth.password == 'api_password':
            return f(*args, **kwargs)
        return jsonify({'message': 'Authentication failed'}), 403

    return decorated


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


@app.route('/login', methods=['POST'])
def user_login():
    return 'Hello World!'


@app.route('/users', methods=['GET'])
def user_get_all():
    db = get_db()
    user_cur = db.execute('select * from user')
    users = user_cur.fetchall()
    return_values = []
    for user in users:
        user_dict = {}
        user_dict['id'] = user['id']
        user_dict['username'] = user['username']
        user_dict['password'] = user['password']
        user_dict['email'] = user['email']
        user_dict['is_active'] = user['is_active']
        return_values.append(user_dict)

    return jsonify({'members': return_values})


@app.route('/users', methods=['GET'])
def user_insert():
    return 'Hello World!'


@app.route('/users', methods=['GET'])
def user_edit():
    return 'Hello World!'


@app.route('/category', methods=['GET'])
def category_get_all():
    db = get_db()
    newscategory_cur = db.execute('select * from newscategory')
    newscategories = newscategory_cur.fetchall()
    return_values = []
    for newscategory in newscategories:
        newscategory_dict = {'id': newscategory['id'], 'title': newscategory['title'], 'is_deleted': newscategory['is_deleted']}
        return_values.append(newscategory_dict)

    return jsonify({'newscategory': return_values})


@app.route('/news', methods=['GET'])
def news_get_all():
    return 'Hello World!'


@app.route('/news/<new_id>', methods=['POST'])
def news_update(new_id):
    return 'Hello World!'


@app.route('/news', methods=['POST'])
def news_insert():
    return 'Hello World!'


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
