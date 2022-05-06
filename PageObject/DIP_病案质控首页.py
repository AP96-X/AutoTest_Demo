from time import sleep

from selenium.webdriver.common.by import By

from Common.basePage import BasePage


class BingAnZhiKongShouYe(BasePage):
    """
    页面元素
    """
    # url
    dip_index_url = "http://172.20.22.237:9688/cddev/index.html"
    # 医院病案质控清单
    first_function = (By.XPATH, '//*[@id="app"]/div/header/div[3]/ul/li[2]')
    # DIP病案质控首页
    second_function = (By.XPATH, '//*[@id="app"]/div/div/div[1]/div[2]/div/ul/li[1]')
    # iframe
    iframe_refer = (By.ID, 'hospDIPModules.html')
    # 开始时间
    start_time = (By.CSS_SELECTOR, '#startTime > div:nth-child(1) > input:nth-child(1)')
    # 结束时间
    end_time = (By.CSS_SELECTOR, '#endTime > div:nth-child(1) > input:nth-child(1)')
    # 开始时间：2021-01
    start_click = (By.CSS_SELECTOR, '.ant-calendar-month-panel-selected-cell')
    # 结束时间：2021-03
    end_click = (
    By.XPATH, '/html/body/div/div/div/div[5]/div/div/div/div/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[3]')
    # 查询按键
    button_search = (By.XPATH, '//*[@id="app"]/div/div/div[1]/div/div[1]/form/div[7]/div/div/div[1]/button[1]')
    # 响应页面元素
    res_ele = (By.XPATH, '//*[@id="record-chart"]/div[1]/canvas')

    # 查询操作
    def search(self):
        # 全局隐性等待
        self.driver.implicitly_wait(10)
        # 开始记录日志
        self.logger.info("【===DIP病案质控首页查询操作===】")
        # 等待一级菜单元素出现
        self.wait_ele_visible(self.first_function, model='一级菜单')
        # 点击一级菜单
        self.click_element(self.first_function, model='一级菜单')
        # 等待二级菜单元素出现
        self.wait_ele_visible(self.second_function, model='二级菜单')
        # 点击二级菜单
        self.click_element(self.second_function, model='二级菜单')
        # 切换iframe
        self.switch_iframe(self.iframe_refer, model='hospDIPModules')
        # 选择开始时间
        self.click_element(self.start_time, model='开始时间选择框')
        self.click_element(self.start_click, model='开始时间')
        # 选择结束时间
        self.click_element(self.end_time, model='开始结束选择框')
        self.click_element(self.end_click, model='结束时间')
        # 点击查询按键
        self.click_element(self.button_search, model='查询按键')
        # 定位响应后存在的元素
        self.find_element(self.res_ele, model='响应元素')
        # 3s后执行后续步骤
        sleep(3)
