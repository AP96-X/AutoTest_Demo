import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from PageObject.baiduIndex import BaiduIndex

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

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
