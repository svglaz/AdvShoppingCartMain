import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys
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
    if driver.current_url == locators.adv_shop_cart_url and driver.title == locators.adv_shop_cart_home_page_title:
        print(f'{locators.app} website launched successfully!')
        print(f'We are on {locators.app} Homepage URL: {driver.current_url}, Homepage title: {driver.title}')
        sleep(0.25)
    else:
        print(f'{locators.app} did not launch. Check your code or application!')
        print(f'Current URL: {driver.current_url}, Page title: {driver.title}')
        # driver.close()
        # driver.quit()


def sign_up():
    print('---------------------------- ~*~ ----------------------------------')
    driver.find_element(By.ID, 'menuUser').click()
    sleep(2.0)
    driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
    sleep(1.0)

    # Validate we are on 'Create account' page
    assert driver.current_url == locators.adv_create_account_page_url
    print(f'We are on Create account page - Page URL: {driver.current_url}')

    driver.find_element(By.NAME, 'usernameRegisterPage').send_keys(locators.new_username)
    sleep(0.25)
    driver.find_element(By.NAME, 'emailRegisterPage').send_keys(locators.email)
    sleep(0.25)
    driver.find_element(By.NAME, 'passwordRegisterPage').send_keys(locators.new_password)
    sleep(0.25)
    driver.find_element(By.NAME, 'confirm_passwordRegisterPage').send_keys(locators.new_password)
    sleep(0.25)

    driver.find_element(By.NAME, 'first_nameRegisterPage').send_keys(locators.first_name)
    sleep(0.25)
    driver.find_element(By.NAME, 'last_nameRegisterPage').send_keys(locators.last_name)
    sleep(0.25)
    driver.find_element(By.NAME, 'phone_numberRegisterPage').send_keys(locators.phone)
    sleep(0.25)

    Select(driver.find_element(By.XPATH, '//select[@name="countryListboxRegisterPage"]')).select_by_visible_text(locators.country)
    sleep(0.25)
    driver.find_element(By.XPATH, '//input[@name="cityRegisterPage"]').send_keys(locators.city)
    sleep(0.25)
    driver.find_element(By.XPATH, '//input[@name="addressRegisterPage"]').send_keys(locators.address)
    sleep(0.25)
    driver.find_element(By.XPATH, '//input[@name="state_/_province_/_regionRegisterPage"]').send_keys(locators.state)
    sleep(0.25)
    driver.find_element(By.XPATH, '//input[@name="postal_codeRegisterPage"]').send_keys(locators.postal_code)
    sleep(0.25)

    driver.find_element(By.XPATH, '//input[@name="i_agree"]').click()
    sleep(0.25)

    driver.find_element(By.ID, 'register_btnundefined').click()
    sleep(0.25)

    # validate signUp successful
    if driver.find_element(By.LINK_TEXT, locators.new_username).is_displayed():
        print(f'New user {locators.full_name} is registered.')
        print(f'Username: {locators.new_username}, Password: {locators.new_password}')
    else:
        print(f'New user is not registered. Please, try again.')


def log_in():
    print('---------------------------- ~*~ -------------------------------')
    if driver.current_url == locators.adv_shop_cart_url:
        driver.find_element(By.ID, 'menuUser').click()
        sleep(0.5)
        driver.find_element(By.NAME, 'username').send_keys(locators.new_username)
        sleep(0.25)
        driver.find_element(By.NAME, 'password').send_keys(locators.new_password)
        sleep(0.25)
        driver.find_element(By.ID, 'sign_in_btnundefined').click()
        sleep(0.25)

        # validate login successful
        if driver.current_url == locators.adv_shop_cart_url:
            try:
                assert driver.find_element(By.LINK_TEXT, locators.new_username).is_displayed()
                print(f'Login is successful. Username: {locators.new_username}')
                sleep(0.25)
            except NoSuchElementException as nsa:
                if driver.find_element(By.ID, 'signInResultMessage').is_displayed():
                    print(f'User is not found. Test passed.')
                else:
                    print(f'Login is not successful. Check your code or website and try again. ')


