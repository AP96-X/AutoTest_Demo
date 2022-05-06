import json

import requests

from Utils.myLog import MyLog


class HttpClient:
    __headers = {
        "content-type": "application/json;charset=UTF-8"
    }

    def __init__(self):
        self.__session = requests.session()
        self.logger = MyLog().get_log()

    def get(self, path, **kwargs):
        return self.__request(path, 'GET', **kwargs)

    def post(self, path, data=None, json_string=None, **kwargs):
        return self.__request(path, 'POST', data, json_string, **kwargs)

    def __request(self, url, method, data=None, json_string=None, **kwargs):
        headers = kwargs.get("headers")
        params = kwargs.get("params")
        # 如果传入header不为空，那么将更新为传入的header
        if headers:
            self.__headers.update(headers)
        self.__request_log(url, method, data, json_string, params, self.__headers)
        resp = None
        if method == "GET":
            resp = self.__session.get(url, **kwargs)
        elif method == "POST":
            resp = requests.post(url, data, json_string, **kwargs)
        self.__response_log(resp)
        return resp

    def __request_log(self, url, method, data=None, json_string=None, params=None, headers=None):
        self.logger.info("接口请求地址: {}".format(url))
        self.logger.info("接口请求方式: {}".format(method))
        self.logger.info("接口请求头: {}".format(json.dumps(headers, indent=4, ensure_ascii=False)))
        self.logger.info("接口请求 params 参数: {}".format(json.dumps(params, indent=4, ensure_ascii=False)))
        self.logger.info("接口请求体 data 参数 : {}".format(json.dumps(data, indent=4, ensure_ascii=False)))
        self.logger.info("接口请求体 json 参数: {}".format(json.dumps(json_string, indent=4, ensure_ascii=False)))

    def __response_log(self, resp):
        try:
            self.logger.info("返回信息 : {}".format(resp.text, ensure_ascii=False))
        except Exception as e:
            self.logger.error('系统错误：{}'.format(e))
