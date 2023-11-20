from activities.profile import Profile
from activities.learn import Learn
from activities.leaderboard import LeaderBoard
from helper.helper_functions import fixture
import time


def test_CT001_learn_glossary(fixture):
    driver = fixture
    learn = Learn(driver)
    learn.click_learn_button('Glossary')
    header_name = learn.get_glossary_header()
    assert header_name == "Glossary"


def test_CT002_learn_streak(fixture):
    driver = fixture
    learn = Learn(driver)
    learn.click_learn_button('Streak')
    header_name = learn.get_streak_header()
    assert header_name == "Activity"


def test_CT003_learn_path(fixture):
    driver = fixture
    expected_header = "Select Path"
    learn = Learn(driver)
    learn.click_course_button()
    time.sleep(2)
    learn.click_course_settings_button()
    time.sleep(2)
    header = learn.get_select_path_header()
    assert header == expected_header


def test_CT004_learn_settings_header(fixture):
    driver = fixture
    expected_header = "Select Path"
    learn = Learn(driver)
    learn.click_course_button()
    time.sleep(2)
    learn.click_course_settings_button()
    time.sleep(2)
    lang = learn.get_language_header()
    career = learn.get_career_header()
    assert lang == "Languages"
    assert career == "Career Paths"


def test_CT005_leaderboard(fixture):
    driver = fixture
    lb = LeaderBoard(driver)
    expected_league_name = "Wooden League"
    expected_header = "Leaderboard"
    expected_button = "START LESSON"
    league_name = lb.get_league_name()
    header_name = lb.get_leaderboard_header()
    button_msg = lb.get_start_button()
    assert league_name == expected_league_name
    assert header_name == expected_header
    assert button_msg == expected_button


def test_CT006_leaderboard(fixture):
    driver = fixture
    lb = LeaderBoard(driver)
    nld = lb.get_no_lessons_done()
    assert nld == "1 more lesson"


def test_CT007_profile_share(fixture):
    driver = fixture
    profile = Profile(driver)
    share = profile.get_share()
    assert share == "SHARE MY PROGRESS"


def test_CT008_profile_headers(fixture):
    driver = fixture
    profile = Profile(driver)
    friends = profile.get_friends_header()
    cert = profile.get_cert_header()
    assert friends == "Friends"
    assert cert == "Certificates"