def check_full_name():
    print('---------------------------- ~*~ ----------------------------------')
    if driver.current_url == locators.adv_shop_cart_url:
        driver.find_element(By.LINK_TEXT, locators.new_username).click()
        sleep(0.5)
        driver.find_element(By.XPATH, '//*[@id="menuUserLink"]/div[1]/label[contains(text(), "My account")]').click()
        sleep(1.0)
        if driver.current_url == locators.adv_myAccount_page_url:
            print(f'We are on MY ACCOUNT page.')
            try:
                assert driver.find_element(By.XPATH, f'//label[contains(., "{locators.full_name}")]').is_displayed()
                print(f'Full name is displayed on MY ACCOUNT page. Full name: {locators.full_name}')
            except NoSuchElementException as nsa:
                print(f'Full name is not displayed on MY ACCOUNT page.')


def check_orders():
    print('---------------------------- ~*~ ----------------------------------')
    if driver.current_url == locators.adv_shop_cart_url:
        driver.find_element(By.LINK_TEXT, locators.new_username).click()
        sleep(0.5)
        driver.find_element(By.XPATH, '//*[@id="menuUserLink"]/div[1]/label[contains(text(), "My orders")]').click()
        sleep(0.5)
        if driver.current_url == locators.adv_MyOrders_page_url:
            print(f'We are on MY ORDERS page.')
            try:
                assert driver.find_element(By.XPATH, f'//label[contains(., " - No orders - ")]').is_displayed()
                print(f'"No orders" is displayed on MY ORDERS page')
                sleep(0.25)
            except NoSuchElementException as nsa:
                print(f'"No orders" is not displayed on MY ORDERS page.')


def log_out():
    print('---------------------------- ~*~ ----------------------------------')
    #driver.find_element(By.LINK_TEXT, locators.new_username).click()
    driver.find_element(By.ID, 'menuUser').click()
    sleep(1.0)
    #driver.find_element(By.XPATH, '//label[@ng-click="signOut($event)"]').click()
    driver.find_element(By.XPATH, '//*[@id="menuUserLink"]/div[1]/label[contains(text(), "Sign out")]').click()
    sleep(1.0)

    # validate logout successful
    if driver.current_url == locators.adv_shop_cart_url:
        driver.implicitly_wait(3)
        try:
            assert driver.find_element(By.LINK_TEXT, locators.new_username).is_displayed()
        except NoSuchElementException as nsa:
            print(f'Logout is successful. {datetime.datetime.now()}')


def delete_test_account():
    if driver.current_url == locators.adv_shop_cart_url:
        driver.find_element(By.LINK_TEXT, locators.new_username).click()
        sleep(0.5)
        driver.find_element(By.XPATH, '//*[@id="menuUserLink"]/div[1]/label[contains(text(), "My account")]').click()
        sleep(1.5)
        if driver.current_url == locators.adv_myAccount_page_url:
            print(f'We are on MY ACCOUNT page.')
            driver.find_element(By.CLASS_NAME, 'deleteBtnText').click()
            sleep(2.0)
            #driver.find_element(By.CLASS_NAME, 'deletePopupBtn deleteRed').click()
            driver.find_element(By.XPATH, '//div[@data-ng-click="deleteAccountConfirmed()"]').click()
            sleep(10.0)
            if driver.current_url == locators.adv_shop_cart_url:
                driver.implicitly_wait(3)
                try:
                    assert driver.find_element(By.LINK_TEXT, locators.new_username).is_displayed()
                except NoSuchElementException as nsa:
                    print(f'Account is successfully deleted.')


def tearDown():
    if driver is not None:
        print(f'----------------------- ~*~ ------------------------------')
        print(f'The test is completed at: {datetime.datetime.now()}')
        sleep(0.5)
        driver.close()
        driver.quit()


# setUp()
# sign_up()
# log_out()
# log_in()
# check_full_name()
# log_out()
# log_in()
# check_orders()
# log_out()
# log_in()
# delete_test_account()
# log_in()
# tearDown()
