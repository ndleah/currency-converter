import unittest
from currency import check_valid_currency, extract_api_result, Currency


class TestValidCurrency(unittest.TestCase):
    def test_check_valid_currency_true(self):
        true_currency = "AUD"
        self.assertEqual(check_valid_currency(true_currency), True)
    
    def test_check_valid_currency_false(self):   
        false_currency = "WKD"
        self.assertEqual(check_valid_currency(false_currency), False)

class TestExtractApi(unittest.TestCase):
    def test_extract_api_result_1(self):
        from_currency = "USD"
        to_currency = "AUD"
        rate = 2.0
        date = "2021-11-20"
        amount = 1034
        reverse_rate = 0.5
        currency = Currency(from_currency, to_currency, amount, rate, None, date)
        currency.reverse_rate()

        self.assertEqual(currency.from_currency, from_currency)
        self.assertEqual(currency.to_currency, to_currency)
        self.assertEqual(currency.rate, rate)
        self.assertEqual(currency.date, date)
        self.assertEqual(currency.amount, amount)
        self.assertEqual(currency.inverse_rate, reverse_rate)

    def test_extract_api_result_2(self):
        test_data = {
            "amount": 1,
            "base": "EUR",
            "date": "2021-09-09",
            "rates": {
                "USD": 4.0
            }
        }
        actual_currency = extract_api_result(test_data)

        self.assertEqual(actual_currency.from_currency, "EUR")
        self.assertEqual(actual_currency.to_currency, "USD")
        self.assertEqual(actual_currency.rate, 4.0)
        self.assertEqual(actual_currency.date, "2021-09-09")
        self.assertEqual(actual_currency.amount, 1)
        self.assertEqual(actual_currency.inverse_rate, 0.25)


if __name__ == '__main__':
    unittest.main(exit=False)
