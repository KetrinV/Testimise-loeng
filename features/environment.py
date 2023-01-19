from selenium import webdriver


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome('./chromedriver')
    context.driver.maximize_window