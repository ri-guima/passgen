from argparse import ArgumentParser

from main import generate_password


if __name__ == '__main__':
    parser = ArgumentParser(description='Password Generator')
    parser.add_argument('-l', '--length', type=int,
                        default=8, help='Password length')
    parser.add_argument('-d', '--digits',
                        help='With digits', action='store_true')
    parser.add_argument('-s', '--special',
                        help='With special characters', action='store_true')
    args = parser.parse_args()
    generate_password(args.length, digits=args.digits, special=args.special)
