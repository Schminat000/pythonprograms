first = input('Type your first name: '); last = input('Type your last name: ')
job = input('Type your job title: '); email = input('Type your email address: ')
id = input('Type your ID number: '); phone = input('Type your phone number: ')
hair = input('Type your hair color: '); eye = input('Type your eye color: ')
month = input('Type your starting month: '); train = input('Have you completed advanced training? Type yes or no: ')
names = f'{last}, {first}'; jobs = f'{job}'
print('')
print('The ID Card is:')
print('----------------------------------------')
print(last.upper() + ', ' + first.capitalize())
print(jobs.title())
print('ID: ' + id)
print('')
print(email.lower())
print(phone)
print('')
print(f"Hair: {hair.capitalize():15} Eyes: {eye.capitalize()}")
print(f'Month: {month.capitalize():14} Training: {train.capitalize()}')
print('----------------------------------------')