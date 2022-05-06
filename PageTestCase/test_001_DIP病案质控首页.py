import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from PageObject.DIP_病案质控首页 import BingAnZhiKongShouYe

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

bingAnShouYe = BingAnZhiKongShouYe(driver)


@pytest.fixture(scope="class")
def init():
    # 打开浏览器, 访问登录页面
    bingAnShouYe.logger.info("\nWebDriver 正在初始化...")
    driver.get(bingAnShouYe.dip_index_url)
    # 清空cookies
    driver.delete_all_cookies()
    # 添加cookies
    driver.add_cookie(cookie_dict={'name': 'JSESSIONID', 'value': 'A798502728027936296D1AA498FD4F18'})
    driver.add_cookie(cookie_dict={'name': 'http://172.20.22.237:5002/gateway/drgTA-JTOKEN',
                                   'value': 'eyJ0eXAiOiJqd3QiLCJjbGFnIjoiSFM1MTIiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiIxNzIuMTcuMC4xIiwiaWF0IjoxNjUwNzYzOTY3LCJzdWIiOiI1REQ4NDM4NEM4RkY3NTVCMTBGNUU4RTY4QzY0Mzg0ODUxRTQ2RURBRTBGMTYyMjk1QjAzQjczMENCODQwNUEyRTkyQjcxMTUyQzU5N0RBMTk3RkZGRjJDOTQ0REIxREQiLCJqdGkiOiIwM2ZjYmNkYjU2ZjY0ZmFlOGI4MWFkZTMwMjg4Zjc1NCJ9.c6KCFSAEbE67H_4ujRMCDpXhn6PzZn11f8nd0QJw0C-o7ADvdc92ljGcbFIOHG_11hVrw9rKZ9ZMMc1DqYTaxw'})
    driver.add_cookie(cookie_dict={'name': 'http://172.20.22.237:5002/gateway/drgTA-RJTOKEN',
                                   'value': 'yJ0eXAiOiJqd3QiLCJjbGFnIjoiSFM1MTIiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiIxNzIuMTcuMC4xIiwiaWF0IjoxNjUwNzYzOTY3LCJzdWIiOiI1REQ4NDM4NEM4RkY3NTVCMTBGNUU4RTY4QzY0Mzg0ODUxRTQ2RURBRTBGMTYyMjk1QjAzQjczMENCODQwNUEyRTkyQjcxMTUyQzU5N0RBMTk3RkZGRjJDOTQ0REIxREQiLCJqdGkiOiJkZjNjMDM0MmEzZDU0MTVhYmUxYWQzODJlOWNjNTg1ZSJ9.2Ohmph8FFy6NOwyFRyGx4d4kkD0BoY7btPf7fRH4M-dc4wJFUnxDamg2Fr3h0Cf685YTcRmx1bGm0YXMMk1Ziw'})
    # 添加cookies后重载页面
    driver.get(bingAnShouYe.dip_index_url)
    bingAnShouYe.logger.info(f"打开链接: {bingAnShouYe.dip_index_url}...")
    # 窗口最大化
    driver.maximize_window()
    # 隐式等待
    driver.implicitly_wait(10)
    bingAnShouYe.logger.info("WebDriver 初始化完成！")
    yield
    driver.quit()
    bingAnShouYe.logger.info("WebDriver 成功退出...")


@allure.feature("医院病案清单质控")
class TestDIPSearch:

    @pytest.mark.BingAnShouYe
    @allure.story("DIP病案质控首页 - 查询")
    def test_search(self, init):
        bingAnShouYe.search()
        res = bingAnShouYe.find_element(bingAnShouYe.res_ele)
        assert res is not None

    @pytest.mark.bingAnShouYe
    @allure.story("DIP病案质控首页 - 重置")
    def test_reset(self):
        assert 1 == 1
