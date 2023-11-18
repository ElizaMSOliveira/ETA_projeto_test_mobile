from .baseActivity import BaseActivity
from helper.helper_functions import *
from appium.webdriver.common.appiumby import AppiumBy


class Profile(BaseActivity):

    def __init__(self, driver):
        super().__init__(driver=driver)
        profile_icon = driver.find_element(by=AppiumBy.XPATH, value=f"{MAIN_ICON_BAR_PATH}[4]")
        profile_icon.click()


