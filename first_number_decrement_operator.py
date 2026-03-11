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
    first_input_number_equated = 0
    first_input_number_unequated = 0
    decrement_number_list = []
    
    for user_input in range(1,11):
        if user_input == 1:
            input_number = float(input(f'{color.yellow + color.bold} ENTER {user_input}ST NUMBER --> {color.end}' ))
            first_input_number_equated += input_number
            first_input_number_unequated += input_number
        elif user_input == 2:
            input_number = float(input(f'{color.yellow + color.bold} ENTER {user_input}ND NUMBER --> {color.end}'))
            first_input_number_equated -= input_number
            decrement_number_list.append(input_number)
        elif user_input == 3:
            input_number = float(input(f'{color.yellow + color.bold} ENTER {user_input}RD NUMBER --> {color.end}'))
            first_input_number_equated -= input_number
            decrement_number_list.append(input_number)
        else:
            input_number = float(input(f'{color.yellow + color.bold} ENTER {user_input}TH NUMBER --> {color.end}'))
            first_input_number_equated -= input_number
            decrement_number_list.append(input_number)
    
    decrement_of_first_number = f'{color.green + color.bold}{first_input_number_equated}{color.end}'
    
    equation_of_list = " - ".join(str(number) for number in decrement_number_list)
    equation_of_list = f'{color.cyan + color.bold}{equation_of_list}{color.end}'
    first_input_number_unequated = f'{color.yellow + color.bold}{first_input_number_unequated}{color.end}'
    first_input_number_equated = f'{color.green + color.bold}{first_input_number_equated}{color.end}'
    
    print(f'{first_input_number_unequated} - ({equation_of_list}) =')
    print(first_input_number_equated)

except ValueError as e:
    print(f'{color.red + color.bold}Input an appropriate value. Please try again.{color.end}')