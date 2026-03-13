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
    input_number_list = []
    input_number_set = set()
    
    for user_input in range(1,11):
        if user_input == 1:
            input_number = input(f'{color.yellow + color.bold} ENTER {user_input}ST NUMBER --> {color.end}' )
        elif user_input == 2:
            input_number = input(f'{color.yellow + color.bold} ENTER {user_input}ND NUMBER --> {color.end}')
        elif user_input == 3:
            input_number = input(f'{color.yellow + color.bold} ENTER {user_input}RD NUMBER --> {color.end}')
        else:
            input_number = input(f'{color.yellow + color.bold} ENTER {user_input}TH NUMBER --> {color.end}')

        if input_number in input_number_list:
            input_number_set.add(input_number)
        else:
            input_number_list.append(input_number)
        
    display_list = ", ".join(number for number in input_number_set)
    
    count_list = len(input_number_set)
    
    if count_list != 0:
        print(f'A Set of {color.cyan + color.bold}{display_list}{color.end}')
    
    else:
        print(f'{color.red + color.bold}NO EXISTING DUPLICATES{color.end}')

except ValueError as e:
    print(f'{color.red + color.bold}Input an appropriate value. Please try again.{color.end}')