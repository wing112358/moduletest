import unittest
import sys

from dbchange.item_db import Queryitem

print("路径-------")
print(sys.path)
from lib.getJsonToRequests import Send

sys.path.append("..")




class TestPost(unittest.TestCase):
    def testpost_normal(self):
        sendrequest = Send()
        result = sendrequest.sendapi(sheetname='test_read_excel', casename='test_post')
        print(result)

        querybyname = Queryitem()
        sqlresult=querybyname.querybyname("插电版车型")

        self.assertIn(result,200)
