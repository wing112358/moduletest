import pymysql#导第三方库

#根据参数获取连接
from config.dbconfig import *


def get_db_coon(host,user,passwd,db):
    conn = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        passwd=passwd,
        db=db,
        charset = 'utf8'
    )
    return conn


#根据sql增，删，改
def change_db(sql,db):
    conn = get_db_coon(host=psa_sit_host,user=psa_sit_user,passwd=psa_sit_pwd,db=db)    #获取连接
    cur = conn.cursor()   #建立游标
    try:
        cur.execute(sql)   #执行sql
        conn.commit()      #提交更改
    except Exception as e: #捕捉异常
        conn.rollback()    #回滚
    finally:
        cur.close()        #关闭游标
        conn.close()       #关闭连接



#查
def query_db(sql,db):
    conn = get_db_coon(host=psa_sit_host, user=psa_sit_user, passwd=psa_sit_pwd, db=db)  # 获取连接
    cur = conn.cursor()  # 建立游标
    cur.execute(sql)  # 执行sql
    result = cur.fetchall()   #获取结果
    cur.close()  # 关闭游标
    conn.close()  # 关闭连接
    return result  #返回结果




