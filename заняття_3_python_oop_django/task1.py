class User:

    USERS_COUNT = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

        User.USERS_COUNT += 1

    @classmethod
    def increment_users(cls):
        cls.USERS_COUNT += 1

    @classmethod
    def from_dict(cls, d):
        return cls(d['name'], d['age'])


    @staticmethod
    def is_valid_name(name):
        return len(name) > 1 and name != ""



User.USERS_COUNT += 1

user1 = User("Alice", 18)
print(user1.name)
print(user1.age)

user2 = User.from_dict({'name': 'Bob', 'age': 25})
print(user2.name)
print(user2.age)


