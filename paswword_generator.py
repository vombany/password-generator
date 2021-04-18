import string
import random
import argparse


def generate_password(length: int, use_punctuation: bool, use_digits: bool, use_uppercase: bool) -> str:
    symbols = string.ascii_lowercase
    if use_punctuation:
        symbols += string.punctuation
    if use_digits:
        symbols += string.digits
    if use_uppercase:
        symbols += string.ascii_uppercase
    result = random.choices(symbols, k=length)
    return ''.join(result)


parser = argparse.ArgumentParser()
parser.add_argument('-l', '--length', help='Length of the generated password', type=int, default=8)
parser.add_argument(
    '--use_punctuation', help='Indicates the need to use punctuation symbols', action='store_true', default=False
)
parser.add_argument(
    '--use_digits', help='Indicates the need to use digits', action='store_true', default=False
)
parser.add_argument(
    '--use_uppercase', help='Indicates the need to use uppercase symbols', action='store_true', default=False
)
args = parser.parse_args()


generated_password = generate_password(args.length, args.use_punctuation, args.use_digits, args.use_uppercase)
print(generated_password)
