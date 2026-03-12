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

input_number_list = []
    
while True:
    try:
        user_input_number = int(input(f'{color.yellow + color.bold}ENTER A NUMBER --> {color.end}'))

        if user_input_number in input_number_list:
            print('duplicate')
        
        else:
            print('unique')
            input_number_list.append(user_input_number)


    except ValueError as e:
        print(f'{color.red + color.bold}Input an appropriate value. {color.end}')
        break

