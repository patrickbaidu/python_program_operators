class color:
    PURPLE = '\033[95m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    GREEN = '\033[92m'

while True:
    try:
        input_first_number = float(input(f'{color.YELLOW + color.BOLD}ENTER FIRST NUMBER -->{color.END} '))
        input_second_number = float(input(f'{color.YELLOW + color.BOLD}ENTER SECOND NUMBER -->{color.END} '))
        
        input_first_number_colored = f'{color.PURPLE + color.BOLD}{input_first_number}{color.END}'
        input_second_number_colored = f'{color.PURPLE + color.BOLD}{input_second_number}{color.END}'

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
        print(f'{color.RED + color.RED}Input an appropriate value. Please try again.{color.END}')