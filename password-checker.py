username = input('Hello! Please input your username. ')
password = input('And now your password. ') 
password_length = len(password)

print(f'It\'s good to see you again, {username}! Your password {password_length * '*'} is {password_length} letters long.')