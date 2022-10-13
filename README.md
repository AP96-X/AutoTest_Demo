# AutoTest_Demo

## 自动化测试与自动化API测试的综合框架。

# 1.基础知识

[Python基础](https://www.runoob.com/python3/python3-tutorial.html)

[Selenium基础](https://www.selenium.dev/zh-cn/documentation/)

[pytest基础](https://docs.pytest.org/en/stable/)

[allure框架](https://qameta.io/allure-report/)

# 2.自动化使用教程

## 2.1.框架介绍

框架集成pytest + selenium + allure，可用于UI自动化，也可用于API自动化测试。

**项目结构：**

```
- AutoTest_Demo:项目目录
  - ApiData: Api数据文件夹，文件格式: yaml
  - ApiRequest: Api请求实现
  - ApiTestCase: Api自动化测试用例
  - Common: 公共方法
  - Logs: 执行日志存放位置
  - PageObject: 页面对象，包含页面元素和页面操作
  - PageTestCase: UI自动化测试用例存放位置
  - Report: 测试报告存放位置
  - Screenshots: 失败用例截图
  - pytest.ini: pytest配置文件
  - run_api.py: Api自动化测试启动文件
  - run_ui.py: UI自动化测试启动文件
  - requirements.txt: 环境依赖文件
```

**环境依赖：**

```
项目依赖：
1.python~=3.9.x
2.pytest~=7.1.2
3.selenium~=4.1.3
4.allure-pytest~=2.9.45
5.webdriver-manager~=3.5.4
6.requests~=2.27.1
7.PyYaml~=6.0
外部依赖：
1.aullre~=2.17.3
```

**集成开发环境：**

```
PyCharm
```

## 2.2.UI自动化

### 2.2.1.PageObject

这类文件用于定位元素，完整页面的操作逻辑。

```python
from time import sleep

from selenium.webdriver.common.by import By

from Common.basePage import BasePage


class BaiduIndex(BasePage):
    """
    页面元素
    """
    # 百度首页链接
    baidu_index_url = "https://www.baidu.com"
    # 搜索框
    search_input = (By.ID, "kw")
    # "百度一下"按钮框
    search_button = (By.ID, "su")

    # 查询操作
    def search_key(self, search_key):
        # 全局隐性等待
        self.driver.implicitly_wait(10)
        # 开始记录日志
        self.logger.info("【===搜索操作===】")
        # 等待用户名文本框元素出现
        self.wait_ele_visible(self.search_input, model='搜索框')
        # 清除keyword
        self.clean_input_text(self.search_input, model='搜索框')
        # 输入keyword
        self.input_text(self.search_input, text=search_key, model='搜索框')
        # 等待搜索按钮出现
        self.wait_ele_visible(self.search_button, model='"百度一下"搜索按钮')
        # 点击搜索按钮
        self.click_element(self.search_button, model='"百度一下"搜索按钮')
        # 3s后执行后续步骤
        sleep(3)

```

### 2.2.2.PageTestCase

组织测试用例，执行pageobject中的逻辑操作，进行预期结果与实际结果的判断等。

```python
import allure
import pytest

from PageObject.baiduIndex import BaiduIndex
from Utils.browser import driver

baidu_index = BaiduIndex(driver)


@pytest.fixture(scope="class")
def init():
    # 打开浏览器,访问登录页面
    baidu_index.logger.info("\nWebDriver 正在初始化...")
    driver.get(baidu_index.baidu_index_url)
    baidu_index.logger.info(f"打开链接: {baidu_index.baidu_index_url}...")
    # 窗口最大化
    driver.maximize_window()
    # 隐式等待
    driver.implicitly_wait(10)
    baidu_index.logger.info("WebDriver 初始化完成！")
    yield
    driver.quit()
    baidu_index.logger.info("WebDriver 成功退出...")


@allure.feature("百度搜索")
class TestBaiduSearch:

    @pytest.mark.baidu_search
    @allure.story("搜索指定关键字")
    @pytest.mark.parametrize("key_word", [
        "张三",
        "李四"
    ], )
    def test_search(self, init, key_word):
        # @pytest.mark.parametrize 参数化
        baidu_index.search_key(key_word)
        web_title = driver.title
        assert f"{key_word}_百度搜索" == web_title

    @pytest.mark.baidu_search
    @allure.story("这是一个demo")
    def test_demo(self):
        assert 1 == 2

```

### 2.2.3.run_ui.py

测试执行文件：可通过[**.py**]文件或[**标志**]进行执行特定测试用例。

```python
import os
import time

import pytest

if __name__ == '__main__':
    # 当前时间
    now_time = time.strftime('%Y%m%d-%H%M%S', time.localtime(time.time()))
    # allure 测试报告路径
    cur_path = os.path.dirname(os.path.realpath(__file__))
    report_path = os.path.join(cur_path, f'Report/{now_time}')

    # -s : 打印信息 可选
    # -m : 运行含标签的用例 可选
    # ./TestCase/test_001_baiduSearch.py : 测试文件的路径 必要
    pytest.main(["-s", "./TestCase/test_001_baiduSearch.py", "--alluredir", report_path])
    # pytest.main(["-s", "-m", "baidu_search and binganshouye", "./TestCase/", "--alluredir", report_path])
    # 解析并打开测试报告，执行: allure serve {report_path}
    os.system(f"allure serve {report_path}")
    # 生成最终的测试报告，执行allure generate {report_path} -o {report_path}/allure-report --clean
    os.system(f"allure generate {report_path} -o {report_path}/allure-report --clean")

```

## 2.3.API自动化

### 2.3.1.ApiRequest

定义api请求

```python
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

```

### 2.3.2.ApiData

接口所需的数据，一个yaml文件存在多类数据。[参考](https://www.runoob.com/w3cnote/yaml-intro.html)

```yaml
login_data:
  mobile: '18289454846'
  ver_code: '123456'
```

### 2.3.3.ApiTestCase

组织测试用例，执行ApiRequest中的请求操作，进行预期结果与实际结果的判断等。

```python
# test_001_demo.py
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

```

### 2.3.4.run_api.py

测试执行文件：可通过[**.py**]文件或[**标志**]进行执行特定测试用例。

```python
import os
import time

import pytest

if __name__ == '__main__':
    # 当前时间
    now_time = time.strftime('%Y%m%d-%H%M%S', time.localtime(time.time()))
    # allure 测试报告路径
    cur_path = os.path.dirname(os.path.realpath(__file__))
    report_path = os.path.join(cur_path, f'Report/{now_time}')

    # -s : 打印信息 可选
    # -m : 运行含标签的用例 可选
    # ./PageTestCase/test_001_baiduSearch.py : 测试文件的路径 必要
    pytest.main(["-s", "./ApiTestCase/test_001_demo.py", "--alluredir", report_path])
    # pytest.main(["-s", "-m", "baidu_search and binganshouye", "./PageTestCase/", "--alluredir", report_path])
    # 解析并打开测试报告，执行: allure serve {report_path}
    os.system(f"allure serve {report_path}")
    # # 生成最终的测试报告，执行allure generate {report_path} -o {report_path}/allure-report --clean
    os.system(f"allure generate {report_path} -o {report_path}/allure-report --clean")

```

