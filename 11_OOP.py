class SchoolMember():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Initialized SchoolMember: {self.name}")
    
    def tell(self):

        print(f"Name: {self.name}, Age: {self.age}")

class Teacher(SchoolMember):
    def __init__(self,name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print(f"Initialized Teacher {self.name}")
    def tell(self):
        SchoolMember.tell(self)
        print(f"Salary: {self.salary}")

class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print(f"Initialized Student {self.name}")
    def tell(self):
        SchoolMember.tell(self)
        print(f"Marks: {self.marks} ")

t = Teacher("Mr Man", 40, 30000)

s = Student("Ngoan", 25, 75)

sc = SchoolMember("Man", 75)

print()

members = [t,s]

for member in members:
    member.tell()
        