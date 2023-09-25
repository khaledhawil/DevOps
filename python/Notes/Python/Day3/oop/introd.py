print("------------------------OOP----------------------------------------")

# emp1 ={
#     "name" : "ahmed",
#     'email' : "ahmed@gmail.com",
#     "dept" : "devops"
# }
#
# emp2 ={
#     "empname" :"ali",
#     'empemail': "ali@gmail.com",
#     "dept" : "sd"
# }

"""
    create my own datastructure Employee ---> name, email , dept , id 

    define blueprint for a structure 
    --> properties of the instances from class
    --> functionalities this object can do 
"""
# ##############3 create class ########################
# class Employee:
#     pass
#
#
# e = Employee()  # address of object
# print(e)

#############################################

##############3 create class ########################
# class Employee:
#     def __init__(self):  # constructor function ---> is called while creating the object
#         print(self)  # self --> refer to the object address in the memory
#         self.name = "emp"
#         self.email = "ahmed@gmail.com"
#         self.id = 10
#
#
# e = Employee()  # address of object
# print(e)
# e2 = Employee()


#######################3 customize the object creation
#
# class Employee:
#     def __init__(self,name, email,id):  # constructor function ---> is called while creating the object
#         print(self)  # self --> refer to the object address in the memory
#         self.name = name  # instance varaible
#         self.email = email
#         self.id = id
#
#
# e = Employee("Ahmed", "ahmed@gmail.com", 10)  # address of object
# # python support representing the object in form of dic
# print(e.__dict__)
# e2 = Employee("Ali", "ali@gmail.com", 4)
# print(e2.__dict__)
#
#
# # ######################## instance method
#
# class Employee:
#     def __init__(self,name, email,id):  # constructor function ---> is called while creating the object
#         print(self)  # self --> refer to the object address in the memory
#         self.name = name  # instance varaible
#         self.email = email
#         self.id = id
#
#     # instance method
#     def printEmpInfo(self): # self ---> refer to the current caller instance
#         print(f"my name is {self.name}, you can reach me at {self.email}")
#
#
# e = Employee("Ahmed", "ahmed@gmail.com", 10)  # address of object
# e.printEmpInfo()
# e2 = Employee("Ali", "ali@gmail.com", 4)
# e2.printEmpInfo()
#
#


############################# class variable

# ######################## instance method
"""propery value ---> shared between all instance ---> it depends on the Class not the instance 

You can access it using class Name 
"""


class Employee:
    nationality = "Egyptian"   # class variable ---> value depends on the class not the object

    def __init__(self, name, email, id):  # constructor function ---> is called while creating the object
        print(self)  # self --> refer to the object address in the memory
        self.name = name  # instance varaible
        self.email = email
        self.id = id

    # instance method
    def printEmpInfo(self):  # self ---> refer to the current caller instance
        print(f"my name is {self.name}, you can reach me at {self.email}")


e = Employee("Ahmed", "ahmed@gmail.com", 10)  # address of object
e2 = Employee("Ali", "ali@gmail.com", 4)
e3 = Employee("Mohmed", "ali@gmail.com", 4)
print(e3.nationality)


