from day16.utils.DBUtils import MysqlUtils
from day16.utils.ExcelUtils import ExcelUtils
import os
class DataRead:
    list = None
    def __init__(self,mode,filename="",sheetname="0",host="localhost",database="",user="",password="",tablename=""):
        if mode == "excel":
            if filename == "":
                raise Exception("文件名不能为空！")
            elif not os.path.isfile(filename):
                raise Exception("文件不从在！")
            else:
                DataRead.list = ExcelUtils.read(filename,sheetname)

        elif mode == "database":
            DataRead.list = MysqlUtils.read(host=host,database=database,user=user,password=password,tablename=tablename)

        else:
            raise Exception("对不起，您的操作模式无法识别！")
d = DataRead("database",database="bank",tablename="bankzhanghu",user="root",password="")
print(d.list)

