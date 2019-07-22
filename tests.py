import unittest
from format_price import format_price


class TestFormatPrice(unittest.TestCase):

    def test_format_price(self):
        self.assertEqual(format_price('3245.000000'), '3 245')
        self.assertEqual(format_price('33245.000000'), '33 245')
        self.assertEqual(format_price('333245.000000'), '333 245')
        self.assertEqual(format_price('3333245.000000'), '3 333 245')

        self.assertEqual(format_price('3245.500000'), '3 245.50')
        self.assertEqual(format_price('3245.53450000'), '3 245.53')
        self.assertEqual(format_price('3333245.53450000'), '3 333 245.53')

        self.assertEqual(format_price(1234), '1 234')
        self.assertEqual(format_price(1234.900), '1 234.90')


if __name__ == '__main__':
    unittest.main()
