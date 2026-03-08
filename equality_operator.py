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

while True:
    try:
        input_first_number = float(input(f'{color.yellow + color.bold}ENTER FIRST NUMBER -->{color.end} '))
        input_second_number = float(input(f'{color.yellow + color.bold}ENTER SECOND NUMBER -->{color.end} '))
        
        first_number_colored_green = f'{color.green + color.bold}{input_first_number}{color.end}'
        second_number_colored_green = f'{color.green + color.bold}{input_second_number}{color.end}'
        first_number_colored_red = f'{color.red + color.bold}{input_first_number}{color.end}'
        second_number_colored_red = f'{color.red + color.bold}{input_second_number}{color.end}'

        if input_first_number == input_second_number:
            print(f'{first_number_colored_green} is equal to {second_number_colored_green}')
            break
        
        else:
            print(f'{first_number_colored_red} is not equal to {second_number_colored_red}')
            break
        
    except ValueError as e:
        print(f'{color.red + color.bold}Input an appropriate value. Please try again.{color.end}')