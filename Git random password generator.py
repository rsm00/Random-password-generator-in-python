import random , string

length_of_password = int(input('Enter the length of the password in number, you want : '))

password_characters = string.ascii_letters + string.digits + string.punctuation

password = []

for x in range(length_of_password):
    password.append(random.choice(password_characters))

print(''.join(password))


