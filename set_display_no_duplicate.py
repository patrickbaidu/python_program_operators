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
    
    for user_input in range(1,11):
        if user_input == 1:
            input_number = input(f'{color.yellow + color.bold} ENTER {user_input}ST NUMBER --> {color.end}' )
            input_number_list.append(input_number)
        elif user_input == 2:
            input_number = input(f'{color.yellow + color.bold} ENTER {user_input}ND NUMBER --> {color.end}')
            input_number_list.append(input_number)
        elif user_input == 3:
            input_number = input(f'{color.yellow + color.bold} ENTER {user_input}RD NUMBER --> {color.end}')
            input_number_list.append(input_number)
        else:
            input_number = input(f'{color.yellow + color.bold} ENTER {user_input}TH NUMBER --> {color.end}')
            input_number_list.append(input_number)
        
        count_data = input_number_list.count(input_number)
        
        if count_data != 1:
            for similar_data in input_number_list:
                input_number_list.pop(count_data)    
    
    display_list = ", ".join(number for number in input_number_list)
    
    print(f'A Set of {color.cyan + color.bold}{display_list}{color.end}')

except ValueError as e:
    print(f'{color.red + color.bold}Input an appropriate value. Please try again.{color.end}')