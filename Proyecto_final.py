#Primera versión
#Creación de clase:

class Employee():
    def __init__(self, name, surname, age, sal, id, date_vin ):
        self.name = name
        self.surname = surname
        self.age = age
        self.sal = sal
        self.id = id
        self.dateini = date_vin
    
    def getFull_name(self):
        return f"{self.name} {self.surname}"
    
class Boss(Employee):
    def __init__(self, name, surname, age, sal, id, date_vin, EmployeeAC):
        super().__init__(name, surname, age, sal, id, date_vin)
        self.EmployeeCharged = EmployeeAC
        
class Area():
    def _init_(self, name, description):
        self.name = name
        self.description = description
        self.employees = []
    
    def add_employee(self, employee):
        self.employees.append(employee)
        
    def get_quant_employee(self):
        return len(self.employees)
    
    def get_employees(self):
        return self.employees
    
    def __str__(self):
        return f"Área: {self.name}. Descripción: {self.description}. Cantidad de empleados: {len(self.empleados)}"