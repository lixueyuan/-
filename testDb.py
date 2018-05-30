import pymysql

pymysql.install_as_MySQLdb()

#打开数据库连接
db = pymysql.connect(host="localhost",user="root",
    password="123456",db="test",port=3306)

# 使用cursor()方法获取操作游标
cur = db.cursor()

# 1.查询操作
# 编写sql 查询语句  user 对应我的表名
# sql = "select * from user"
# try:
#     a = cur.execute(sql)  # 执行sql语句
#     print(a)
#
#
# except Exception as e:
#     raise e
# finally:
#     db.close()  # 关闭连接

sql_insert = """insert into user(id,username,password) values(2,'wang123132123','1123234')"""

try:
    cur.execute(sql_insert)
    # 提交
    db.commit()
except Exception as e:
    # 错误回滚
    db.rollback()
finally:
    db.close()
