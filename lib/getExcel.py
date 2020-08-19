import xlrd

from config.dataconfig import datapath


class read_Excel():
    #获取工作表所有数据
    def readexcel(self,datapath,sheetname):
        #根据文件路径打开excel表
        book = xlrd.open_workbook(datapath)
        #根据sheet名称打开表
        table = book.sheet_by_name(sheetname)

        # 获取总行数
        row_Num = table.nrows

        #获取第一行数据，作为字典的key值
        title = table.row_values(0)

        #新建一个空列表承接数据
        datalist = []

        #将标题和每行数据组装成字典
        for i in range(1, row_Num):
            d = dict(zip(title,table.row_values(i)))
            datalist.append(d)
        return datalist    #列表嵌套字典格式，列表每个元素是一个字典



    #根据用例名获取case参数
    def getdata(self,datalist,dataname):
        for casedata in datalist:
            if dataname == casedata['casename']:
                return casedata


if __name__=='__main__':
    sheet = read_Excel()
    datalist = sheet.readexcel(datapath=datapath, sheetname='test_read_excel')

    f_dict = sheet.getdata(datalist, 'test_post')
    print(f_dict)