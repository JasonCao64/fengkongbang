
class Page(object):

    baidu_url = 'http://login_test.fengkongbang.cn/justitia/toLogin.htm'

    def __init__(self, selenium_driver, base_url=baidu_url, parent=None):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30
        self.parent = parent

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    # def _open(self, url):
    #     url = self.base_url + url
    #     self.driver.get(url)
    #     assert self.on_page(), 'Did not land on %s' % url
    #
    # def open(self):
    #     self._open(self.url)
    #
    # def on_page(self):
    #     return (self.driver.current_url).encode('utf-8') == (self.base_url + self.url)
    #
    # def script(self, src):
    #     return self.driver.execute_script(src)