my_biodata = {
    'name': 'Lydia Sanyu',
    'age': 50,
    'date_of_birth': '01/02/1970',
    'address': 'Kampala, Uganda',
    'email': 'lydiasanyu@gmail.com',
    'phone_number': '0772123456'
}

print('\nMy biodata')
print('----------------------------')
for (key, value) in my_biodata.items():
    print(f'{key}: {value}')
print('----------------------------\n')
