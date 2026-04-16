from collections import namedtuple
from dataclasses import dataclass

# User = namedtuple('User', ['name', 'password'])

@dataclass
class StatusCode:
    NOT_FOUND: int = 404
    FATAL_ERROR: int = 500


class User:

    role: str = 'User'

    code: StatusCode = StatusCode.NOT_FOUND

    def __init__(self, name: str, password: str):
        named_tuple = namedtuple('User', ['name', 'password'])
        self._name = name
        self.__password = password
        self.u = named_tuple

    def login(self):
        pass

    @property
    def name(self):
        return "name: " + self._name

    @name.setter
    def name(self, value: str):
        if value != '':
            self._name = value



user1 = User('Alyona', '09876543221')
user2 = User('Polina', 'qwerty')

print(user1.role)
print(user2.role)

User.role = 'Admin'

user1.role = 'Guest'

print(user1.role)
print(user2.role)

# u.login()

# небезпечний доступ до private атрибута
# print(u._User__password)

# помилка - немає такого атрибута
# print(u.__password)

# u.name = 'Anna'
# print(u.name)