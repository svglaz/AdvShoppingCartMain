import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import adshopcart_locators as locators

s = Service(executable_path='../chromedriver.exe')
driver = webdriver.Chrome(service=s)


def setUp():
    print(f'Launch {locators.app} App')
    print(f'---------------------------- ~*~ ---------------------------------')
    print(f'The test is started at: {datetime.datetime.now()}')

    # make browser full screen
    driver.maximize_window()

    # give browser up to 30 seconds to respond
    driver.implicitly_wait(30)

    # navigate to Moodle App website
    driver.get(locators.adv_shop_cart_url)

    # check that Moodle URL and the home page title are as expected
    if driver.current_url == locators.adv_shop_cart_url and locators.adv_shop_cart_home_page_title in driver.title:
        print(f'We are at Advantage Shopping homepage -- {driver.current_url}')
        print(f'{locators.app} Homepage title: {driver.title}')
        sleep(0.25)
    else:
        print(f'{locators.app} did not launch. Check your code or application!')
        print(f'Current URL: {driver.current_url}, Page title: {driver.title}')
        # driver.close()
        # driver.quit()


def tearDown():
    if driver is not None:
        print(f'----------------------- ~*~ ------------------------------')
        print(f'The test is completed at: {datetime.datetime.now()}')
        sleep(0.5)
        driver.close()
        driver.quit()

# setUp()
# tearDown()
