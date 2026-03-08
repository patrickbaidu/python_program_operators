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
        
        input_first_number_colored = f'{color.purple + color.bold}{input_first_number}{color.end}'
        input_second_number_colored = f'{color.purple + color.bold}{input_second_number}{color.end}'

        if input_first_number > input_second_number:
            print(f'{input_first_number_colored} is greater than {input_second_number_colored}')
            break
        
        elif input_first_number == input_second_number:
            print(f'{input_first_number_colored} is equal to {input_second_number_colored}')
            break
        
        else:
            print(f'{input_second_number_colored} is greater than {input_first_number_colored}')
            break
    
    except ValueError as e:
        print(f'{color.red + color.bold}Input an appropriate value. Please try again.{color.end}')