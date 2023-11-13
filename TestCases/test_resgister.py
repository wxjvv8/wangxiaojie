import pytest

from Pages.register_page import RegisterPage
import allure


class TestRegister():
    @pytest.fixture(autouse=True)
    def open(self, register):
        register.open("/users/register/")

    @allure.feature("注册页面")
    @allure.story("注册功能")
    @allure.title("测试注册成功案例")
    @allure.severity("blocker")
    def test_register_success(self, driver, base_url):
        '''测试注册成功案例'''
        # 1、打开浏览器
        with allure.step("1、打开浏览器"):
            register = RegisterPage(driver, base_url)
            register.open("/users/register/")
        # 2、输入邮箱和密码
        with allure.step("2、输入邮箱和密码"):
            register.send_email("ww654321@qq.com")
            register.send_password("123456")
        # 3、点击登录
        with allure.step("3、点击登录"):
            register.click_submit()
        # 4、检测是否登录成功
        with allure.step("4、检测是否登录成功"):
            assert register.get_success_text() == "尊敬的用户，您好，账户已激活成功！"

    @allure.title("测试注册失败案例")
    @allure.severity("blocker")
    def test_register_failed(self, driver, base_url):
        '''测试注册失败案例'''
        # 1、打开浏览器
        register = RegisterPage(driver, base_url)
        register.open("/users/register/")
        # 2、输入邮箱和密码
        register.send_email("ww654321@qq.com")
        register.send_password("123456")
        # 3、点击登录
        register.click_submit()
        # 4、检测是否登录成功
        assert register.get_success_text() == ""

    @allure.title("测试邮箱输入框显示正确")
    @allure.severity("normal")
    def test_email_input(self, driver, base_url):
        '''测试邮箱输入框显示'''
        # 1、打开浏览器
        register = RegisterPage(driver, base_url)
        register.open("/users/register/")
        # 2、输入邮箱和密码
        register.send_email("ww654321@qq.com")
        register.send_password("123456")
        # 3、获取输入框显示
        email_text = register.get_email_attr("value")
        # 4、检测显示是否正确
        assert email_text == "ww654321@qq.com"

    @allure.title("测试邮箱输入框清空功能正常")
    @allure.severity("normal")
    def test_email_input_clear(self, driver, base_url):
        '''测试邮箱输入框清空功能'''
        # 1、打开浏览器
        register = RegisterPage(driver, base_url)
        register.open("/users/register/")
        # 2、输入邮箱,然后清空
        register.send_email("1111")
        register.clear_email()
        # 3、获取输入框显示
        email_text = register.get_email_attr("value")
        # 4、检测显示是否正确
        assert email_text == ""

    @allure.title("测试密码输入框显示正确")
    # 没有加等级默认是normal级别
    def test_password_input(self, driver, base_url):
        '''测试密码输入框显示'''
        # 1、打开浏览器
        register = RegisterPage(driver, base_url)
        register.open("/users/register/")
        # 2、输入密码
        register.send_email("1111")
        register.clear_email()
        # 3、获取输入框显示
        password_type = register.get_password_attr("type")
        # 4、检测显示是否正确
        assert password_type == "password"

    @allure.title("测试密码输入框清空功能正常")
    # 没有加等级，默认是normal级别
    def test_password_input_clear(self, driver, base_url):
        '''测试密码输入框清空功能'''
        # 1、打开浏览器
        register = RegisterPage(driver, base_url)
        register.open("/users/register/")
        # 2、输入密码
        register.send_password("1111")
        # password_value = register.get_password_attr("value")
        # assert password_value == "1111"
        register.clear_password()
        # 3、获取输入框显示
        password_value = register.get_password_attr("value")
        # 4、检测显示是否正确
        assert password_value == ""

    @allure.title("测试回到首页按钮跳转正常")
    @allure.severity("minor")
    def test_backbtn_link(self, register, base_url):
        '''测试回到首页跳转是否正确'''
        # # 1、打开浏览器
        # register = RegisterPage(driver, base_url)
        # register_page.open("/users/register/")
        # 2、获取回到首页按钮的链接
        href_text = register.get_back_btn_attr("href")
        # 3、检测跳转是否正确
        assert href_text == base_url+"/"