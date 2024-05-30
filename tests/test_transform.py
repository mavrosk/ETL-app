import unittest
from transform import Transformer

class TestTransformer(unittest.TestCase):
    def test_transform(self):
        data = {
            "timestamp": "2023-05-20",
            "rates": {
                "USD": 1.0,
                "EUR": 0.85,
                "GBP": 0.75
            }
        }
        transformed_data = Transformer.transform(data)
        self.assertEqual(len(transformed_data), 3)
        for entry in transformed_data:
            self.assertIn('currency_date', entry)
            self.assertIn('currency_symbol', entry)
            self.assertIn('currency_rate', entry)

if __name__ == '__main__':
    unittest.main()
