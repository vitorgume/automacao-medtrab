from src.models.automacao_model import AutomacaoModel
from src.config.browser_maneger import BrowserManeger

from src.dataprovider.automacao_dataprovider import AutomacaoDataProvider

class AutomacaoService:

    def criar_integracao(self, model: AutomacaoModel):
        browser = BrowserManeger(headless=False)
        driver = browser.get_driver()

        automacao_data_provider = AutomacaoDataProvider(driver)

        link_conversa = ""

        try:

            link_conversa = automacao_data_provider.encontrar_conversa(model.telefone)

        except Exception:
            pass
        finally:
            try:
                browser.close()
            except Exception:
                pass
            try:
                browser.driver.quit()
            except Exception:
                pass

        return link_conversa



