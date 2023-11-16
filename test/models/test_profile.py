# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import pytest

IP_SERVER = "http://127.0.0.1:4723"
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

@pytest.fixture
def fixture():
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
    #teardown
    driver.quit()

def test_CT001_(fixture):
    driver = fixture
    el1 = driver.find_element(by=AppiumBy.XPATH,
                              value="(//android.widget.ImageView[@resource-id=\"com.getmimo:id/navigation_bar_item_icon_view\"])[4]")
    el1.click()
    el2 = driver.find_element(by=AppiumBy.ID, value="com.getmimo:id/cw_share_my_progress")
    el2.click()
    el3 = driver.find_element(by=AppiumBy.ID, value="com.getmimo:id/cw_share_my_progress")
    el3.click()

    driver.quit()
