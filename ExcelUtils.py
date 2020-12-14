import xlrd

class ExcelUtils:
    @classmethod
    def read(cls,filename="",sheetname="0"):
        try:
            list = []
            file = xlrd.open_workbook(filename,)
            if sheetname.isdigit():
                sheet = file.sheet_by_index(int(sheetname))
                rows = sheet.nrows
                for i in range(rows):
                    list.append(sheet.row_values(i))
                return list
            else:
                sheet = file.sheet_by_name(sheetname)
                rows = sheet.nrows
                for i in range(rows):
                    list.append(sheet.row_values(i))
                    return list
        except Exception as error:
            print(error)
result = ExcelUtils.read("D:\\Users\\86923\\PycharmProjects\\pythonProject1\\day16\\testcase\\a.xlsx","用户管理")
print(result)


