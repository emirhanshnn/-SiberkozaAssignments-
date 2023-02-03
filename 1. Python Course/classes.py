# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object
class student_es:
    def __init__(self,name="Unknown",surname="Unknown",number="Unknown"):
        self.name_es=name
        self.surname_es=surname
        self.number_es=number
    
    def show_es(self):
        print(f"Name:{self.name_es}\tSurname:{self.surname_es}\tNumber:{self.number_es}\t")
    
    def change_number(self,number):
        self.number_es=number


student1_es = student_es("Emirhan","Şahin",200201006)
student2_es = student_es("Karsu")
student1_es.show_es()
student2_es.show_es()
student1_es.change_number(3238)
student1_es.show_es()