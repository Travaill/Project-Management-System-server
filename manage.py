import sqlite3
import datetime

def projectManage(token):
    conn = sqlite3.connect('./database/data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT level FROM USER where token=? ', (token,))
    values = cursor.fetchall()
    level = values[0][0]
    cursor.execute('SELECT PROJECT.ID,PROJECT.NAME,PROJECT.DESCRIPTION,PROJECT.SITE_ADDRESS,PROJECT.DATE FROM USER,PROJECT  WHERE user.sn = project.ownersn and level >= ?', (level,))
    values = cursor.fetchall()
    info = {}
    id = 1
    for data in values:
        info[id]={'id':data[0],
                  'name':data[1],
                  'description':data[2],
                  'site_address':data[3],
                  'date':data[4],}
        id+=1
    cursor.close()
    conn.close()
    return info

def UserManage(token):
    conn = sqlite3.connect('./database/data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT level FROM USER where token=? ', (token,))
    values = cursor.fetchall()
    level = values[0][0]
    cursor.execute('SELECT name,sn,level,direction FROM USER WHERE level >= ?', (level,))
    values = cursor.fetchall()
    info = {}
    id = 1
    for data in values:
        info[id]={'name':data[0],
                  'sn':data[1],
                  'level':data[2],
                  'direction':data[3],}
        id+=1
    cursor.close()
    conn.close()
    return info