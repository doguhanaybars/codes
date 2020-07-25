class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print("Person Created")

    def who_am_i(self):
        print("i am a person")

    def eat(self):
        print("Eating")


class Student(Person):
    def __init__(self, fname, lname, number):
        # Studentın initi ile personun initi birbirini ezmesin ikisi de çalışsın diye
        Person.__init__(self, fname, lname)
        self.studentNumber = number
        print("Student Created")

    def who_am_i(self):
        print("İ am a student")

    def sayHello(self):
        print("hello i am a student")


class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname, lname)
        self.branch = branch

    def who_am_i(self):
        print(f"i am a {self.branch} teacher")


p1 = Person("Ali", "Yılmaz")
s1 = Student("Çınar", "Turan", 1256)
t1 = Teacher("Nejat", "Yumuşak", "Matematik")
print(p1.firstName + p1.lastName)

print(s1.firstName + s1.lastName + str(s1.studentNumber))
p1.who_am_i()
s1.who_am_i()
s1.eat()
s1.sayHello()
t1.who_am_i()
