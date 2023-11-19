from activities.profile import Profile
from activities.learn import Learn
from helper.helper_functions import fixture
from appium.webdriver.common.appiumby import AppiumBy

import time


# def test_CT001_(fixture):
#     driver = fixture
#     profile_page = Profile(driver)

# el1 = driver.find_element(by=AppiumBy.XPATH,
#                           value="(//android.widget.ImageView[@resource-id='com.getmimo:id/navigation_bar_item_icon_view'])[4]")
# el1.click()
# el2 = driver.find_element(by=AppiumBy.ID, value="com.getmimo:id/cw_share_my_progress")
# el2.click()
# el3 = driver.find_element(by=AppiumBy.ID, value="com.getmimo:id/cw_share_my_progress")
# el3.click()

# def test_CT001_(fixture):
#     driver = fixture
#     learn = Learn(driver)
#     learn.click_learn_button('glossario')


def test(fixture):
    driver = fixture
    learn = Learn(driver)
    learn.click_learn_button('Glossary')
    header_name = learn.get_glossary_header()
    assert header_name == "Glossary"
