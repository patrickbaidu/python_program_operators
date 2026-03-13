user_input = input('ENTER --> ')

front_index = 0

characters = len(user_input)

while True:
    if front_index < characters and user_input[front_index] == " ":
        front_index += 1

    print(user_input[front_index:])
    break