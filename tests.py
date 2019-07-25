import unittest
from format_price import format_price


class TestFormatPrice(unittest.TestCase):

    def test_format_price_short_str(self):
        self.assertEqual(format_price('0.0049'), '0')
        self.assertEqual(format_price('3245.0000001'), '3 245')
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
        self.assertEqual(format_price(3000), '3 000')
        self.assertEqual(format_price(10564), '10 564')
        self.assertEqual(format_price(623401), '623 401')

    def test_format_price_float(self):
        self.assertEqual(format_price(3245.000001), '3 245')
        self.assertEqual(format_price(3245.678901), '3 245.68')
        self.assertEqual(format_price(3245.670001), '3 245.67')
        self.assertEqual(format_price(1111.978901), '1 111.98')
        self.assertEqual(format_price(0.0049), '0')
        self.assertEqual(format_price(1234.9), '1 234.90')
        self.assertEqual(format_price(3000.00), '3 000')
        self.assertEqual(format_price(10564.113), '10 564.11')
        self.assertEqual(format_price(623401.7867), '623 401.79')

    def test_format_price_sep(self):
        self.assertEqual(format_price('1234,900'), None)
        self.assertEqual(format_price('1234|900'), None)
        self.assertEqual(format_price('1234;900'), None)
        self.assertEqual(format_price('1234/900'), None)
        self.assertEqual(format_price('1234:900'), None)

    def test_format_price_func(self):
        def func():
            ...
        self.assertEqual(format_price(func), None)

    def test_format_price_none(self):
        self.assertEqual(format_price(None), None)

    def test_format_price_bool(self):
        self.assertEqual(format_price(True), None)

if __name__ == '__main__':
    unittest.main()
