from .baseActivity import BaseActivity
from helper.helper_functions import *
from appium.webdriver.common.appiumby import AppiumBy
import logging


class LeaderBoard(BaseActivity):
    def __init__(self, driver):
        """
        Classe PageObject para controlar a pagina de Learn do aplicativo.
        :param driver: objeto do driver que controlara as ações.
        """
        super().__init__(driver=driver)
        self._leader_boarder_header = "(//android.widget.TextView[@text=\"Leaderboard\"])[1]"
        self._start_lesson_button = "com.getmimo:id/btn_leaderboard_fragment_locked_jump_into_lesson"
        self._league_name_id = "com.getmimo:id/tv_leaderboard_results_league_label"
        leaderboard_icon = driver.find_element(by=AppiumBy.XPATH, value=f"{MAIN_ICON_BAR_PATH}[2]")
        leaderboard_icon.click()

    def get_leaderboard_header(self):
        header = self._driver.find_element(by=AppiumBy.XPATH, value=self._leader_boarder_header)
        return header.text

    def get_league_name(self):
        league = self._driver.find_element(by=AppiumBy.ID, value=self._league_name_id)
        return league.text

    def get_start_button(self):
        button = self._driver.find_element(by=AppiumBy.ID, value=self._start_lesson_button)
        return button.text

    def get_no_lessons_done(self):
        msg = self._driver.find_element(by=AppiumBy.ID, value="com.getmimo:id/tv_leaderboard_fragment_locked_header")
        return msg.text
