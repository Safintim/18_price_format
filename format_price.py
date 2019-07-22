import argparse


def main():
    parser = create_parser()
    namespace = parser.parse_args()
    print(format_price(namespace.price))


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('price', help='price value')
    return parser


def format_price(price):
    try:
        price = float(price)
    except ValueError:
        return None
    if int(price) == float(price):
        return '{:,}'.format(int(price)).replace(',', ' ')
    else:
        return '{:,.2f}'.format(price).replace(',', ' ')


if __name__ == '__main__':
    main()
