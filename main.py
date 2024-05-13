import re
from collections import UserDict

class Field:
    '''Basic class for text information'''
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    '''The class for contact name'''
    def __init__(self, value):
           super().__init__(value)

class Phone(Field):
    '''The class for phone number'''
    def __init__(self, value):
           super().__init__(value)

class Record:
    '''This class contain objects of Class Name and list of objects from class Phone'''
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: str):
        '''
        The method add the phone number in to list, and check
        if the phone number has correct format
        '''
        if bool(re.match(r'^\d{10}$', phone)):
            self.phones.append(Phone(phone))

    def edit_phone(self, old_phone: str, new_phone: str):
        '''This method allow to replace the old_phone with the new_phone'''
        for index, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones[index].value = new_phone

    def remove_phone(self, phone_to_remove: str):
        '''This method allow to remove the phone number'''
        for index, phone in enumerate(self.phones):
            if phone.value == phone_to_remove:
                del self.phones[index]

    def find_phone(self, phone_to_search: str) -> Phone:
        '''This method accept phone number and return existing Phone object'''
        for index, phone in enumerate(self.phones):
            if phone.value == phone_to_search:
                return phone.value
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    '''The main class for object for user interract with'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add_record(self, record):
        '''
        Method to add object Record in to AddressBook
        The Record will be associated with key value record.name
        '''
        self.data[record.name] = record

    def find(self, name_to_search: str) -> Record:
        '''This method performs search of the Record type object by his name'''
        for name, record in self.data.items():
            if name.value == name_to_search:
                return record
        return None

    def delete(self, name_to_delete: str) -> None:
        '''This method delete existing Record object from the AddressBook'''
        record_to_delete = self.find(name_to_delete)
        key_to_delete = record_to_delete.name
        del self.data[key_to_delete]


#####################################

# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# ведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")
