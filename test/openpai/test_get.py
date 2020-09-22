#import unittest
import pytest
import os,sys
sys.path.append(os.getcwd())            #告诉pytest运行前先检索当前路径

import sys
from config.dataconfig import datapath

# print("路径-------")
# print(sys.path)
from lib.getJsonToRequests import Send

# sys.path.append("..")

class TestPost():
    def testpost_normal(self):
        sendrequest = Send()
        result = sendrequest.sendapi(datapath=datapath,sheetname='test_read_excel', casename='test_get')
        print(result)

    def test_add(self):
        a=3
        b=a+1
        print(b)

if __name__ == '__main__':
    pytest.main(["test_get.py"])

