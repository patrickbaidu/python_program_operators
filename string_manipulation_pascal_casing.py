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
        user_input = input(f'{color.yellow + color.bold}ENTER FULL NAME --> {color.end}')
        
        if not user_input.replace(' ', '').isalpha():
            raise ValueError

    except ValueError as e:
        print(f'{color.red + color.bold}Input an appropriate value. Please try again.{color.end}')
    else:
        user_input = user_input.strip()
        user_input = user_input.title()
        user_input = user_input.replace(' ', '')
        print(f'{color.green + color.bold}{user_input}{color.end}')
        break