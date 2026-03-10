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
    
    power_of_numbers = input_first_number ** input_second_number
    
    first_number_bold = f'{color.bold}{input_first_number}{color.end}'
    second_number_bold = f'{color.bold}{input_second_number}{color.end}'
    power_of_numbers_colored = f'{color.purple}{power_of_numbers}{color.end}'
    
    print(f'{first_number_bold} ^ {second_number_bold} = {power_of_numbers_colored}')
    print(f'{power_of_numbers_colored} is {first_number_bold} raised to {second_number_bold}.')
    
except ValueError as e:
    print(f'{color.red + color.bold}Input an appropriate value. Please try again.{color.end}')