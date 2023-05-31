import json
import hashlib
import uuid
from datetime import datetime


class Human:
    def __init__(self, name, phone_number, password, id_user=None):
        self.name = name
        self.phone_number = phone_number
        self.password = self._encrypt_password(password)
        if id_user is None:
            self.id_user = str(uuid.uuid4())
        else:
            self.id_user = id_user

    @staticmethod
    def _encrypt_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    def validate_password(self):
        return len(self.password) >= 4


class User(Human):
    def __init__(self, name, phone_number, password, id_user=None, birth_date=None, registration_date=None, subscription='Bronze', balance=0):
        super().__init__(name, phone_number, password, id_user=id_user)
        self.birth_date = birth_date
        if registration_date is None:
            self.registration_date = datetime.today().date().isoformat()
        else:
            self.registration_date = registration_date
        self.subscription = subscription
        self.balance = balance

    def register_user(self):
        try:
            with open('users.json', 'r') as f:
                users = json.load(f)
        except FileNotFoundError:
            with open('users.json', 'w') as f:
                f.write("{}")
                users = json.load(f)

        if self.name in users:
            print("Name already exists")
            return False

        users[self.name] = {
            'id_user': self.id_user,
            'name': self.name,
            'phone_number': self.phone_number,
            'password': self.password,
            'birth_date': self.birth_date,
            'registration_date': self.registration_date,
            'subscription': self.subscription,
            'balance': self.balance
        }

        with open('users.json', 'w') as f:
            json.dump(users, f)

        return True

    def edit_personal_info(self, new_name=None, new_phone_number=None, new_birth_date=None):
        try:
            with open('users.json') as f:
                users = json.load(f)
        except FileNotFoundError:
            quit(print("File not found"))

        user = users.get(self.name)
        if user is None:
            quit(print("user not found"))
        if new_name is not None:
            user['name'] = new_name
            self.name = new_name
        if new_phone_number is not None:
            user['phone_number'] = new_phone_number
            self.phone_number = new_phone_number
        if new_birth_date is not None:
            user['birth_date'] = new_birth_date
            self.birth_date = new_birth_date

        with open('users.json', 'w') as f:
            json.dump(users, f)

    @staticmethod
    def login_user(name, password):
        try:
            with open('users.json') as f:
                users = json.load(f)
        except FileNotFoundError:
            quit(print("fila not found"))

        user = users.get(name)
        if user['name'] == name and user['password'] == hashlib.sha256(password.encode()).hexdigest():
            return User(user['name'], user['phone_number'], user['password'], user['birth_date'],
                        user['registration_date'], user['subscription'], user['balance'])

        return False

    def change_password(self, old_password, new_password):
        try:
            with open('users.json') as f:
                users = json.load(f)
        except FileNotFoundError:
            quit(print("fila not found"))

        user = users.get(self.name)
        if user['id_user'] == self.id_user and user['password'] == hashlib.sha256(old_password.encode()).hexdigest():
            user['password'] = hashlib.sha256(new_password.encode()).hexdigest()
            self.password = user['password']

        with open('users.json', 'w') as f:
            json.dump(users, f)


class Manager(Human):
    def __init__(self, name, phone_number, password, id_user=None):
        super().__init__(name, phone_number, password, id_user=id_user)

    def register_admin(self):
        try:
            with open('managers.json', 'r') as f:
                managers = json.load(f)
        except FileNotFoundError:
            with open('managers.json', 'w') as f:
                    f.write("{}")
                    managers = json.load(f)

        if self.name in managers:
            print("Name already exists")
            return False

        managers[self.name] = {
            'id_admin': self.id_user,
            'name': self.name,
            'phone_number': self.phone_number,
            'password': self.password,
        }

        with open('managers.json', 'w') as f:
            json.dump(managers, f)

        return True

    @staticmethod
    def login_admin(name, password):
        try:
            with open('managers.json') as f:
                managers = json.load(f)
        except FileNotFoundError:
            quit(print("File not found"))

        admin = managers.get(name)
        if admin['name'] == name and admin['password'] == hashlib.sha256(password.encode()).hexdigest():
            return Manager(admin['name'], admin['phone_number'], admin['password'], admin['id_admin'])

        return False

    @staticmethod
    def show_user():
        try:
            with open('users.json', 'r') as f:
                users = json.load(f)
        except FileNotFoundError:
            print('File not found')
            return False
        name_list = list(users.keys())
        print('\n'.join(name_list))

    @staticmethod
    def del_user(user_name):
        try:
            with open('users.json', 'r') as f:
                users = json.load(f)
        except FileNotFoundError:
            print('File not found')
            return False

        if user_name in users:
            del users[user_name]

        with open('users.json', 'w') as f:
            json.dump(users, f)

        return True
