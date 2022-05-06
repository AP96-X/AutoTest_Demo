# demo.py

from Common.http_client import HttpClient


# 继承HttpClient
class Auth(HttpClient):
    # 定义一个登录api的函数，形参 data:字典类型{key: value}
    def login(self, data):
        # self.post()， 调用父类HttpClient的post方法
        return self.post('https://console-api.apipost.cn/api/demo/login', data)


# 实例化Auth类
auth = Auth()
