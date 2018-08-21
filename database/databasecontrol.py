import sqlite3
import datetime
conn = sqlite3.connect('data.db')
cursor = conn.cursor()
#cursor.execute('DROP TABLE USER')
#cursor.execute('DROP TABLE PROJECT')
cursor.execute('CREATE TABLE USER(sn CHAR(9) PRIMARY KEY,name VARCHAR(20) NOT NULL,password VARCHAR(20) NOT NULL,token VARCHAR(200),email VARCHAR(40),level SMALLINT NOT NULL,direction VARCHAR(10))')

cursor.execute('INSERT INTO USER(sn,name,password,level) values (\'031602325\',\'linshen\',\'111111\',\'1\')')
cursor.execute('CREATE TABLE PROJECT (ownersn CHAR(9) NOT NULL,name VARCHAR(20) NOT NULL,description VARCHAR(200),site_address VARCHAR(100) NOT NULL,id INT PRIMARY KEY,date DATE NOT NULL, FOREIGN KEY (ownersn) REFERENCES  USER(sn))')

date = datetime.datetime.now().strftime('%Y-%m-%d')
cursor.execute('INSERT INTO PROJECT values (?,?,?,?,?,?)',('031602325', 'test2', 111, 111, 2, date))
#token='MTUyNzAwNzQzMi4xNzE1OTk5OjM0OGMzM2I3ZjM4ZWE0OGY1YzA0NjJiMTFhMzlhMTkwOWNhYWYyOTU='
#cursor.execute('SELECT USER.name,PROJECT.* FROM USER,PROJECT WHERE USER.sn=PROJECT.ownersn  AND USER.token = "MTUyODEwMDE5Ni4wNjg5MDQ0OjYxYmM2YzQwMzNkODM2ZDJhZjMxZTE0YjkzYjBiM2U1ZWQ1YjZhY2Q="')
#print (cursor.fetchall())
cursor.close()
conn.commit()
conn.close()