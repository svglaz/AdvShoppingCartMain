import unittest
import adshopcart_locators as locators
import adshopcart_methods as methods


class AddShopCartPositiveTestCases(unittest.TestCase):

    @staticmethod  # signal to Unittest that this is a function inside class (vs @classmethod)
    def test_create_new_user():
        methods.setUp()
        methods.sign_up()
        methods.check_homepage()
        methods.check_full_name()
        methods.check_orders()
        methods.log_out()
        methods.log_in()
        methods.delete_test_account()
        methods.log_in()
        methods.tearDown()


