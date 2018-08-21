import sqlite3
import datetime


def GetUser(token):
    conn = sqlite3.connect('./database/data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM USER WHERE token = ?', (token,))
    values = cursor.fetchall()
    if len(values) == 0:
        data ={'info':'获取信息失败','status_code':400}
    else:
        data = {'info': '获取项目成功',
                'status_code': 200,
                'name': values[0][1],
                'sn': values[0][0],
                'email': values[0][4]}
    cursor.close()
    conn.close()
    return data


def UpdateUser(token,name,email):
    conn = sqlite3.connect('./database/data.db')
    cursor = conn.cursor()
    try:
        cursor.execute('UPDATE USER SET name = ?,email= ? WHERE token = ?',(name,email,token,))
        conn.commit()
    except:
        info = {'info': '更新失败', 'statusCode': 400}
    else:
        info = {'info': '更新成功', 'statusCode': 200}
    cursor.close()
    conn.close()
    return info

def AddUser(sn,name,password,email):
    conn = sqlite3.connect('./database/data.db')
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO USER(sn,name,password,email,level) values (?,?,?,?,?)',(sn,name,password,email,5,))  #默认新注册的用户为五级权限
    except:
        info = {'info':'注册失败','statusCode':401}
    else:
        info = {'info': '注册成功','statusCode':200}
    conn.commit()
    cursor.close()
    conn.close()
    return info

