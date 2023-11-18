from .baseActivity import BaseActivity
from helper.helper_functions import *
from appium.webdriver.common.appiumby import AppiumBy


class Learn(BaseActivity):
    def __init__(self, driver):
        """
        Classe PageObject para controlar a pagina de Learn do aplicativo.
        :param driver: objeto do driver que controlara as ações.
        """
        super().__init__(driver=driver)
        profile_icon = driver.find_element(by=AppiumBy.XPATH, value=f"{MAIN_ICON_BAR_PATH}[1]")
        profile_icon.click()
