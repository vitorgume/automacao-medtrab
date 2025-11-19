from selenium.webdriver.support.ui import WebDriverWait
from src.config.settings import PASSWORD_PLUG_CHAT
from src.config.settings import USER_PLUG_CHAT
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

user_plug_chat = USER_PLUG_CHAT
password_plug_chat = PASSWORD_PLUG_CHAT


class AutomacaoDataProvider:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 12)

    def encontrar_conversa(self, telefone: str):
        self.driver.get("https://plugchat.com.br/chat/e97487a6-5ccf-4787-b44a-80d8074662f4/login")
        email_input = self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "input[placeholder='Operador']")
            )
        )

        email_input.clear()
        email_input.send_keys(user_plug_chat)

        senha_input = self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "input[placeholder='Senha']")
            )
        )

        senha_input.clear()
        senha_input.send_keys(password_plug_chat)

        botao_continuar = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[.//span[normalize-space()='Continuar']]")
            )
        )

        botao_continuar.click()

        campo_busca = self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#search-chats")
            )
        )

        campo_busca.clear()
        campo_busca.send_keys(telefone)

        link_contato = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//a[.//div[@id='chat_{telefone}']]")
            )
        )

        link_contato.click()

        url_atual = self.driver.current_url

        return url_atual
