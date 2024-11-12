# class is a blueprint (empty) different class is present
# when filled it is an oject (form)
# class Employee:
#     name = "Kashyap"
#     language = "py"
#     salary = 120000
# RAM = Employee()
# print(RAM.name, RAM.language)  

class Employee:
    language = "py"
    salary = 120000


RAM = Employee()
print(RAM.language, RAM.salary) 

# Shayam = Employee()
# Shayam.name = "Shayam"
# print(Shayam.name, Shayam.salary, Shayam.language)

# here name is object (instance) attribute,  and salary and language are class attribute as they directly belong to class
