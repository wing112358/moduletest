import unittest
import sys
print("路径-------")
print(sys.path)
from lib.getJsonToRequests import Send

sys.path.append("..")




class TestPost(unittest.TestCase):
    def testpost_normal(self):
        sendrequest = Send()
        result = sendrequest.sendapi(sheetname='test_read_excel', casename='test_get')
        print(result)