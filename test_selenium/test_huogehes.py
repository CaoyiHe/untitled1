from asyncio import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_Openweb:  # 打开浏览器
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://testerhome.com/")
        self.driver.implicitly_wait(5)  # 隐式等待

    def test_hogwarts(self):
        self.driver.find_element(By.LINK_TEXT, '社团').click()
        # sleep(1)
        #  尽量使用CSS的定位方法集，Link有可能会导致解析元素的时候出现异常
        WebDriverWait(self.driver, 10).until(expected_conditions)
        self.driver.find_element(By.PARTIAL_LINK_TEXT, '霍格沃兹测试学院').click()
        # self.driver.find_element(By.CSS_SELECTOR, '[data-name="霍格沃兹测试学院"]').click()
        # self.driver.find_element(By.CSS_SELECTOR, '[class="node"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '.topic:nth-child(1) .title a').click()  # 访问第一个帖子

    def web_tui(self):
        sleep(5)
        self.driver.quit()
