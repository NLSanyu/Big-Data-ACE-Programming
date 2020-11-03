class Person:
    def __init__(self, name, age, date_of_birth, 
                    address, email, phone_number
                ):
        self.name = name
        self.age = age
        self.date_of_birth = date_of_birth
        self.address = address
        self.email = email
        self.phone_number = phone_number

    def print_biodata(self):
        print('Name: {}\nAge: {}\nDate of birth: {}\nAddress: {}\nEmail: {}\nPhone_number: {}'.format(
                self.name, self.age, self.date_of_birth, 
                self.address, self.email, self.phone_number
            )
        )

if __name__ == '__main__':
    lydia = Person(
            'Lydia Sanyu', '50', '01/02/1970', 'Kampala, Uganda',
            'lydiasanyu@gmail.com', '0772123456'
        )
    lydia.print_biodata()