import os
import common.log
from config import getPathInfo
from common.configEmall import operate_emall
from config.readConfig import ReadConfig
from common.HTMLTestRunner import HTMLTestRunner
from unite.testSuite import testSuite


log = common.log.logger
path = getPathInfo.get_path()
resultPath = os.path.join(path, 'result', 'report.html')
send_emall = operate_emall()
on_off = ReadConfig().get_emall('on_off')


def run():

    try:
        report = open(resultPath, 'wb')
        suite = testSuite().set_case_suite()
        if suite is not None:
            runny = HTMLTestRunner(stream=report, title='接口自动化报告', description='接口自动化报告描述', verbosity=2)
            runny.run(suite)
        else:
            print('Have no case to test.')
    except Exception as e:
        print('e:', str(e))

    finally:
        print("*********TEST END*********")
        report.close()

    if on_off == 'on':
        operate_emall().send_emall(resultPath)
    else:
        print("邮件发送开关配置关闭，请打开开关后可正常自动发送测试报告")


if __name__ == '__main__':

    run()
    print('123')
    print('456')
    print('456')

    # from testcase.BBoosSearch_test import Boos_case
    # # All_Test().set_case_suite()
    # suite = unittest.TestSuite()
    # suite.addTest(Boos_case().test2_case())
    # runny = unittest.TextTestRunner()
    # runny.run(suite)


