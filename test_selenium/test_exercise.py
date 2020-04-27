from asyncio import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_Open:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://testerhome.com/')
        self.driver.implicitly_wait(5)

    def open_tiezi(self):
        self.driver.find_element(By.CSS_SELECTOR, '.topic-21805 .title a').click()  # 访问置顶帖处第一个帖子
        self.driver.find_element(By.LINK_TEXT, '目录').click()
        self.driver.find_element(By.LINK_TEXT, '征集议题范围').click()

    def test_tui(self):
        pass
        # sleep(20)
        # self.driver.quit()
