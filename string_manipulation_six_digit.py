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

zero_digit = 0

while True:
    try:
        user_input = int(input(f'{color.yellow + color.bold}ENTER FROM 0-1000 --> {color.end}'))
        
        if user_input > 1000 or user_input < 0:
            raise ValueError

        else:
            user_input = str(user_input)
            for number in user_input:
                zero_digit += 1
            
            zero_amount = 6 - zero_digit
            final_digits = f'{'0' * zero_amount}' + user_input
        
        print(f'{color.green + color.bold}{final_digits}{color.end}')
        break
    
    except ValueError as e:
        print(f'{color.red + color.bold}Input an appropriate value. Please try again.{color.end}')