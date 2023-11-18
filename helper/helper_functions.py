from enum import Enum
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options

MAIN_ICON_BAR_PATH = "(//android.widget.ImageView[@resource-id='com.getmimo:id/navigation_bar_item_icon_view'])"
MIMO_ID_PATH = "com.getmimo:id/"
IP_SERVER = "http://127.0.0.1:4723"


class ReturnCode(Enum):
    STATUS_OK = 0
    STATUS_INVALID = -1
    STATUS_ERROR = -2


def validate_str(name: str) -> ReturnCode:
    if not isinstance(name, str) or len(name.strip()) == 0 or name is None:
        return ReturnCode.STATUS_INVALID
    else:
        return ReturnCode.STATUS_OK


def validate_number(number: int) -> bool:
    if isinstance(number, int) and number > 0:
        return True
    else:
        return False


def is_ok(status: ReturnCode) -> bool:
    return status == ReturnCode.STATUS_OK


@pytest.fixture
def fixture():
    """
    Fixture para todos os testes da pagina PIM.
    Passos: Inicia o driver, acessa a pagina de login, executa o login e visita a pagina PIM.
    Retorna o pageObject de PIM. Após a execucao do teste, executa driver.quit como tierDown do teste.
    """

    caps = dict()
    caps["platformName"] = "Android"
    caps["appium:automationName"] = "UiAutomator2"
    caps["appium:appPackage"] = "com.getmimo"
    caps["appium:appActivity"] = "com.getmimo.ui.main.MainActivity"
    caps["appium:ensureWebviewsHavePages"] = True
    caps["appium:nativeWebScreenshot"] = True
    caps["appium:newCommandTimeout"] = 3600
    caps["appium:connectHardwareKeyboard"] = True

    options = UiAutomator2Options()
    options.load_capabilities(caps)
    driver = webdriver.Remote(IP_SERVER, options=options)
    yield driver
    # teardown
    # driver.quit()
