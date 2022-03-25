import unittest
import adshopcart_locators as locators
import adshopcart_methods as methods


class AddShopCartPositiveTestCases(unittest.TestCase):

    @staticmethod  # signal to Unittest that this is a function inside class (vs @classmethod)
    def test_setup_teardown():
        methods.setUp()
        methods.tearDown()
