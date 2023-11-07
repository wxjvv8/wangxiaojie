
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException

'''封装selenium基本操作'''
class LocatorTypeError(Exception):
    pass
class ElementNotFound(Exception):
    pass


class Base():
    """基于原生的selenium进行二次封装"""
    def __init__(self, driver:webdriver.chrome, base_url, timeout = 10, t = 0.5):
        self.driver = driver
        self.timeout = timeout
        self.t = t
        self.base_url = base_url

    def open(self, url):
        """跟get方法一样，这里支持相对路径yrl"""
        if "http" in url:
            self.driver.get(url)
        self.driver.get(self.base_url+url)

    def find(self, locator):
        """locator必须是元祖类型：loc=（id, value）定位到元素，返回元素对象，没有定位到，Timeout异常"""
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元祖类型：loc=（id, value）")
        else:
            print("正在定位元素信息：定位方式->%s, value值->%s" %(locator[0], locator[1]))
            try:
                ele = WebDriverWait(self.driver, self.timeout,self.t).until(EC.presence_of_element_located(locator))
                return ele
            except TimeoutException as msg:
                raise ElementNotFound("定位元素出现超时！！！")

    def finds(self, locator):
        """locator必须是元祖类型：loc=（id, value）定位到元素，返回元素对象，没有定位到，Timeout异常"""
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元祖类型：loc=（id, value）")
        else:
            print("正在定位元素信息：定位方式->%s, value值->%s" %(locator[0], locator[1]))
            try:
                ele = WebDriverWait(self.driver, self.timeout,self.t).until(EC.presence_of_all_elements_located(locator))
                return ele
            except TimeoutException as msg:
                raise ElementNotFound("定位元素出现超时！！！")

    def send(self, loc, text):
        ele = self.find(loc)
        if ele.is_displayed():
            ele.send_keys(text)
        else:
            raise ElementNotVisibleException("元素不可见，或定位不唯一，无法定位到元素，请检查定位信息是否正确！")

    def click(self, loc):
        ele = self.find(loc)
        if ele.is_displayed():
            ele.click()
        else:
            raise ElementNotVisibleException("元素不可见，或定位不唯一，无法定位到元素，请检查定位信息是否正确！")

    def clear(self, loc):
        ele = self.find(loc)
        if ele.is_displayed():
            ele.clear()
        else:
            raise ElementNotVisibleException("元素不可见，或定位不唯一，无法定位到元素，请检查定位信息是否正确！")

    def get_text(self, loc):
        try:
            ele = self.find(loc)
            if ele.is_displayed():
                print("获取到text：", ele.text)
                return ele.text
            else:
                return ""
        except:
            return ""

