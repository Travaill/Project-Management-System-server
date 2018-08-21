from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask_cors import *
from login import *
from user import *
from project import *
from manage import *
app=Flask(__name__)
key  = "JLUIE487"

CORS(app, resources=r'/*')
@app.route('/login', methods=['POST'])   #登录
def Login():
        if request.method == 'POST':
            sn=request.get_json()['sn']
            password=request.get_json()['password']
            info = SignIn(sn, password)
            return json.dumps(info),info['status_code']

@app.route('/user', methods=['POST','PUT','GET'])
def UserOperation():                                 #注册
    token = request.headers.get('X-USER-TOKEN')
    if request.method == 'POST':
        sn = request.get_json()['sn']
        name=request.get_json()['name']
        password = request.get_json()['password']
        email = request.get_json()['email']
        info = AddUser(sn,name,password,email)
        return json.dumps({'info': info['info']}), info['statusCode']
    else:
        if certify_token(key, token):
            if request.method == 'GET':
                info = GetUser(token)
                print (token)
                print (info)
                return json.dumps(info)
            elif request.method == 'PUT':
                email = request.get_json()['email']
                name = request.get_json()['name']
                info = UpdateUser(token,name,email)
                return json.dumps(info)
        else:
            return json.dumps({'info': '请重新登录'}), 401

@app.route('/project/<int:id>', methods=['POST','GET','PUT','DELETE'])  #项目相关接口
def ProjetOperation(id):
    token = request.headers.get('X-USER-TOKEN')
    if certify_token(key, token):
        if request.method == 'GET':           #获取项目列表
            data = GetProject(token)
            return json.dumps(data)
        elif request.method == 'POST':
            name = request.get_json()['name']
            description = request.get_json()['description']
            site_address = request.get_json()['site_address']
            info = AddProject(token, name, description, site_address)
            return json.dumps({'info':info['info']}),info['statusCode']
        elif request.method == 'PUT':
            name = request.get_json()['name']
            description = request.get_json()['description']
            site_address = request.get_json()['site_address']
            id = request.get_json()['id']
            info = UpdateProject(id, name, description, site_address)
            return json.dumps({'info': info['info']}), info['statusCode']
        elif request.method == 'DELETE':
            info = DelProject(id)
            return json.dumps({'info': info['info']}), info['statusCode']
    else:
        return json.dumps({'info': '请重新登录'}), 401

@app.route('/manage/project', methods=['POST','GET','PUT','DELETE'])
def Project():
    token = request.headers.get('X-USER-TOKEN')
    if certify_token(key, token):
        if request.method == 'GET':
            info = projectManage(token)
            return json.dumps(info)

@app.route('/manage/user', methods=['POST','GET'])
def User():
    token = request.headers.get('X-USER-TOKEN')
    if certify_token(key, token):
        if request.method == 'GET':
            info = UserManage(token)
            return json.dumps(info)

if __name__=='__main__':
   app.run(debug=True)