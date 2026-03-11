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
        between_number_list = []
        
        input_first_number = int(input(f'{color.yellow + color.bold}ENTER FIRST NUMBER -->{color.end} '))
        input_second_number = int(input(f'{color.yellow + color.bold}ENTER SECOND NUMBER -->{color.end} '))
        
        input_first_number_increment = input_first_number + 1
        input_second_number_increment = input_second_number + 1
        
        if input_first_number > input_second_number:
            
            for between_number in range(input_second_number_increment, input_first_number):
                between_number_list.append(between_number)
                
            number_list = ", ".join(str(number) for number in between_number_list)
            number_list = f'{color.bold}{number_list}{color.end}'
            
            input_first_number_colored = f'{color.purple + color.bold}{input_first_number}{color.end}'
            input_second_number_colored = f'{color.purple + color.bold}{input_second_number}{color.end}'
            
            print(f'The numbers between {input_first_number_colored} and {input_second_number_colored} are {number_list}')
        
        else:
            for between_number in range(input_first_number_increment, input_second_number):
                between_number_list.append(between_number)
                
            number_list = ", ".join(str(number) for number in between_number_list)
            number_list = f'{color.bold}{number_list}{color.end}'
            
            input_first_number_colored = f'{color.purple + color.bold}{input_first_number}{color.end}'
            input_second_number_colored = f'{color.purple + color.bold}{input_second_number}{color.end}'
            
            print(f'The numbers between {input_first_number_colored} and {input_second_number_colored} are {number_list}')
            
        break
        
    except ValueError as e:
        print(f'{color.red + color.bold}Input an appropriate value. Please try again.{color.end}')