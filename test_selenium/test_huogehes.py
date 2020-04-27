from asyncio import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_Openweb:
    def setup_method(self):  # 打开浏览器
        self.driver = webdriver.Chrome()
        self.driver.get("https://testerhome.com/")
        self.driver.implicitly_wait(5)  # 隐式等待

    def test_hogwarts(self):
        self.driver.find_element(By.LINK_TEXT, '社团').click()
        # sleep(1)
        #  尽量使用CSS的定位方法集，Link有可能会导致解析元素的时候出现异常
        element = By.PARTIAL_LINK_TEXT, '霍格沃兹测试学院'
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(element))  # 显示等待，检测LINK是否能够点击
        self.driver.find_element(*element).click()
        # self.driver.find_element(By.CSS_SELECTOR, '[data-name="霍格沃兹测试学院"]').click()
        # self.driver.find_element(By.CSS_SELECTOR, '[class="node"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '.topic:nth-child(1) .title a').click()  # 访问第一个帖子

    #  多窗口与frame切换
    def test_frame(self):
        # self.driver.get('https://testerhome.com/topics/21805')
        self.driver.find_element(By.CSS_SELECTOR, '.topic:nth-child(1) .title a').click()
        self.driver.find_element(By.LINK_TEXT, '第六届中国互联网测试开发大会').click()
        self.driver.switch_to.window(self.driver.window_handles[1])  # 打开新窗口后，切换到新窗口
        self.driver.find_element(By.LINK_TEXT, '演讲申请').click()
        # print(self.driver.window_handles)  # 查看有多少窗口，从而找到对应的窗口进行切换
        WebDriverWait(self.driver, 10,
                      lambda X: len(self.driver.window_handles) > 1)  # 显示等待，窗口还没有切换完成时，页面元素还没有出现，不能进行操作
        print(self.driver.window_handles)
        self.driver.switch_to.window(self.driver.window_handles[2])
        self.driver.find_element(By.NAME, 'username').click()
        self.driver.find_element(By.NAME, 'username').send_keys(123)
        self.driver.find_element(By.NAME, 'title').send_keys(321)


