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

sum_of_input_number = 0
count_user_input = 0
    
while True:
    try:
        user_input_number = int(input(f'{color.yellow + color.bold}ENTER A NUMBER --> {color.end}'))

        if user_input_number:
            count_user_input += 1
            sum_of_input_number += user_input_number
        
        average = sum_of_input_number / count_user_input
        
        print(f'{color.purple + color.bold}{sum_of_input_number} ÷ {count_user_input} ={color.end}')
        print(f'{color.green + color.bold}{average}{color.end} is the Average.')
    except ValueError as e:
        print(f'{color.red + color.bold}Input an appropriate value. {color.end}')
        break

