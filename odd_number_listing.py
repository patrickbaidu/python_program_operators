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

print(f'{color.yellow + color.bold}{'-'*4} LIST OF ODD NUMBERS FROM 0-100 {'-'*4}{color.end}')

number = 0
odd_number_list = []

while number < 100:
    number += 1
    if number % 2 == 1:
        odd_number_list.append(number)

list_of_odd_numbers = ', '.join(str(number) for number in odd_number_list)
list_of_odd_numbers = f'{color.bold}{list_of_odd_numbers}{color.end}'

print(list_of_odd_numbers)