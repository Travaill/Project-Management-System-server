import sqlite3
import datetime
def AddProject(token,name,description ,site_address):
        conn = sqlite3.connect('./database/data.db')
        cursor = conn.cursor()
        cursor.execute('SELECT sn FROM USER WHERE token = ? ', (token,))
        values = cursor.fetchall()
        print (values)
        ownersn =values[0][0]
        cursor.execute('SELECT MAX(id) FROM PROJECT')
        values = cursor.fetchall()
        id = values[0][0]
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        try:
            cursor.execute('INSERT INTO PROJECT values (?,?,?,?,?,?)',(ownersn, name, description, site_address, id+1, date,))
            conn.commit()
        except:
            info = {'info': '添加失败','statusCode':400}
        else:
            info = {'info': '添加成功','statusCode':200}
        cursor.close()
        conn.close()
        return  info

def DelProject(id):
    conn = sqlite3.connect('./database/data.db')
    cursor = conn.cursor()
    try:
        cursor.execute('DELETE FROM PROJECT WHERE id = ?',(id,))
        conn.commit()
    except:
        info = {'info': '删除失败', 'statusCode': 400}
    else:
        info = {'info': '删除成功', 'statusCode': 200}
    cursor.close()
    conn.close()
    return info

def UpdateProject(id,name,description ,site_address):
    conn = sqlite3.connect('./database/data.db')
    cursor = conn.cursor()
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    try:
        cursor.execute('UPDATE  PROJECT SET name = ?,description= ?,site_address= ?,date= ? WHERE id = ?',(name, description,date, site_address,id,))
        conn.commit()
    except:
        info = {'info': '更新失败', 'statusCode': 400}
    else:
        info = {'info': '更新成功', 'statusCode': 200}
    cursor.close()
    conn.close()
    return info

def GetProject(token):
    conn = sqlite3.connect('./database/data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT PROJECT.* FROM USER,PROJECT WHERE USER.sn=PROJECT.ownersn AND token=? ', (token,))
    values = cursor.fetchall()
    print (values)
    id = 1
    info = {}
    for data in values:
        info[id]={'id':data[4],
                  'name':data[1],
                  'description':data[2],
                  'site_address':data[3],
                  'date':data[5],}
        id+=1
    conn.commit()
    cursor.close()
    conn.close()
    return  info



