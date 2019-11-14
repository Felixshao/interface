import os
import unittest
import time
from config.getPathInfo import get_path
import common.log

path = get_path()
log = common.log.logger
success = 'Success'
fail = 'Fail'


class testSuite():
    def __init__(self):
        """
        初始化参数和数据
        """
        t1 = time.time()
        global resultPath
        resultPath = os.path.join(path, 'result', 'report.html')    # 测试报告文件路径
        self.caseLiseFile = os.path.join(path, 'config', 'caselist.txt')    # 测试用例配置文件路径
        self.caseFile = os.path.join(path, 'testcase')      # 测试用例目录路径
        self.caseList = []  # 存放需要执行的测试用例的list
        log.info('resultPath:' + resultPath)
        log.info('caseLiseFile:' + self.caseLiseFile)
        log.info('caseFile:' + self.caseFile)
        log.info('"{0} Init resultPath: <{1}> , Spend {2} seconds"'.
                 format(success, resultPath, time.time() - t1))

    def set_case_list(self):
        """
        读取caselist文件的用例名称，并存入self.caseList列中
        :return:
        """
        fl = open(self.caseLiseFile, encoding='utf-8')    # 打开测试用例配置文件
        for value in fl.readlines():
            data = str(value)
            if data != '' and not data.startswith('#'):  # data不为空且不以#号开头
                self.caseList.append(data.replace('\n', ''))
        fl.close()

    def set_case_suite(self):
        """
        用例加入测试集中
        :return:
        """
        self.set_case_list()
        test_suite = unittest.TestSuite()
        suite_module = []
        for case in self.caseList:
            case_name = case.split('/')[-1]
            discover = unittest.defaultTestLoader.discover(self.caseFile, pattern=case_name, top_level_dir=None)
            suite_module.append(discover)
        if len(suite_module) > 0:
            for suite in suite_module:
                for test_name in suite:
                    test_suite.addTest(test_name)
        else:
            print('else:')
            return None
        return test_suite   # 返回测试集


if __name__ == '__main__':  # 测试

    print(testSuite().set_case_suite())