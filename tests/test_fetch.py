import unittest
from fetch import Fetcher

class TestFetcher(unittest.TestCase):
    def test_fetch_data(self):
        fetcher = Fetcher()
        data = fetcher.fetch_data('2023-05-20')
        self.assertIn('rates', data)
        self.assertIn('EUR', data['rates'])

if __name__ == '__main__':
    unittest.main()
