class Human:
    height = 170
    age=50

class Student(Human):
    age = 12
    height = 165
class Worker(Human):
    age = 35
    height = 170

class Pensioner(Human):
    age = 75
    height = 165

nick = Student()
ann = Worker()
john = Pensioner()
print(nick.height)
print(ann.height)
print(john.height)

print(nick.age)
print(ann.age)
print(john.age)