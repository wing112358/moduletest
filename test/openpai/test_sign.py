#import unittest
import pytest
import sys

from config.dataconfig import datapath
from config.keyconfig import testkey
from dbchange.item_db import Queryitem
import json

print("路径-------")
print(sys.path)
from lib.getJsonToRequests import Send

sys.path.append("..")




class TestPost():
    def testpost_normal(self):
        sendrequest = Send()
        result = sendrequest.sendapi(datapath=datapath,sheetname='test_read_excel', casename='test_sign',key=testkey)
        print(result)

        querybyname = Queryitem()
        sqlresult=querybyname.querybyname("插电版车型")

        assert json.loads(result.text).get('code')==200


