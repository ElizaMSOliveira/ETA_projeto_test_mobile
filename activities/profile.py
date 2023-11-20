from .baseActivity import BaseActivity
from helper.helper_functions import *
from appium.webdriver.common.appiumby import AppiumBy


class Profile(BaseActivity):

    def __init__(self, driver):
        super().__init__(driver=driver)
        self._share_progress = "com.getmimo:id/cw_share_my_progress"
        self._friends_header = "com.getmimo:id/tv_friends_title"
        self._certificates_header = "//android.widget.TextView[@text=\"Certificates\"]"
        profile_icon = driver.find_element(by=AppiumBy.XPATH, value=f"{MAIN_ICON_BAR_PATH}[4]")
        profile_icon.click()

    def get_cert_header(self):
        header = self._driver.find_element(by=AppiumBy.XPATH, value=self._certificates_header)
        return header.text
    def get_friends_header(self):
        header = self._driver.find_element(by=AppiumBy.ID, value=self._friends_header)
        return header.text

    def get_share(self):
        header = self._driver.find_element(by=AppiumBy.ID, value=self._share_progress)
        return header.text
