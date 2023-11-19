from typing import Any
from helper.helper_functions import *
import logging


class BaseActivity:
    """
    Classe base para suportar pageObject.
    """

    def __init__(self, driver: Any = None):
        # Initialize WebDriver
        if driver:
            self._driver = driver
        else:
            raise ValueError(f' Driver nao encontrado.')
        self._base_url = ''
        self._driver.implicitly_wait(5)

    def visit(self, url: str):
        if not validate_str(url):
            logging.info("Url nao valida para visita.")
            raise ValueError
        return self._driver.get(url)

    # def wait_element(self, *locator):
    #     return WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((locator)))

    def click_btn(self, *locator):
        self._driver.find_element(*locator).click()
