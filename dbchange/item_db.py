print("——————————————————开始导db——————————————————")
from lib.publicDb import query_db
print("——————————————————开始导traceback——————————————————")
print("——————————————————开始执行方法——————————————————")

class Queryitem():
    def querybyname(self,name):
        sql = "select * from item where status = 1 and type = 8 and name ={}{}{}".format("'",name,"'")
        print(sql)
        print("——————————————————开始查询——————————————————")
        itemresult = query_db(sql, 'psa_item')
        print("——————————————————打印结果——————————————————")
        print(itemresult)

        return itemresult
