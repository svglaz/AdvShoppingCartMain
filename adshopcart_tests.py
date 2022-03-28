import unittest
import adshopcart_locators as locators
import adshopcart_methods as methods


class AddShopCartPositiveTestCases(unittest.TestCase):

    @staticmethod  # signal to Unittest that this is a function inside class (vs @classmethod)
    def test_setup_teardown():
        methods.setUp()
        methods.sign_up()
        methods.log_out()
        methods.log_in()
        methods.check_full_name()
        methods.log_out()
        methods.log_in()
        methods.check_orders()
        methods.log_out()
        methods.log_in()
        methods.delete_test_account()
        methods.log_in()
        methods.tearDown()


