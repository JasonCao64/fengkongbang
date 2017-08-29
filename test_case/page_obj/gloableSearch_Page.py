from test_case.models import myunit
from test_case.models.Xpath import *
import time

class gloableSearch_testcase(myunit.myTest):

    def login(self, username, password):
        self.driver.find_element_by_xpath(username_inputbox).clear()
        self.driver.find_element_by_xpath(username_inputbox).send_keys(username)
        self.driver.find_element_by_xpath(password_inputbox).clear()
        self.driver.find_element_by_xpath(password_inputbox).send_keys(password)
        self.driver.find_element_by_xpath(authCode_loc).send_keys('T@$!0')
        self.driver.find_element_by_xpath(submit_button).click()

    def __gloableSearchEnterance(self):
        self.login('18202815282', '123456')
        time.sleep(3)
        self.driver.find_element_by_xpath(collection_icon).click()
        # self.driver.implicitly_wait(20)
        time.sleep(2)
        login_windows = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != login_windows:
                self.driver.switch_to_window(handle)
                self.driver.implicitly_wait(20)

    def searchButton(self):
        self.driver.find_element_by_xpath(gloableSearch_button).click()

    def contactsPhone(self, contacts_phone):
        self.driver.find_element_by_xpath(contactsPhone_loc).send_keys(contacts_phone)

    def idCard(self, id_card):
        self.driver.find_element_by_xpath(idCard_loc).send_keys(id_card)

    def accountNo(self, account_no):
        self.driver.find_element_by_xpath(accountNo_loc).send_keys(account_no)

    def cardNo(self, card_no):
        self.driver.find_element_by_xpath(cardNo_loc).send_keys(card_no)

    def address(self, address):
        self.driver.find_element_by_xpath(address_loc).send_keys(address)

    def custName(self, cust_name):
        self.driver.find_element_by_xpath(custName_loc).send_keys(cust_name)

    def searchNull_verify(self):
        return self.driver.find_element_by_xpath(sarchNull_verify_loc).text

    def searchPhone_verify(self):
        return self.driver.find_element_by_xpath(search_phone_verify).text

    def no_search_result_verify(self):
        return self.driver.find_element_by_xpath(no_search_result).text

    def search_IdCard_verify(self):
        return self.driver.find_element_by_xpath(searchIdCard_verify).text

    def search_AccountNo_verify(self):
        return self.driver.find_element_by_xpath(searchAccountNo_verify).text

    def search_cardNo_verify(self):
        return self.driver.find_element_by_xpath(searchCardNo_verify).text

    def search_address_verify(self):
        return self.driver.find_element_by_xpath(searchAddress_verify).text

    # 不输入任何条件搜索
    def test_search_bull(self):
        self.__gloableSearchEnterance()
        time.sleep(1)
        self.searchButton()
        time.sleep(0.5)
        self.assertEqual(self.searchNull_verify(), '请输入查询条件!')

    # 搜索正确手机号码
    def test_search_phone(self):
        self.__gloableSearchEnterance()
        time.sleep(1)
        self.contactsPhone('13698281632')
        time.sleep(0.5)
        self.searchButton()
        time.sleep(1)
        all_handles1 = self.driver.window_handles
        self.driver.switch_to_window(all_handles1[2])
        time.sleep(1)
        self.driver.find_element_by_xpath(click_search_result).click()
        time.sleep(1)
        all_handles2 = self.driver.window_handles
        self.driver.switch_to_window(all_handles2[3])
        self.driver.find_element_by_xpath(click_more).click()
        self.assertEqual(self.searchPhone_verify(), '13698281632')

    # 搜索错误手机号码
    def test_search_phone1(self):
        self.__gloableSearchEnterance()
        time.sleep(1)
        self.contactsPhone('987654321')
        time.sleep(0.5)
        self.searchButton()
        time.sleep(1)
        all_handles1 = self.driver.window_handles
        self.driver.switch_to_window(all_handles1[2])
        time.sleep(1)
        self.assertEqual(self.no_search_result_verify(), '共有案件0条')


    # 搜索特殊字符
    def test_search_phone2(self):
        self.__gloableSearchEnterance()
        time.sleep(1)
        self.contactsPhone('！@#abc')
        time.sleep(0.5)
        self.searchButton()
        time.sleep(1)
        all_handles1 = self.driver.window_handles
        self.driver.switch_to_window(all_handles1[2])
        time.sleep(1)
        self.assertEqual(self.no_search_result_verify(), '共有案件0条')

    # 搜索正确的证件号
    def test_search_idCard(self):
        self.__gloableSearchEnterance()
        time.sleep(1)
        self.idCard('510103197301192867')
        time.sleep(0.5)
        self.searchButton()
        time.sleep(1)
        all_handles1 = self.driver.window_handles
        self.driver.switch_to_window(all_handles1[2])
        time.sleep(1)
        self.assertEqual(self.search_IdCard_verify(), '510103197301192867')

    # 搜索错误的证件号
    def test_search_idCard1(self):
        self.__gloableSearchEnterance()
        time.sleep(1)
        self.idCard('987654321')
        time.sleep(0.5)
        self.searchButton()
        time.sleep(3)
        all_handles1 = self.driver.window_handles
        self.driver.switch_to_window(all_handles1[2])
        time.sleep(1)
        self.assertEqual(self.no_search_result_verify(), '共有案件0条')

    # 搜索特殊字符
    def test_search_idCard2(self):
        self.__gloableSearchEnterance()
        time.sleep(1)
        self.idCard('！@#abc')
        time.sleep(0.5)
        self.searchButton()
        time.sleep(3)
        all_handles1 = self.driver.window_handles
        self.driver.switch_to_window(all_handles1[2])
        time.sleep(1)
        self.assertEqual(self.no_search_result_verify(), '共有案件0条')

    # 搜索正确的账号
    def test_search_accountNo(self):
        self.__gloableSearchEnterance()
        time.sleep(1)
        self.accountNo('51211981')
        time.sleep(0.5)
        self.searchButton()
        time.sleep(3)
        all_handles1 = self.driver.window_handles
        self.driver.switch_to_window(all_handles1[2])
        time.sleep(1)
        self.assertEqual(self.search_AccountNo_verify(), '51211981')

    # 搜索错误的账号
    def test_search_accountNo1(self):
        self.__gloableSearchEnterance()
        time.sleep(1)
        self.accountNo('987654321')
        time.sleep(0.5)
        self.searchButton()
        time.sleep(3)
        all_handles1 = self.driver.window_handles
        self.driver.switch_to_window(all_handles1[2])
        time.sleep(1)
        self.assertEqual(self.no_search_result_verify(), '共有案件0条')

    # 搜索特殊字符
    def test_search_accountNo2(self):
        self.__gloableSearchEnterance()
        time.sleep(1)
        self.accountNo('！@#abc')
        time.sleep(0.5)
        self.searchButton()
        # self.driver.implicitly_wait(20)
        time.sleep(3)
        all_handles1 = self.driver.window_handles
        self.driver.switch_to_window(all_handles1[2])
        time.sleep(1)
        self.assertEqual(self.no_search_result_verify(), '共有案件0条')

    # 搜索正确的卡号
    def test_search_cardNo(self):
        self.__gloableSearchEnterance()
        time.sleep(1)
        self.cardNo('6217903100013349493')
        time.sleep(0.5)
        self.searchButton()
        self.driver.implicitly_wait(10)
        all_handles1 = self.driver.window_handles
        self.driver.switch_to_window(all_handles1[2])
        time.sleep(1)
        self.assertEqual(self.search_cardNo_verify(), '6217903100013349493')

    # 搜索错误的卡号
    def test_search_cardNo1(self):
        self.__gloableSearchEnterance()
        time.sleep(1)
        self.cardNo('987654321')
        time.sleep(0.5)
        self.searchButton()
        time.sleep(3)
        all_handles1 = self.driver.window_handles
        self.driver.switch_to_window(all_handles1[2])
        time.sleep(1)
        self.assertEqual(self.no_search_result_verify(), '共有案件0条')

    # 搜索特殊字符
    def test_search_cardNo2(self):
        self.__gloableSearchEnterance()
        time.sleep(1)
        self.cardNo('！@#abc')
        time.sleep(0.5)
        self.searchButton()
        time.sleep(3)
        all_handles1 = self.driver.window_handles
        self.driver.switch_to_window(all_handles1[2])
        time.sleep(1)
        self.assertEqual(self.no_search_result_verify(), '共有案件0条')

    # 搜索正确的地址
    def test_search_address(self):
        self.__gloableSearchEnterance()
        time.sleep(1)
        self.address('成都')
        time.sleep(0.5)
        self.searchButton()
        time.sleep(1)
        all_handles1 = self.driver.window_handles
        self.driver.switch_to_window(all_handles1[2])
        time.sleep(8)
        self.driver.find_element_by_xpath(click_search_result).click()
        time.sleep(1)
        all_handles2 = self.driver.window_handles
        self.driver.switch_to_window(all_handles2[3])
        self.assertIn('成都', self.search_address_verify())

    # 搜索错误的地址
    def test_search_address1(self):
        self.__gloableSearchEnterance()
        time.sleep(1)
        self.address('呵呵呵呵')
        time.sleep(0.5)
        self.searchButton()
        time.sleep(1)
        all_handles1 = self.driver.window_handles
        self.driver.switch_to_window(all_handles1[2])
        time.sleep(1)
        self.assertEqual(self.no_search_result_verify(), '共有案件0条')

    # 搜索特殊字符
    def test_search_address2(self):
        self.__gloableSearchEnterance()
        time.sleep(1)
        self.address('*&^&')
        time.sleep(0.5)
        self.searchButton()
        time.sleep(1)
        all_handles1 = self.driver.window_handles
        self.driver.switch_to_window(all_handles1[2])
        time.sleep(1)
        self.assertEqual(self.no_search_result_verify(), '共有案件0条')

    # 组合搜索
    def test_multiple_search(self):
        self.__gloableSearchEnterance()
        time.sleep(1)
        list1 = [address_loc, custName_loc, cardNo_loc, contactsPhone_loc, idCard_loc, accountNo_loc]
        list2 = ['成都', '胡明', '4380886882888120', '13730811792', '510107199004062972', '0435834219882187']
        for (i, j) in zip(list1, list2):
            self.driver.find_element_by_xpath(i).send_keys(j)
            self.searchButton()
            time.sleep(3)
        all_handle1 = self.driver.window_handles
        self.driver.switch_to_window(all_handle1[2])
        self.assertEqual(self.search_IdCard_verify(), '510107199004062972')
