import os
import xlrd
import openpyxl
from config import getPathInfo

path = getPathInfo.get_path()


class operateExcel():
    """
    操作excel类
    """
    def __init__(self, file_name=None, sheet_name=None):
        """
        :param file_name: 文件名称
        param file_name: 表名称
        """
        self.file_name = os.path.join(path, 'testfile', file_name)  # 连接文件路径
        self.sheet_name = sheet_name

    def get_excel(self):
        """
        读取excel并存入list
        :return:data;数据存放在list中返回
        """
        table = xlrd.open_workbook(self.file_name)
        sheet = table.sheet_by_name(self.sheet_name)
        data = [[sheet.cell_value(i, j).replace('\n', '') for j in range(sheet.ncols)]
                for i in range(1, sheet.nrows)]
        return data

    def input_excel(self, result):
        """
        在excel写入结果
        :param result: 传入结果list
        """
        table = openpyxl.load_workbook(self.file_name)
        sheet = table.get_sheet_by_name(self.sheet_name)
        row = 2
        for i in result:
            sheet.cell(row, 5, i)
            row += 1
        table.save(self.file_name)


if __name__ == '__main__':

    read = operateExcel('interface.xlsx', 'Sheet2')
    result = ['erron1', 'erron2']
    data = read.get_excel()
    print(data)
    # read.input_excel(result)