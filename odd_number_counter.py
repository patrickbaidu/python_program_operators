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
    
    number_list = []
    odd_number_list = []
    
    for user_input in range(1,11):
        if user_input == 1:
            input_number = float(input(f'{color.yellow + color.bold} ENTER {user_input}ST NUMBER --> {color.end}' ))
            number_list.append(input_number)
        elif user_input == 2:
            input_number = float(input(f'{color.yellow + color.bold} ENTER {user_input}ND NUMBER --> {color.end}'))
            number_list.append(input_number)
        elif user_input == 3:
            input_number = float(input(f'{color.yellow + color.bold} ENTER {user_input}RD NUMBER --> {color.end}'))
            number_list.append(input_number)
        else:
            input_number = float(input(f'{color.yellow + color.bold} ENTER {user_input}TH NUMBER --> {color.end}'))
            number_list.append(input_number)
    
    for number in number_list:
        if number % 2 == 1:
            odd_number_list.append(number)
    
    count_odd_number = f'{len(odd_number_list)} Odd Numbers'
    
    print(f'There are {color.green + color.bold}{count_odd_number}{color.end} in the number list.')
    
except ValueError as e:
    print(f'{color.red + color.bold}Input an appropriate value. Please try again.{color.end}')