import unittest
from format_price import format_price


class TestFormatPrice(unittest.TestCase):

    def test_format_price_short_str(self):
        self.assertEqual(format_price('3245.000000'), '3 245')
        self.assertEqual(format_price('33245.000000'), '33 245')
        self.assertEqual(format_price('333245.000000'), '333 245')

    def test_format_price_long_str(self):
        self.assertEqual(format_price('3333245.000000'), '3 333 245')
        self.assertEqual(format_price('3245.500000'), '3 245.50')
        self.assertEqual(format_price('3245.53450000'), '3 245.53')
        self.assertEqual(format_price('3333245.53450000'), '3 333 245.53')

    def test_format_price_list(self):
        self.assertEqual(format_price([]), None)

    def test_format_price_dict(self):
        self.assertEqual(format_price({}), None)

    def test_format_price_int(self):
        self.assertEqual(format_price(1234), '1 234')
        self.assertEqual(format_price(1234.900), '1 234.90')

    def test_format_price_func(self):
        self.assertEqual(format_price('1234,900'), None)
        self.assertEqual(format_price('1234|900'), None)
        self.assertEqual(format_price('1234/900'), None)

    def test_format_price_sep(self):
        def func():
            ...
        self.assertEqual(format_price(func), None)


if __name__ == '__main__':
    unittest.main()
