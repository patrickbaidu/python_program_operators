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
    input_number_set = {}
    input_number_set = set(input_number_set)
    
    for user_input in range(1,11):
        if user_input == 1:
            input_number = input(f'{color.yellow + color.bold} ENTER {user_input}ST NUMBER --> {color.end}' )
            input_number_set.add(input_number)
        elif user_input == 2:
            input_number = input(f'{color.yellow + color.bold} ENTER {user_input}ND NUMBER --> {color.end}')
            input_number_set.add(input_number)
        elif user_input == 3:
            input_number = input(f'{color.yellow + color.bold} ENTER {user_input}RD NUMBER --> {color.end}')
            input_number_set.add(input_number)
        else:
            input_number = input(f'{color.yellow + color.bold} ENTER {user_input}TH NUMBER --> {color.end}')
            input_number_set.add(input_number)
    
    display_set = ", ".join(number for number in input_number_set)
    
    print(f'A Set of {color.cyan + color.bold}{display_set}{color.end}')

except ValueError as e:
    print(f'{color.red + color.bold}Input an appropriate value. Please try again.{color.end}')