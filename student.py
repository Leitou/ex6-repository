from module import *
from moduleElement import *



class Student(object):

    def __init__(self, name):
        ######## CODE MISSING HERE 1.
        self.name = name
        self.modules = [] # 2.
        self.grades = {} # 3.


    def add_module(self,title):
        ######## CODE MISSING HERE 4.
        # title is an instance of class Module
        self.modules.append(title)
        # 5.
        self.grades[title] = title.get_grade()


    def get_list_modules(self):
        ######## CODE MISSING HERE 6.
        print("Modules of Student {}".format(self.name))
        for module in self.modules:
            print("\t{}".format(module.get_title()))

    def get_grades(self):
        ######## CODE MISSING HERE 7.
        print("Grades of Student {}".format(self.name))
        for module, grade in self.grades.items():
            # I'm not sure whether accessing the module title in the following
            # way is asked for.. I do it that way because I don't want to change the Course.__str__()
            # method in the other file (because of the other expected outputs there).
            print("\t{}: {}".format(module.get_title(),grade))


### test cases ###

me = Student("FirstName LastName")
me.add_module(info1)
#me.add_module(math1)
me.get_list_modules()
# expected output:
# Modules of Student FirstName LastName:
#	Info 1

me.get_grades()
# expected output:
# Grades of Student FirstName LastName:
#	Info 1: 6
