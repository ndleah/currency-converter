import unittest
from api import call_api, format_currencies_url, get_currencies, format_latest_url, _HOST_, _LATEST_, _CURRENCIES_


class TestFormatUrl(unittest.TestCase):
    def test_format_latest_url(self):
        test_latest_url = "https://api.frankfurter.app/latest?from=GBP&to=AUD"
        test_from_currency = "GBP"
        test_to_currency = "AUD"
        self.assertEqual(format_latest_url(test_from_currency, test_to_currency), test_latest_url)
    
    
    def test_format_currencies_url(self):
        test_format_currencies_url = "https://api.frankfurter.app/currencies"
        self.assertEqual(format_currencies_url(), test_format_currencies_url)


class TestAPI(unittest.TestCase):
    def test_call_api(self):
        test_api_url = "https://api.frankfurter.app/currencies"
        test_expected_status_code = 200
        self.assertEqual(call_api(test_api_url).status_code, test_expected_status_code)

if __name__ == '__main__':
    unittest.main(exit=False)