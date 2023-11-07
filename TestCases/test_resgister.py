from Pages.register_page import RegisterPage


class TestRegister():
    def test_register_success(self, driver, base_url):
        '''测试注册成功案例'''
        # 1、打开浏览器
        register = RegisterPage(driver, base_url)
        register.open("/users/register/")
        # 2、输入邮箱和密码
        register.send_email("ww654321@qq.com")
        register.send_password("123456")
        # 3、点击登录
        register.click_submit()
        # 4、检测是否登录成功
        assert register.get_success_text() == "尊敬的用户，您好，账户已激活成功！"

    def test_register_failed(self, driver, base_url):
        '''测试注册成功案例'''
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
