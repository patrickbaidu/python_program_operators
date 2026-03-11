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

try:
    input_first_number = float(input(f'{color.yellow + color.bold}ENTER FIRST NUMBER -->{color.end} '))
    input_second_number = float(input(f'{color.yellow + color.bold}ENTER SECOND NUMBER -->{color.end} '))
    
    remainder_of_quotient = input_second_number % input_first_number
    
    first_number_bold = f'{color.bold}{input_first_number}{color.end}'
    second_number_bold = f'{color.bold}{input_second_number}{color.end}'
    remainder_of_quotient_colored = f'{color.green}{remainder_of_quotient}{color.end}'
    
    if remainder_of_quotient > 0:
        print(f'{second_number_bold} ÷ {first_number_bold} has a remainder of {remainder_of_quotient_colored}')
        print(f'{remainder_of_quotient_colored} is the remainder of the two numbers.')
    
    else:
        print(f'{second_number_bold} ÷ {first_number_bold} has a remainder of {remainder_of_quotient_colored}')
        print(f'The are no remainder for the two numbers. The value is {remainder_of_quotient_colored}.')
    
except ValueError as e:
    print(f'{color.red + color.bold}Input an appropriate value. Please try again.{color.end}')