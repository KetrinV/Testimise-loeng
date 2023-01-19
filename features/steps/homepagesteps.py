from behave import when, then, given 
from selenium.webdriver.common.by import by
import time

URL = "https://www.ametikool.ee/"

@given("I open URL")
@when("I open URL")
def openURL(context):
    context.driver.get("https://www.ametikool.ee/")

@then("I check homepage is opened")
def checkURL(context):
    driver = context.driver
    assert driver.current_url == URL

    menuAvaleht = driver.find_element(By.CSS_SELECTOR, "body > div.wrapper > header.main.sm-hide > div.header-nav > div > div > div > ul > li.active > a")
    assert menuAvaleht.is_displayed()
    assert menuAvaleht.text == "AVALEHT"

@when ("I search for (keyword)")
def search(contex, keyword):
    driver = context.driver
    searchField = driver.find_element(By.CSS_SELECTOR, "body > div.wrapper > header.main.sm-hide > div.highlight-bg-1 > div > div > div.col-6.flex-right > ul > li:nth-child(4) > form > div > input[type=text]")
    searchField.send_keys(keyword)
    searchButton = driver.find_element(By.CSS_SELECTOR, "body > div.wrapper > header.main.sm-hide > div.highlight-bg-1 > div > div > div.col-6.flex-right > ul > li:nth-child(4) > form > div > button")
    searchButton.click()
    time.sleep(2)

@then("testing is found")
def keywordisFound(context, keyword):
    driver = context.driver
    keywordFound = driver.find_element(By, CSS_SELECTOR, "#all > h2 > span.sm-hide")
    assert keyword in keywordFound