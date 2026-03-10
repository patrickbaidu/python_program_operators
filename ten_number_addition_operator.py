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
    
    increment_of_input_number = 0
    input_number_list = []
    
    for user_input in range(1,11):
        if user_input == 1:
            input_number = float(input(f'{color.yellow + color.bold} ENTER {user_input}ST NUMBER --> '))
            increment_of_input_number += input_number
            input_number_list.append(input_number)
        elif user_input == 2:
            input_number = float(input(f'{color.yellow + color.bold} ENTER {user_input}ND NUMBER --> '))
            increment_of_input_number += input_number
            input_number_list.append(input_number)
        elif user_input == 3:
            input_number = float(input(f'{color.yellow + color.bold} ENTER {user_input}RD NUMBER --> '))
            increment_of_input_number += input_number
            input_number_list.append(input_number)
        else:
            input_number = float(input(f'{color.yellow + color.bold} ENTER {user_input}TH NUMBER --> '))
            increment_of_input_number += input_number
            input_number_list.append(input_number)
    
    summation_of_numbers = f'{color.bold}{input_first_number}{color.end}'
    
    input_number_list_bold = f'{color.bold}{input_number_list}{color.end}'


    
except ValueError as e:
    print(f'{color.red + color.bold}Input an appropriate value. Please try again.{color.end}')