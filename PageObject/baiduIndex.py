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
