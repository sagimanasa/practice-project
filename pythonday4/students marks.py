class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender


class Student(Person):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)

    def set_maths(self, marks):
        self.__maths = marks

    def get_maths(self):
        return self.__maths

    def set_physics(self, marks):
        self.__physics = marks

    def get_physics(self):
        return self.__physics

    def set_chemistry(self,marks):
        self.__chemistry = marks

    def get_chemistry(self):
        return self.__chemistry

    def get_total(self):
        return self.__maths+self.__physics+self.__chemistry

    def set_marks(self, maths, physics, chemistry):
        self.set_maths(maths)
        self.set_physics(physics)
        self.set_chemistry(chemistry)

manasa = Student("manasa", 21, "F")
honey = Student("honey", 21, "F")
rishi = Student("rishi", 21, "F")
manasa.set_marks(90,80,70)
honey.set_marks(80,60,50)
rishi.set_marks(80,40,70)
list_students=[manasa,honey,rishi]
total=0
print(manasa.get_total())
for student in list_students:
    total+=student.get_total()

print(total/len(list_students))
print(manasa.get_maths())

