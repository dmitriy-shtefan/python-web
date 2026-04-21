from datetime import datetime, date, time

t = time(23, 59, 59)
t2 = time(00, 00, 00)
print(t > t2)
print(t < t2)

class TimestampMixin():
    def __init__(self, timestamp):
        self._timestamp = timestamp


class Person:
    def __init__(self, name, **kwargs):
        print(f"__Person__init__")
        self.name = name
        super().__init__(**kwargs)

    def __str__(self):
        return f"Name: {self.name}"

    def describe(self):
        return f"Name (Person): {self.name}"


class Student(Person):
    def __init__(self, group, **kwargs):
        print(f"__Student__init__")
        self.group = group
        super().__init__(**kwargs)

    def __str__(self):
        return f"Name: {self.name}, Student: {self.group}"

    def describe(self):
        return f"Name (Student): {self.name}"


class Athlete:

    def __init__(self, sport, **kwargs):
        print(f"__Athlete__init__")
        self.sport = sport
        super().__init__(**kwargs)

    def __str__(self):
        return f"Sport: {self.sport}"

    def describe(self):
        return f"Sport (Athlete): {self.sport}"


class SportiveStudent(Student, Athlete):

    def __init__(self, name, group, sport):
        print(f"__SportiveStudent__init__")
        super().__init__(name=name, group=group, sport=sport)
        # Student.__init__(self, name=name, group=group)
        # Athlete.__init__(self, sport)

    def describe(self):
        return f"Name (SportiveStudent): {self.name}"



student = SportiveStudent("Alice", "PV411", "running")

print(student.describe())

print(SportiveStudent.__mro__)