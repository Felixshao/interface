import unittest
import json
from json import JSONDecodeError
import paramunittest, ddt
from common.base import base
from common.operateExcel import operateExcel
from common.configHttp import Runmain

excel = operateExcel('interface.xlsx', 'Sheet1')
search_data = excel.get_excel()
result_list = []


@ddt.ddt
# @paramunittest.parametrized(*search_data)
class Boos_case(unittest.TestCase):

    # def setParameters(self, case_name, url, method, params, result):
    #     """
    #
    #     :param case_name:
    #     :param url:
    #     :param method:
    #     :param params:
    #     :return:
    #     """
    #     self.case_name = case_name
    #     self.url = url
    #     self.method = method
    #     self.params = eval(params)
    #     self.result = result
    @classmethod
    def setUpClass(cls):

        print('测试前准备')
        pass

    @classmethod
    def tearDownClass(cls):

        print('测试结束，输入log完结！！！')

    # @ddt.data(*search_data)
    # def test1_case(self, data):
    #     self.case_name = data[0]
    #     self.method = data[2]
    #     self.url = data[1]
    #     self.params = data[3]
    #     self.checkResult()

    def test2_case(self):
        
        print('123')

    def checkResult(self):
        result = Runmain().run_main(self.method, self.url, self.params)
        print(result)
        try:
            ss = json.loads(result)
            if self.case_name == 'boos搜索接口':
                # print(result)
                base().assert_Equal(ss['code'], 1)
                result_list.append(base().assert_Equal(ss['message'], 'Success'))
            else:
                # print(result)
                result_list.append('pass')
        except JSONDecodeError as js:
            # print('msg:{}'.format(js))
            # print(result)
            result_list.append('pass')


if __name__ == '__main__':

    case = Boos_case()
    case.test_case()
    print(result_list)
    print('1')

