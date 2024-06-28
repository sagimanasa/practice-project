class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
class Classes:
    def __init__(self,name):
        self.name=name
        self.subject_list=[]
        self.branch_list=[]
        self.teacher_list=[]
    def add_subject(self,subject):
        self.subject_list.append(subject)
    def get_subject(self):
        return self.subject_list
    def has_subject(self,subject):
        pass
    def add_branch(self,branch):
        self.branch_list.append(branch)
    def get_branch(self):
        return self.branch_list
    def has_branch(self,branch):
        pass
    def add_teacher(self,teacher):
        self.teacher_list.append(teacher)
    def get_teacher(self):
        return self.teacher_list
    def has_teacher(self,teacher):
        pass

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


