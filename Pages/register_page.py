from Commom.base import Base
from selenium.webdriver.common.by import By


class RegisterPage(Base):

    email_loc = (By.ID, "id_email")
    password_loc = (By.ID, "id_password")
    submit_btn_loc = (By.ID, 'jsEmailRegBtn')
    back_btn_loc = (By.CLASS_NAME, "index-font")
    #注册成功文本定位
    success_loc = (By.CSS_SELECTOR, "body > h1")

    def send_email(self, text):
        self.send(self.email_loc, text)

    def clear_email(self):
        self.clear(self.email_loc)

    def get_email_attr(self, attr):
        return self.get_attr(self.email_loc, attr)

    def send_password(self, text):
        self.send(self.password_loc, text)

    def clear_password(self):
        self.clear(self.password_loc)

    def get_password_attr(self, attr):
        return self.get_attr(self.password_loc, attr)

    def click_submit(self):
        self.click(self.submit_btn_loc)

    def get_success_text(self):
        return self.get_text(self.success_loc)

    def get_back_btn_attr(self, attr):
        return self.get_attr(self.back_btn_loc, "href")
