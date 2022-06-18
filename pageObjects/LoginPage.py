import time
from selenium.webdriver.common.by import By


class LoginPage:
    textBox_username_id = "Email"
    textBox_password_id = "Password"
    button_login_xpath = '//button[@class="button-1 login-button"]'
    link_logout_LinkText = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element(By.ID, self.textBox_username_id).clear()
        time.sleep(2)
        self.driver.find_element(By.ID, self.textBox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textBox_password_id).clear()
        time.sleep(2)
        self.driver.find_element(By.ID, self.textBox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_LinkText).click()
