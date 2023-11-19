from .baseActivity import BaseActivity
from helper.helper_functions import *
from appium.webdriver.common.appiumby import AppiumBy
import logging


class Learn(BaseActivity):
    def __init__(self, driver):
        """
        Classe PageObject para controlar a pagina de Learn do aplicativo.
        :param driver: objeto do driver que controlara as ações.
        """
        super().__init__(driver=driver)
        self._glossary_header = "//android.widget.TextView[@text=\"Glossary\"]"
        learn_icon = driver.find_element(by=AppiumBy.XPATH, value=f"{MAIN_ICON_BAR_PATH}[1]")
        learn_icon.click()

    def click_learn_button(self, nome):
        """
        Clica no botao especificado pelo nome na activity de aprendizado.
        """
        accepted_buttons = ['Glossary', 'Store', 'Streak']
        if not validate_str(nome) or nome not in accepted_buttons:
            logging.info(f"Botao invalido: {nome}.")
            raise ValueError
        else:
            button_path = f"//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[{accepted_buttons.index(nome) + 2}]/android.widget.Button"
            self.click_btn(AppiumBy.XPATH, button_path)

    def get_glossary_header(self) -> str:
        header = self._driver.find_element(by=AppiumBy.XPATH, value=self._glossary_header)
        return header.text
