class color:
    purple = '\033[95m'
    red = '\033[91m'
    yellow = '\033[93m'
    blue = '\033[94m'
    cyan = '\033[96m'
    bold = '\033[1m'
    underline = '\033[4m'
    end = '\033[0m'
    green = '\033[92m'

print(f'{color.yellow + color.bold}{'-'*4} LIST OF NUMBERS FROM 0-100 WITHOUT ZEROES {'-'*4}{color.end}')

for number in range(0, 101):
    if number % 10 != 0:
        number_bold = f'{color.bold}{number}{color.end}'
        print(number_bold, end=", ")