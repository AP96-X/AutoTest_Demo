# test_api.py
import allure
import pytest

from ApiRequest.demo import auth
from Utils.read_yaml import read_data

login_data = read_data.load_data('demo.yaml')


@allure.feature("ApiPost")
class TestNetease:
    @pytest.mark.ApiPostLogin
    @allure.story("手机号登录")
    def test_01(self):
        # 从yaml文件中读取数据，组合为 字典类型dict：data_for_login, 传入调用的请求方法中。
        data_for_login = {'mobile': login_data['login_data']['mobile'],
                          'ver_code': login_data['login_data']['ver_code']}
        # xxxx.json, 将结果转变为json字符串
        response = auth.login(data=data_for_login).json()
        # response.get('code')， 从结果中读取code，与预期结果对比
        assert response.get('code') == 10000
