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
        self._streak_header = "//android.widget.TextView[ @text=\"Activity\"]"
        self._course = "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[5]/android.widget.Button"
        self._course_settings = "//android.widget.ImageView[@content-desc=\"Change path\"]"
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

    def get_streak_header(self) -> str:
        header = self._driver.find_element(by=AppiumBy.XPATH, value=self._streak_header)
        return header.text

    def click_course_button(self):
        self.click_btn(AppiumBy.XPATH, self._course)

    def click_course_settings_button(self):
        self.click_btn(AppiumBy.XPATH, self._course_settings)

    def get_select_path_header(self):
        title_alt_course = self._driver.find_element(by=AppiumBy.XPATH,
                                                     value='//android.widget.TextView[@text="Select Path"]')
        return title_alt_course.text

    def get_language_header(self):
        path = "//android.widget.TextView[@text=\"Languages\"]"
        language = self._driver.find_element(by=AppiumBy.XPATH,
                                             value=path)
        return language.text

    def get_career_header(self):
        path = "//android.widget.TextView[@text=\"Career Paths\"]"
        career = self._driver.find_element(by=AppiumBy.XPATH,
                                           value=path)
        return career.text
