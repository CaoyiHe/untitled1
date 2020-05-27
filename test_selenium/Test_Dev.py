import select
from asyncio import sleep
from datetime import time
from lib2to3.pgen2 import driver
from telnetlib import EC
from threading import Thread
from tkinter.tix import Select

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait


class TimeUnit(object):
    pass


class Test_Advertising:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get(
            'http://advertisement.dev.q1op.com/#/ad/audience')
        self.driver.implicitly_wait(5)
        self.driver.set_window_size(2064, 1128)
        self.driver.find_element(By.NAME, 'userName').click()
        self.driver.find_element(By.NAME, 'userName').send_keys("hecaoyi")
        self.driver.find_element(By.NAME, 'password').click()
        self.driver.find_element(By.NAME, 'password').send_keys("Cgl110919.")
        self.driver.find_element(By.CSS_SELECTOR, '.el-button--primary').click()

    def teardown_method(self, method):
        pass
        # sleep(5)
        # self.driver.quit()

    def test_management(self):
        # self.driver.find_element(By.CSS_SELECTOR, '.menu-wrapper:nth-child(2)').click()
        # self.driver.find_element(By.CSS_SELECTOR, '.menu-wrapper:nth-child(2) a').click()
        self.driver.find_element(By.CSS_SELECTOR, '.el-range-input:nth-child(2)').click()
        self.driver.find_element(By.CSS_SELECTOR, '.el-range-input:nth-child(2)').send_keys('2020-01-01')
        self.driver.find_element(By.CSS_SELECTOR, '.el-range-input:nth-child(4)').send_keys('2020-04-20')
        self.driver.find_element(By.CSS_SELECTOR, '.el-range-input:nth-child(4)').send_keys(Keys.ENTER)
        # self.driver.find_element(By.CSS_SELECTOR, '.item__inline-block > .el-input > .el-input__inner').click()
        # self.driver.find_element(By.CSS_SELECTOR, '.item__inline-block > .el-input > .el-input__inner').send_keys(1)
        self.driver.find_element_by_css_selector("[placeholder='广告主账户或ID']").click()
        self.driver.find_element_by_css_selector("[placeholder='广告主账户或ID']").send_keys(1)
        self.driver.find_element_by_css_selector('[class="el-link el-link--primary is-underline"]').click()  # 点击高级筛选
        self.driver.find_element(By.CSS_SELECTOR, '[placeholder="广告商"]').click()
        # self.driver.find_element(By.CSS_SELECTOR, 'body>.el-select-dropdown .el-select-dropdown__item').click()
        # self.driver.find_element(By.CSS_SELECTOR, '[placeholder="代理商"]').click()
        # self.driver.find_elements(By.CSS_SELECTOR, 'body>.el-select-dropdown')[1].find_element(By.CSS_SELECTOR,
        #                                                                                        '.el-select-dropdown__item').click()
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul/li[1]/span').click()
        self.driver.find_element(By.CSS_SELECTOR, '.el-icon-search').click()
