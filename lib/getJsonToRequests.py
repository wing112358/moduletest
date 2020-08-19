import json
import requests

from config.dataconfig import datapath
from lib.getExcel import read_Excel
from lib.paramToSign import sign


class Send():


    def getapi(self,url, params):
        print("——————————————————————get请求————————————————")
        res = requests.get(url=url, params=params)
        print(res.text)
        return res


    def postapi(self,url, data, type):
        print("——————————————————————post请求————————————————")
        if type == 'form' or type is None:
            res = requests.post(url=url, data=data)
            print(res.text)
        else:
            res1 = requests.post(url=url, data=json.dumps(data))
            print(res1.text)
            return res1

    def sendapi(self,sheetname, casename,key):
        # 从excel读取参数
        sheet = read_Excel()
        datalist = sheet.readexcel(datapath=datapath, sheetname=sheetname)

        f_dict = sheet.getdata(datalist, casename)
        print(f_dict)

        # 判断请求类型，发送请求
        if (f_dict['method'] is None and f_dict['data'] is not None) or (f_dict['method'] == 'post') and f_dict['signflag'] == 0:
            print("是否加签标志-------")
            print(f_dict['signflag'])
            data = f_dict['data']
            print("请求链接----" + f_dict['url'] + '\n' + "请求参数----" + json.dumps(f_dict['data']))
            self.postapi(url=f_dict['url'], data=f_dict['data'], type=f_dict['type'])

        elif(f_dict['signflag'] == 1):
            print("是否加签标志-------")
            print(f_dict['signflag'])
            datasign = sign(f_dict['data'],key)
            print("请求链接----" + f_dict['url'] + '\n' + "请求参数----" + json.dumps(datasign))
            self.postapi(url=f_dict['url'], data=datasign, type=f_dict['type'])

        else:
            print("是否加签标志-------")
            print(f_dict['signflag'])
            print("请求链接----" + f_dict['url'] + '\n' + "请求参数----" + json.dumps(f_dict['params']))
            self.getapi(url=f_dict['url'], params=f_dict['params'])


    if __name__ == '__main__':
        sendapi(sheetname='test_read_excel', casename='test_post')
