import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_job:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get('https://testerhome.com/')

    def tui(self):
        time.sleep(5)
        self.driver.quit()

    def test_happy(self):

        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'MTSC2020 中国互联网测试开发大会议题征集').click()
        self.driver.find_element(By.CSS_SELECTOR, '.toc-container > .btn').click()
        self.driver.find_element(By.LINK_TEXT, '征集议题范围').click()

