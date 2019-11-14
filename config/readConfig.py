import os
import configparser
from config import getPathInfo

path = getPathInfo.get_path()   # 获取路径
config_path = os.path.join(path, 'config', 'config.ini')  # 连接路径
config = configparser.ConfigParser()    # 调用外部读取配置方法
config.read(config_path, encoding='utf-8')


class ReadConfig():

    def get_http(self, name):
        value = config.get('Http', name)
        return value

    def get_emall(self, name):
        value = config.get('Emall', name)
        return value

    def get_mysql(self, name):
        value = config.get('Mysql', name)
        return value


if __name__ == '__main__':  # 测试类

    read = ReadConfig()
    http_list = ['scheme', 'baseurl', 'port', 'timeout']
    params = []
    for i in http_list:
        params.append(read.get_http(i))

    print(type(params), params)
