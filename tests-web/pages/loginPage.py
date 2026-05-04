from selenium.webdriver.common.by import By
 
 
class LoginPage:
 
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
 
    def __init__(self, driver):
        self.driver = driver
 
    def preencher_usuario(self, username):
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)
 
    def preencher_senha(self, password):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)
 
    def clicar_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()
 
    def fazer_login(self, username, password):
        self.preencher_usuario(username)
        self.preencher_senha(password)
        self.clicar_login()
 
    def obter_mensagem_erro(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text