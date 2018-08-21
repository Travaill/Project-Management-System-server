import time
import base64
import hmac

key  = "JLUIE487"

#生成token
def generate_token(key, expire=3600):
    ts_str = str(time.time() + expire)
    ts_byte = ts_str.encode("utf-8")
    sha1_tshexstr  = hmac.new(key.encode("utf-8"),ts_byte,'sha1').hexdigest()
    token = ts_str+':'+sha1_tshexstr
    b64_token = base64.urlsafe_b64encode(token.encode("utf-8"))
    return b64_token.decode("utf-8")

#验证token
def certify_token(key, token):
    token_str = base64.urlsafe_b64decode(token).decode('utf-8')
    token_list = token_str.split(':')
    if len(token_list) != 2:
        return False
    ts_str = token_list[0]
    if float(ts_str) < time.time():
        # token expired
        return False
    known_sha1_tsstr = token_list[1]
    sha1 = hmac.new(key.encode("utf-8"),ts_str.encode('utf-8'),'sha1')
    calc_sha1_tsstr = sha1.hexdigest()
    if calc_sha1_tsstr != known_sha1_tsstr:
        # token certification failed
        return False
    # token certification success
    return True

import sqlite3
import json
def SignIn(sn,password):
    conn = sqlite3.connect('./database/data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM USER WHERE sn = ? AND password = ?',(sn,password,))
    values=cursor.fetchall()
    if len(values) == 0:  #登录失败
        data ={'info':'登录失败','status_code':400}
    else:
        token = generate_token(key, 3600)
        cursor.execute('UPDATE USER SET token = ? WHERE sn = ?',(token,sn,))
        conn.commit()
        cursor.execute('SELECT * FROM USER WHERE sn = ? AND password = ?', (sn, password,))
        values = cursor.fetchall()
        data={'sn':values[0][0],
        'token':values[0][3],
        'level':values[0][5],
        'info':'登录成功',
        'status_code':200}
    cursor.close()
    conn.close()
    return data



