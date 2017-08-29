from test_case.models.driver import browser
from selenium import webdriver
import unittest

class myTest(unittest.TestCase):
    # driver = None
    def setUp(self):
        # self.driver = Driver().driver
        # self.driver.get('http://login_test.fengkongbang.cn/justitia/toLogin.htm')
        self.driver = browser()
        # # 测试环境
        # self.driver.get('http://login_test.fengkongbang.cn/justitia/toLogin.htm')
        # 生产环境
        # self.driver.get('http://120.27.150.120:8083/justitia/toLogin.htm')
        self.driver.get('https://login.fengkongbang.cn/justitia/toLogin.htm')
        self.driver.implicitly_wait(20)

    def tearDown(self):
        self.driver.quit()