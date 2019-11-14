import flask
import json
from flask import request

"""
"""
# 创建一个服务，当前py文件当做一个服务
server = flask.Flask(__name__)


# 装饰器将函数转换为服务，参数传入设置的接口路径和请求方式
@server.route('/login', methods=['get', 'post'])
def login():
    username = request.values.get('name')
    password = request.values.get('pwd')
    code = request.values.get('code')

    if username and password and code:
        if username == 'xiaoming' and password == '111':
            resu = {'code': 200, 'message': '登录成功'}
            return json.dumps(resu, ensure_ascii=False)  # 将字典转换字符串
        else:
            resu = {'code': -1, 'message': '账号密码错误'}
            return json.dumps(resu, ensure_ascii=False)
    else:
        resu = {'code': 10001, 'message': '参数不能为空！'}
        return json.dumps(resu, ensure_ascii=False)


if __name__ == '__main__':
    server.run(debug=True, port=8888, host='127.0.0.1')
