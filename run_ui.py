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
    pytest.main(["-s", "./PageTestCase/test_001_baiduSearch.py", "--alluredir", report_path])
    # pytest.main(["-s", "-m", "baidu_search and binganshouye", "./PageTestCase/", "--alluredir", report_path])
    # 解析并打开测试报告，执行: allure serve {report_path}

    # # 生成最终的测试报告，执行allure generate {report_path} -o {report_path}/allure-report --clean
    os.system(f"allure generate {report_path} -o {report_path}/AutoAPITest-report --clean")

    # 解析并打开测试报告，执行: allure serve {report_path} / allure open {report_path}
    os.system(f"allure serve {report_path}")
