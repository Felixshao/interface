import requests
import json
import warnings
import certifi, urllib3

# http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())


class Runmain():
    """
    接口请求类
    """
    def send_get(self, url, data, cookies):
        """
        get请求
        :param url:接口
        :param data:参数
        :param cookies:cookies
        :return:result;结果
        """
        reques = requests.get(url, params=data, cookies=cookies, verify=False)
        try:
            # 格式化json数据
            result = json.dumps(reques.json(), ensure_ascii=False, sort_keys=True, indent=2)
        except:
            result = reques.text
        return result

    def send_post(self, url, data, cookies):
        """
        post请求
        """
        reques = requests.post(url, data=data, cookies=cookies, verify=False)
        try:
            # 格式化json数据
            result = json.dumps(reques.json(), ensure_ascii=False, sort_keys=True, indent=2)
        except:
            result = reques.text
        return result

    def run_main(self, method, url=None, data=None, cookies=None):
        """
        主函数，通过请求方法调用对应请求方式
        :param method:请求方式
        :param url:
        :param data:
        :param cookies:
        :return:result
        """
        warnings.filterwarnings('ignore')
        result = None
        if method == 'get' or method == 'GET':
            result = self.send_get(url, data, cookies)
        elif method == 'post' or method == 'POST':
            result = self.send_post(url, data, cookies)
        else:
            print('method值错误!!!')
        return result


if __name__ == '__main__':

    reques = Runmain()
    method = 'post'
    url = 'https://www.zhipin.com/wapi/zpgeek/autocomplete/query.json'
    params = {'query': '自动化测试'}
    result = reques.run_main(method, url, params)
    print(result)
