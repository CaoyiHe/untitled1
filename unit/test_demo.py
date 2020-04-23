import allure
import pytest
from unit.div import div


@pytest.mark.name  # 对用例进行分组，name是改组的名字
def test_div_chu():
    assert div(10, 2) == 5
    assert div(20, 2) == 10
    assert div(10000000, 1) == 10000000


@pytest.mark.name
@pytest.mark.parametrize("number1, number2, expect", [
    (10, 2, 5),
    (20, 2, 10),
    (100000, 1, 100000)
])
def test_div_dui(number1, number2, expect):
    assert div(number1, number2) == expect


@pytest.mark.abc
def test_():
    assert 123 == 123
    allure.attach.file('E:/timg.jpg', attachment_type=allure.attachment_type.JPG)


#  pytest --junitxml=unit/junit.xml --alluredir=unit/allure_results unit/  新建alluredir文件夹
#  allure serve unit/allure_results/  生成测试报告链接
