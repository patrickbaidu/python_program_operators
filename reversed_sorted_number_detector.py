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
        
        input_number_list.append(user_input_number)
        reversed_sorted_number_list = sorted(input_number_list, reverse = True)
        reversed_sorted_number_list = ", ".join(str(number) for number in reversed_sorted_number_list)
        print(f'Sorted List: {color.purple + color.bold}{reversed_sorted_number_list}{color.end}')
        
    except ValueError as e:
        print(f'{color.red + color.bold}Input an appropriate value. {color.end}')
        break