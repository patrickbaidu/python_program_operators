while True:
    try:
        input_first_number = float(input("ENTER FIRST NUMBER --> "))
        input_second_number = float(input("ENTER SECOND NUMBER --> "))
        
        if input_first_number > input_second_number:
            print(f'{input_first_number} is greater than {input_second_number}')
            break
        
        elif input_first_number == input_second_number:
            print(f'{input_first_number} is equal to {input_second_number}')
            break
        
        else:
            print(f'{input_second_number} is greater than {input_first_number}')
            break
    
    except ValueError as e:
        print("Input an appropriate value. Please try again.")