class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
class Branch:
    def __init__(self,name):
        self.name=name
        self.subject_list=[]
        self.teacher_list=[]
        self.student_list=[]
    def add_subject(self,subject):
        self.subject_list.append(subject)
    def get_subject(self):
        return self.subject_list
    def has_subject(self,subject):
        pass
    def add_teacher(self,teacher):
        self.teacher_list.append(teacher)
    def get_teacher(self):
        return self.teacher_list
    def has_teacher(self,teacher):
        pass
    def add_student(self,student):
        self.student_list.append(student)
    def get_student(self):
        return self.student_list
    def has_student(self,student):
        pass
class Student(Person):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.subject_list=[]
    def add_subject(self,subject):
        self.subject_list.append(subject)
    def get_subject(self):
        return self.subject_list
class Teacher(Person):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.subject_list=[]
        self.branch_list=[]
    def add_subject(self,subject):
        self.subject_list.append(subject)
    def get_subject(self):
        return self.subject_list
    def add_branch(self,branch):
        self.branch_list.append(branch)
    def get_branch(self):
        return self.branch_list
