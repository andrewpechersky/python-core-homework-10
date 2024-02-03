from collections import UserDict


class Field:
    def __init__(self, value):
        if not self.is_valid(value):
            raise ValueError
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __len__(self):
        return len(self.value)

    def __contains__(self, item):
        return item == self.value

    def __str__(self):
        return str(self.value)

    def is_valid(self, value):
        return True


class Name(Field):
    pass


class Phone(Field):

    def is_valid(self, value):
        value = str(value)
        if value.isnumeric():
            return len(value) == 10
        else:
            raise ValueError


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))

    def edit_phone(self, phone, new_phone):
        phone = Phone(phone)
        if phone in self.phones:
            new_phone = Phone(phone)
            self.phones[self.phones.index(phone)] = new_phone
        else:
            raise ValueError

    def remove_phone(self, phone):
        if phone in self.phones:
            self.phones.pop(self.phones.index(phone))
        else:
            raise ValueError

    def find_phone(self, item):
        if item in self.phones:
            return Phone(item)
        else:
            return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}"


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()

    def add_record(self, record):
        self[record.name.value] = record

    def find(self, name):
        try:
            return self[name]
        except KeyError:
            return None

    def delete(self, name):
        if name in self.keys():
            self.pop(name)
        else:
            return None
