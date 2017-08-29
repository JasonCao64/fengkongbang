# from selenium import webdriver
#
# class Driver:
#
#     def __init__(self):
#         chrome_options = webdriver.ChromeOptions()
#         chrome_options.add_argument('enable_automation')
#         self.driver = webdriver.Chrome(chrome_options=chrome_options)
#         # self.driver.get('http://login_test.fengkongbang.cn/justitia/toLogin.htm')

from selenium import webdriver

def browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('enable_automation')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.set_window_size(1394, 877)
    driver.set_window_position(0, 0)
    return driver

if __name__ == '__main__':
    dr = browser()
    dr.get("http://120.27.150.120:8083/justitia/toLogin.htm")
    dr.quit()
