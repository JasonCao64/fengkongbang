from test_case.models import myunit
from test_case.models.Xpath import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select

class myCase_testcase(myunit.myTest):

    def login(self, username, password):
        self.driver.find_element_by_xpath(username_inputbox).clear()
        self.driver.find_element_by_xpath(username_inputbox).send_keys(username)
        self.driver.find_element_by_xpath(password_inputbox).clear()
        self.driver.find_element_by_xpath(password_inputbox).send_keys(password)
        self.driver.find_element_by_xpath(authCode_loc).send_keys('T@$!0')
        self.driver.find_element_by_xpath(submit_button).click()

    def myCase_iFrame(self):
        return self.driver.find_element_by_xpath(myCase_iFrame_loc)

    def myCaseList_verify(self):
        return self.driver.find_element_by_xpath(myCaseList_verify).text

    def secondPage_verify(self):
        return self.driver.find_element_by_xpath(secondPage_verify).text

    def searchBtn(self):
        self.driver.find_element_by_xpath(searchButton).click()

    def trustorVerify(self):
        return self.driver.find_element_by_xpath(trustorVerify_loc).text

    def resultVerify(self):
        return self.driver.find_element_by_xpath(resultVerify_loc).text

    def collectionStatusVerify(self):
        return self.driver.find_element_by_xpath(collectionStatusVerify_loc).text
    #
    # def commissionDateWrongVerify(self):
    #     return self.driver.switch_to_alert().text

    # 我的案件统一入口
    def __myCaseEnterance(self):
        self.login('18202815282', '123456')
        time.sleep(2)
        self.driver.find_element_by_xpath(collection_icon).click()
        time.sleep(2)
        login_windows = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != login_windows:
                self.driver.switch_to_window(handle)
                self.driver.implicitly_wait(20)
                self.driver.find_element_by_xpath(collection_management).click()
                self.driver.find_element_by_xpath(myCase).click()
                self.driver.implicitly_wait(20)
                self.driver.switch_to_frame(self.myCase_iFrame())

    # 进入我的案件列表
    def test_myCaseList(self):
        self.__myCaseEnterance()
        self.driver.find_element_by_xpath(click_current_page).click()
        # 滚动页面至指定的位置
        js = "var q=document.body.scrollTop=500"
        self.driver.execute_script(js)
        self.assertEqual(self.myCaseList_verify(), '张0757')

    # 搜索委托方
    def test_searchTrustor(self):
        self.__myCaseEnterance()
        # 搜索有结果
        self.driver.implicitly_wait(20)
        Select(self.driver.find_element_by_xpath(trustorSelect)).select_by_visible_text('马上消费')
        self.searchBtn()
        time.sleep(1)
        self.driver.find_element_by_xpath(clickAnyCase).click()
        all_handles1 = self.driver.window_handles
        self.driver.switch_to_window(all_handles1[2])
        time.sleep(1)
        self.assertEqual(self.trustorVerify(), '马上消费')
        # 搜索无结果
        self.driver.switch_to_window(all_handles1[1])
        self.driver.switch_to_frame(self.myCase_iFrame())
        self.driver.implicitly_wait(20)
        # self.driver.find_element_by_xpath(trustorCheckbox).click()
        Select(self.driver.find_element_by_xpath(trustorSelect)).select_by_visible_text('中国银行')
        self.searchBtn()
        time.sleep(1)
        self.assertEqual(self.resultVerify(), '共有案件0条')

    # 搜索案件类型
    def test_searchCaseType(self):
        self.__myCaseEnterance()
        # 搜索有结果
        self.driver.implicitly_wait(20)
        Select(self.driver.find_element_by_xpath(caseTypeSelect_loc)).select_by_visible_text('留案')
        self.searchBtn()
        time.sleep(1)
        self.assertEqual(self.resultVerify(), '共有案件1条')
        # 搜索无结果
        time.sleep(2)
        Select(self.driver.find_element_by_xpath(caseTypeSelect_loc)).select_by_visible_text('打包')
        self.searchBtn()
        time.sleep(1)
        self.assertEqual(self.resultVerify(), '共有案件0条')

    # 搜索委案日期
    def test_searchCommissionDate(self):
        self.__myCaseEnterance()
        # 搜索有结果
        self.driver.implicitly_wait(20)
        ActionChains(self.driver).double_click(self.driver.find_element_by_xpath(commissionDateStart_loc)).perform()
        self.driver.find_element_by_xpath(commissionDateStart_loc).send_keys('2017-05-31')
        self.searchBtn()
        time.sleep(1)
        self.assertEqual(self.resultVerify(), '共有案件750条')
        time.sleep(1)
        ActionChains(self.driver).double_click(self.driver.find_element_by_xpath(commissionDateStart_loc)).perform()
        ActionChains(self.driver).double_click(self.driver.find_element_by_xpath(commissionDateEnd_loc)).perform()
        self.driver.find_element_by_xpath(commissionDateEnd_loc).send_keys('2017-05-31')
        self.searchBtn()
        time.sleep(1)
        self.assertEqual(self.resultVerify(), '共有案件250条')
        # 搜索无结果
        time.sleep(2)
        ActionChains(self.driver).double_click(self.driver.find_element_by_xpath(commissionDateStart_loc)).perform()
        self.driver.find_element_by_xpath(commissionDateStart_loc).send_keys('2017-05-01')
        ActionChains(self.driver).double_click(self.driver.find_element_by_xpath(commissionDateEnd_loc)).perform()
        self.driver.find_element_by_xpath(commissionDateEnd_loc).send_keys('2017-05-01')
        self.searchBtn()
        time.sleep(1)
        self.assertEqual(self.resultVerify(), '共有案件0条')
        # 日期格式不合法
        time.sleep(2)
        ActionChains(self.driver).double_click(self.driver.find_element_by_xpath(commissionDateStart_loc)).perform()
        self.driver.find_element_by_xpath(commissionDateStart_loc).send_keys('a017-o9-01')
        self.searchBtn()
        self.assertIn('不合法的日期格式', self.driver.switch_to_alert().text)

    # 搜索上次跟进日期
    def test_searchLFUDate(self):
        self.__myCaseEnterance()
        # 搜索有结果
        self.driver.implicitly_wait(20)
        ActionChains(self.driver).double_click(self.driver.find_element_by_xpath(LFUDateStart_loc)).perform()
        self.driver.find_element_by_xpath(LFUDateStart_loc).send_keys('2017-05-31')
        self.searchBtn()
        time.sleep(1)
        self.assertEqual(self.collectionStatusVerify(), '新案')
        time.sleep(1)
        ActionChains(self.driver).double_click(self.driver.find_element_by_xpath(LFUDateStart_loc)).perform()
        ActionChains(self.driver).double_click(self.driver.find_element_by_xpath(LFUDateEnd_loc)).perform()
        self.driver.find_element_by_xpath(LFUDateEnd_loc).send_keys('2017-05-31')
        self.searchBtn()
        time.sleep(1)
        self.assertEqual(self.resultVerify(), '共有案件0条')
        # 搜索无结果
        time.sleep(2)
        ActionChains(self.driver).double_click(self.driver.find_element_by_xpath(LFUDateStart_loc)).perform()
        self.driver.find_element_by_xpath(LFUDateStart_loc).send_keys('2017-05-01')
        ActionChains(self.driver).double_click(self.driver.find_element_by_xpath(LFUDateEnd_loc)).perform()
        self.driver.find_element_by_xpath(LFUDateEnd_loc).send_keys('2017-05-01')
        self.searchBtn()
        time.sleep(1)
        self.assertEqual(self.resultVerify(), '共有案件0条')
        # 日期格式不合法
        time.sleep(2)
        ActionChains(self.driver).double_click(self.driver.find_element_by_xpath(LFUDateStart_loc)).perform()
        self.driver.find_element_by_xpath(LFUDateStart_loc).send_keys('a017-o9-01')
        self.searchBtn()
        self.assertIn('不合法的日期格式', self.driver.switch_to_alert().text)

    # 搜索标色状态
    def test_searchColorStatus(self):
        self.__myCaseEnterance()
        # 搜索有结果
        self.driver.implicitly_wait(20)
        Select(self.driver.find_element_by_xpath(colorStatusSelect_loc)).select_by_visible_text('标红')
        self.searchBtn()
        time.sleep(1)
        self.assertEqual(self.resultVerify(), '共有案件1条')
        # 搜索无结果
        time.sleep(2)
        Select(self.driver.find_element_by_xpath(colorStatusSelect_loc)).select_by_visible_text('标紫')
        self.searchBtn()
        time.sleep(1)
        self.assertEqual(self.resultVerify(), '共有案件0条')

    # 搜索催收状态
    def test_searchCollectionStatus(self):
        self.__myCaseEnterance()
        # 搜索有结果
        # self.driver.implicitly_wait(20)
        time.sleep(3)
        Select(self.driver.find_element_by_xpath(collectionStatusSelect_loc)).select_by_visible_text('有线索')
        self.searchBtn()
        time.sleep(1)
        self.assertEqual(self.collectionStatusVerify(), '有线索')
        # 搜索无结果
        time.sleep(2)
        Select(self.driver.find_element_by_xpath(collectionStatusSelect_loc)).select_by_visible_text('其他')
        self.searchBtn()
        time.sleep(1)
        self.assertEqual(self.resultVerify(), '共有案件0条')

    # 搜索还款情况
    def test_searchRepayment(self):
        self.__myCaseEnterance()
        # 搜索有结果
        self.driver.implicitly_wait(20)
        Select(self.driver.find_element_by_xpath(repaymentSelect_loc)).select_by_visible_text('部分还款')
        self.searchBtn()
        time.sleep(2)
        self.assertEqual(self.resultVerify(), '共有案件1条')
        time.sleep(2)
        Select(self.driver.find_element_by_xpath(repaymentSelect_loc)).select_by_visible_text('已结清')
        self.searchBtn()
        time.sleep(2)
        self.assertEqual(self.resultVerify(), '共有案件0条')
        # 搜索无结果
        time.sleep(2)
        Select(self.driver.find_element_by_xpath(repaymentSelect_loc)).select_by_visible_text('未还款')
        self.searchBtn()
        time.sleep(2)
        self.assertEqual(self.resultVerify(), '共有案件999条')

    # 搜索还款日期
    def test_searchRepaymentDate(self):
        self.__myCaseEnterance()
        # 搜索有结果
        self.driver.implicitly_wait(20)
        ActionChains(self.driver).double_click(self.driver.find_element_by_xpath(repaymentDateStart_loc)).perform()
        self.driver.find_element_by_xpath(repaymentDateStart_loc).send_keys('2017-05-31')
        self.searchBtn()
        time.sleep(1)
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="mycase"]/tbody/tr/td[16]').text, '2017-08-08')
        time.sleep(2)
        ActionChains(self.driver).double_click(self.driver.find_element_by_xpath(repaymentDateStart_loc)).perform()
        self.driver.find_element_by_xpath(repaymentDateStart_loc).send_keys('2017-08-08')
        ActionChains(self.driver).double_click(self.driver.find_element_by_xpath(repaymentDateEnd_loc)).perform()
        self.driver.find_element_by_xpath(repaymentDateEnd_loc).send_keys('2017-08-08')
        self.searchBtn()
        time.sleep(1)
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="mycase"]/tbody/tr/td[16]').text, '2017-08-08')
        # 搜索无结果
        time.sleep(1)
        ActionChains(self.driver).double_click(self.driver.find_element_by_xpath(repaymentDateStart_loc)).perform()
        ActionChains(self.driver).double_click(self.driver.find_element_by_xpath(repaymentDateEnd_loc)).perform()
        self.driver.find_element_by_xpath(repaymentDateEnd_loc).send_keys('2017-05-31')
        self.searchBtn()
        time.sleep(1)
        self.assertEqual(self.resultVerify(), '共有案件0条')
        # 日期格式不合法
        time.sleep(2)
        ActionChains(self.driver).double_click(self.driver.find_element_by_xpath(repaymentDateStart_loc)).perform()
        self.driver.find_element_by_xpath(repaymentDateStart_loc).send_keys('a017-o9-01')
        self.searchBtn()
        self.assertIn('不合法的日期格式', self.driver.switch_to_alert().text)

    # 搜索委案金额
    def test_searchEntrustAmt(self):
        self.__myCaseEnterance()
        # 搜索有结果
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(entrustAmtMin_loc).send_keys('10000')
        self.searchBtn()
        time.sleep(1)
        self.assertEqual(self.resultVerify(), '共有案件4条')
        ActionChains(self.driver).double_click(self.driver.find_element_by_xpath(entrustAmtMin_loc)).perform()
        self.driver.find_element_by_xpath(entrustAmtMax_loc).send_keys('500')
        self.searchBtn()
        time.sleep(1)
        self.assertEqual(self.resultVerify(), '共有案件10条')
        self.driver.find_element_by_xpath(entrustAmtMin_loc).send_keys('1')
        ActionChains(self.driver).double_click(self.driver.find_element_by_xpath(entrustAmtMax_loc)).perform()
        self.driver.find_element_by_xpath(entrustAmtMax_loc).send_keys('100')
        self.searchBtn()
        time.sleep(1)
        self.assertEqual(self.resultVerify(), '共有案件1条')
        # 搜索无结果
        ActionChains(self.driver).double_click(self.driver.find_element_by_xpath(entrustAmtMax_loc)).perform()
        self.driver.find_element_by_xpath(entrustAmtMax_loc).send_keys('1')
        self.searchBtn()
        time.sleep(1)
        self.assertEqual(self.resultVerify(), '共有案件0条')
        # # 非数字
        # ActionChains(self.driver).double_click(self.driver.find_element_by_xpath(entrustAmtMin_loc)).perform()
        # self.driver.find_element_by_xpath(entrustAmtMax_loc).send_keys('abc')
        # self.searchBtn()
        # time.sleep(1)
        # self.assertEqual(self.driver.find_element_by_xpath(entrustAmtMinWrong_loc).text, '请输入数字')
        # ActionChains(self.driver).double_click(self.driver.find_element_by_xpath(entrustAmtMin_loc)).perform()
        # ActionChains(self.driver).double_click(self.driver.find_element_by_xpath(entrustAmtMax_loc)).perform()
        # self.driver.find_element_by_xpath(entrustAmtMax_loc).send_keys('abc')
        # self.searchBtn()
        # time.sleep(1)
        # self.assertEqual(self.driver.find_element_by_xpath(entrustAmtMaxWrong_loc).text, '请输入数字')

    # 搜索电话
    def test_searchPhoneNo(self):
        self.__myCaseEnterance()
        # 搜索有结果
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(phoneNo_loc).send_keys('18000000653')
        self.searchBtn()
        time.sleep(2)
        self.assertEqual(self.resultVerify(), '共有案件1条')
        # 搜索无结果
        ActionChains(self.driver).double_click(self.driver.find_element_by_xpath(phoneNo_loc)).perform()
        self.driver.find_element_by_xpath(phoneNo_loc).send_keys('11111111111111')
        self.searchBtn()
        time.sleep(1)
        self.assertEqual(self.resultVerify(), '共有案件0条')

    # 搜索逾期天数
    def test_searchOverdueDays(self):
        self.__myCaseEnterance()
        # 搜索有结果
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(overdueDaysMin_loc).send_keys('170')
        self.searchBtn()
        time.sleep(1)
        self.assertEqual(self.resultVerify(), '共有案件12条')
        ActionChains(self.driver).double_click(self.driver.find_element_by_xpath(overdueDaysMin_loc)).perform()
        self.driver.find_element_by_xpath(overdueDaysMax_loc).send_keys('100')
        self.searchBtn()
        time.sleep(1)
        self.assertEqual(self.resultVerify(), '共有案件12条')
        self.driver.find_element_by_xpath(overdueDaysMin_loc).send_keys('1')
        ActionChains(self.driver).double_click(self.driver.find_element_by_xpath(overdueDaysMax_loc)).perform()
        self.driver.find_element_by_xpath(overdueDaysMax_loc).send_keys('50')
        self.searchBtn()
        time.sleep(1)
        self.assertEqual(self.resultVerify(), '共有案件1条')
        # 搜索无结果
        ActionChains(self.driver).double_click(self.driver.find_element_by_xpath(overdueDaysMax_loc)).perform()
        self.driver.find_element_by_xpath(overdueDaysMax_loc).send_keys('1')
        self.searchBtn()
        time.sleep(1)
        self.assertEqual(self.resultVerify(), '共有案件0条')
        # # 非数字
        # ActionChains(self.driver).double_click(self.driver.find_element_by_xpath(overdueDaysMin_loc)).perform()
        # self.driver.find_element_by_xpath(overdueDaysMin_loc).send_keys('abc')
        # self.searchBtn()
        # time.sleep(1)
        # self.assertEqual(self.driver.find_element_by_xpath(entrustAmtMinWrong_loc).text, '请输入数字')
        # ActionChains(self.driver).double_click(self.driver.find_element_by_xpath(overdueDaysMin_loc)).perform()
        # ActionChains(self.driver).double_click(self.driver.find_element_by_xpath(overdueDaysMax_loc)).perform()
        # self.driver.find_element_by_xpath(overdueDaysMax_loc).send_keys('abc')
        # self.searchBtn()
        # time.sleep(1)
        # self.assertEqual(self.driver.find_element_by_xpath(entrustAmtMaxWrong_loc).text, '请输入数字')

    # 搜索账龄
    def test_searchAccountAge(self):
        self.__myCaseEnterance()
        # 搜索有结果
        self.driver.implicitly_wait(20)
        Select(self.driver.find_element_by_xpath(accountAge_loc)).select_by_visible_text('M2')
        self.searchBtn()
        time.sleep(2)
        self.assertEqual(self.driver.find_element_by_xpath(accountAgeVerify_loc).text, 'M2')
        # 搜索无结果
        ActionChains(self.driver).double_click(self.driver.find_element_by_xpath(accountAge_loc)).perform()
        Select(self.driver.find_element_by_xpath(accountAge_loc)).select_by_visible_text('M3')
        self.searchBtn()
        time.sleep(1)
        self.assertEqual(self.resultVerify(), '共有案件0条')

    # 搜索催收区域
    def test_searchCollectionArea(self):
        self.__myCaseEnterance()
        # 搜索有结果
        time.sleep(2)
        Select(self.driver.find_element_by_xpath(collectionAreaSelect_loc)).select_by_visible_text('成都市')
        self.searchBtn()
        time.sleep(1)
        self.assertEqual(self.resultVerify(), '共有案件750条')
        Select(self.driver.find_element_by_xpath(collectionAreaSelect_loc)).select_by_visible_text('乐山市')
        self.searchBtn()
        time.sleep(1)
        self.assertEqual(self.resultVerify(), '共有案件250条')
        # 搜索无结果
        Select(self.driver.find_element_by_xpath(collectionAreaSelect_loc)).select_by_visible_text('贵阳市')
        self.searchBtn()
        time.sleep(1)
        self.assertEqual(self.resultVerify(), '共有案件0条')

    # 搜索地址
    def test_searchAddress(self):
        self.__myCaseEnterance()
        # 搜索有结果
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(searchAddress_loc).send_keys('成都')
        self.searchBtn()
        time.sleep(1)
        self.assertEqual(self.resultVerify(), '共有案件19条')
        ActionChains(self.driver).double_click(self.driver.find_element_by_xpath(searchAddress_loc)).perform()
        self.driver.find_element_by_xpath(searchAddress_loc).send_keys('北京')
        self.searchBtn()
        time.sleep(2)
        self.assertEqual(self.resultVerify(), '共有案件8条')
        # 搜索无结果
        ActionChains(self.driver).double_click(self.driver.find_element_by_xpath(searchAddress_loc)).perform()
        self.driver.find_element_by_xpath(searchAddress_loc).send_keys('aaa')
        self.searchBtn()
        time.sleep(1)
        self.assertEqual(self.resultVerify(), '共有案件0条')

    # 搜索姓名
    def test_searchName(self):
        self.__myCaseEnterance()
        # 搜索有结果
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(searchName_loc).send_keys('张0432')
        self.searchBtn()
        time.sleep(2)
        self.assertEqual(self.resultVerify(), '共有案件1条')
        ActionChains(self.driver).double_click(self.driver.find_element_by_xpath(searchName_loc)).perform()
        self.driver.find_element_by_xpath(searchName_loc).send_keys('张0528')
        self.driver.find_element_by_xpath(searchName_loc).send_keys(Keys.ENTER)
        self.driver.find_element_by_xpath(searchName_loc).send_keys('张0110')
        self.searchBtn()
        time.sleep(2)
        self.assertEqual(self.resultVerify(), '共有案件2条')
        # 搜索无结果
        ActionChains(self.driver).double_click(self.driver.find_element_by_xpath(searchName_loc)).perform()
        self.driver.find_element_by_xpath(searchName_loc).send_keys('aaa')
        self.searchBtn()
        time.sleep(1)
        self.assertEqual(self.resultVerify(), '共有案件0条')

    # 搜索卡号
    def test_searchCardNo(self):
        self.__myCaseEnterance()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(searchCardNo_loc).send_keys('6217000000000000809')
        self.searchBtn()
        time.sleep(2)
        self.assertEqual(self.resultVerify(), '共有案件1条')
        ActionChains(self.driver).double_click(self.driver.find_element_by_xpath(searchCardNo_loc)).perform()
        self.driver.find_element_by_xpath(searchCardNo_loc).send_keys('6217000000000000235')
        self.driver.find_element_by_xpath(searchCardNo_loc).send_keys(Keys.ENTER)
        self.driver.find_element_by_xpath(searchCardNo_loc).send_keys('6217000000000000333')
        self.searchBtn()
        time.sleep(2)
        self.assertEqual(self.resultVerify(), '共有案件2条')
        # 搜索无结果
        ActionChains(self.driver).double_click(self.driver.find_element_by_xpath(searchCardNo_loc)).perform()
        self.driver.find_element_by_xpath(searchCardNo_loc).send_keys('aaa')
        self.searchBtn()
        time.sleep(1)
        self.assertEqual(self.resultVerify(), '共有案件0条')

    # 搜索序列号
    def test_searchSerialNo(self):
        self.__myCaseEnterance()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(searchSerialNo_loc).send_keys('TEST201708080303')
        self.searchBtn()
        time.sleep(2)
        self.assertEqual(self.resultVerify(), '共有案件1条')
        ActionChains(self.driver).double_click(self.driver.find_element_by_xpath(searchSerialNo_loc)).perform()
        self.driver.find_element_by_xpath(searchSerialNo_loc).send_keys('TEST201708080301')
        self.driver.find_element_by_xpath(searchSerialNo_loc).send_keys(Keys.ENTER)
        self.driver.find_element_by_xpath(searchSerialNo_loc).send_keys('TEST201708080308')
        self.searchBtn()
        time.sleep(2)
        self.assertEqual(self.resultVerify(), '共有案件2条')
        # 搜索无结果
        ActionChains(self.driver).double_click(self.driver.find_element_by_xpath(searchSerialNo_loc)).perform()
        self.driver.find_element_by_xpath(searchSerialNo_loc).send_keys('aaa')
        self.searchBtn()
        time.sleep(1)
        self.assertEqual(self.resultVerify(), '共有案件0条')

    # 搜索批次号
    def test_searchBatchNo(self):
        self.__myCaseEnterance()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(searchBatchNo_loc).send_keys('QA测试')
        self.searchBtn()
        time.sleep(5)
        self.assertEqual(self.resultVerify(), '共有案件750条')
        ActionChains(self.driver).double_click(self.driver.find_element_by_xpath(searchBatchNo_loc)).perform()
        self.driver.find_element_by_xpath(searchBatchNo_loc).send_keys('QA测试1')
        self.searchBtn()
        time.sleep(5)
        self.assertEqual(self.resultVerify(), '共有案件250条')
        ActionChains(self.driver).double_click(self.driver.find_element_by_xpath(searchBatchNo_loc)).perform()
        self.driver.find_element_by_xpath(searchBatchNo_loc).send_keys('QA测试')
        self.driver.find_element_by_xpath(searchBatchNo_loc).send_keys(Keys.ENTER)
        self.driver.find_element_by_xpath(searchBatchNo_loc).send_keys('QA测试1')
        self.searchBtn()
        time.sleep(5)
        self.assertEqual(self.resultVerify(), '共有案件1000条')
        # 搜索无结果
        ActionChains(self.driver).double_click(self.driver.find_element_by_xpath(searchBatchNo_loc)).perform()
        self.driver.find_element_by_xpath(searchBatchNo_loc).send_keys('aaa')
        self.searchBtn()
        time.sleep(1)
        self.assertEqual(self.resultVerify(), '共有案件0条')

    # 搜索证件号
    def test_searchIdCardNo(self):
        self.__myCaseEnterance()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(searchIdCard_loc).send_keys('622621201708080317')
        self.searchBtn()
        time.sleep(3)
        self.assertEqual(self.resultVerify(), '共有案件1条')
        ActionChains(self.driver).double_click(self.driver.find_element_by_xpath(searchIdCard_loc)).perform()
        self.driver.find_element_by_xpath(searchIdCard_loc).send_keys('622621201708080256')
        self.driver.find_element_by_xpath(searchIdCard_loc).send_keys(Keys.ENTER)
        self.driver.find_element_by_xpath(searchIdCard_loc).send_keys('622621201708080478')
        self.searchBtn()
        time.sleep(3)
        self.assertEqual(self.resultVerify(), '共有案件2条')
        # 搜索无结果
        ActionChains(self.driver).double_click(self.driver.find_element_by_xpath(searchIdCard_loc)).perform()
        self.driver.find_element_by_xpath(searchIdCard_loc).send_keys('aaa')
        self.searchBtn()
        time.sleep(1)
        self.assertEqual(self.resultVerify(), '共有案件0条')

    # 清空
    def test_clear(self):
        self.__myCaseEnterance()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(searchIdCard_loc).send_keys('622621201708080256')
        self.driver.find_element_by_xpath(searchIdCard_loc).send_keys(Keys.ENTER)
        self.driver.find_element_by_xpath(searchIdCard_loc).send_keys('622621201708080478')
        self.searchBtn()
        time.sleep(2)
        self.assertEqual(self.resultVerify(), '共有案件2条')
        self.driver.find_element_by_xpath(searchClearBtn_loc).click()
        self.searchBtn()
        time.sleep(2)
        self.assertEqual(self.resultVerify(), '共有案件1000条')

    # 更改催收状态
    def test_changeCollectionStatus(self):
        self.__myCaseEnterance()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(searchSelectCase_loc).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(updateStatusBtn_loc).click()
        Select(self.driver.find_element_by_xpath(updateStatusSelect_loc)).select_by_visible_text('留案')
        self.driver.find_element_by_xpath(updateStatusOKBtn_loc).click()
        time.sleep(3)
        self.assertEqual(self.driver.find_element_by_xpath(updateStatusVerify_loc).text, '留案')
        self.driver.find_element_by_xpath(searchSelectCase_loc).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(updateStatusBtn_loc).click()
        Select(self.driver.find_element_by_xpath(updateStatusSelect_loc)).select_by_visible_text('新案')
        self.driver.find_element_by_xpath(updateStatusOKBtn_loc).click()
        time.sleep(3)
        self.assertEqual(self.driver.find_element_by_xpath(updateStatusVerify_loc).text, '新案')

    # 翻页
    def test_paging(self):
        self.__myCaseEnterance()
        self.driver.find_element_by_xpath(click_current_page).click()
        # 滚动页面至指定的位置
        js = "var q=document.body.scrollTop=2000"
        self.driver.execute_script(js)
        self.driver.find_element_by_xpath(next_button).click()
        self.assertEqual(self.secondPage_verify(), '张0839')
        time.sleep(1)
        js = "var q=document.body.scrollTop=2000"
        self.driver.execute_script(js)
        self.driver.find_element_by_xpath(previous_button).click()
        self.assertEqual(self.myCaseList_verify(), '张0757')
