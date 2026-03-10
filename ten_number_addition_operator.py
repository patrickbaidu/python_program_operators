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
    
    for user_input in range(1,11):
        if user_input == 1:
            input_number = float(input(f'{color.yellow + color.bold} ENTER {user_input}ST NUMBER --> '))
        elif user_input == 2:
            input_number = float(input(f'{color.yellow + color.bold} ENTER {user_input}ND NUMBER --> '))
        elif user_input == 3:
            input_number = float(input(f'{color.yellow + color.bold} ENTER {user_input}RD NUMBER --> '))
        else:
            input_number = float(input(f'{color.yellow + color.bold} ENTER {user_input}TH NUMBER --> '))

    
except ValueError as e:
    print(f'{color.red + color.bold}Input an appropriate value. Please try again.{color.end}')