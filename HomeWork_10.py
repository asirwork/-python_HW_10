from collections import UserDict


class Field:

    def __init__(self, value):
        self.value = value


class Name(Field):
    ...


class Phone(Field):
    ...


class Record:

    def __init__(self, name: Name, phone: Phone = Phone(None)):
        self.name = name
        self.phones = [phone] if phone else []

    def __str__(self):
        return f"{self.name}: {', '.join(self.phone)}"

    def add(self, phone: Phone):
        self.phones.append(phone)

    def edit(self, new_phone: Phone) -> str:
        old_phone = self.phone.value
        new_phone_value = new_phone.value
        self.phone = new_phone
        return f"Change {old_phone} to {new_phone_value}"

    def remove(self, phone: Phone):
        if phone in self.phones:
            self.phones.remove(phone)
            if phone == self.phone:
                self.phone = None
        else:
            raise ValueError("Phone not found in record.")


class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def __str__(self):
        output = []
        for name, record in self.data.items():
            phones = [
                phone.value for phone in record.phones
                if phone.value is not None
            ]
            phone_str = ", ".join(phones) if phones else "N/A"
            output.append(f"{name}: {phone_str}")
        return "\n".join(output)


if __name__ == "__main__":

    ab = AddressBook()
    name = Name("Bill")
    phone1 = Phone("12345")
    phone2 = Phone("67890")
    phone3 = Phone("7777777")
    rec = Record(name, phone1)
    rec.add(phone2)
    rec.add(phone3)
    ab.add_record(rec)
    print(ab)
