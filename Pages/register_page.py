from Commom.base import Base
from selenium.webdriver.common.by import By


class RegisterPage(Base):

    email_loc = (By.ID, "id_email")
    password_loc = (By.ID, "id_password")
    submit_btn_loc = (By.ID, 'jsEmailRegBtn')
    #注册成功文本定位
    success_loc = (By.CSS_SELECTOR, "body > h1")

    def send_email(self, text):
        self.send(self.email_loc, text)

    def send_password(self, text):
        self.send(self.password_loc, text)

    def click_submit(self):
        self.click(self.submit_btn_loc)

    def get_success_text(self):
        return self.get_text(self.success_loc)

