#Primera versión
#Creación de clase:

class Employee():
    def __init__(self, name, surname)
                 #, age, sal, id, dateini 
        self.__name = name
        self.__surname = surname
        #self.__age = age
        #self.__sal = sal
        #self.__id = id
        #self.__dateini = dateini
        
        
    def getFullname(self):
        return f"{self.__name}, {self.__surname}" 
        
    def getName(self):
        return self.__name   
    
    def getAge(self):
        return self.__age
    
    def getDate(self):
        return self.__dateini
    
    def setAge(self, age):
        set.__age = age  
    
class Boss(Employee):
    def __init__(self, name, surname, age, sal, id, dateini, employeeAC):
        super().__init__(name, surname, age, sal, id, dateini)
        listaEmp = []
        
    def addEmp(listaEmp):
        listaEmp.append(input("Nombre del empleado: "))
        
        #self.EmployeeCharged = employeeAC
        
employee1 = Employee("Ana", "Méndez", 21, 2000000, 1062134256, "10-02-2023")

print(f"Nombre completo del empleado: ", employee1.getFullname())
print(f"Edad del empleado: ", employee1.getAge())
print(f"Fecha de vinculación: ", employee1.getDate())


#boss1 = Boss("Diana", "Álvarez", 34)
#boss1.addEmp()

        
        
class Area():
    def _init_(self, name, description):
        self.name = name
        self.description = description
        #self.employees = []
        
        
       # listEmpl = []
        #
listEmpl = []
def Show():
    k = 0
    while (k < len (listEmpl)):
        print (listEmpl[k].name, " ", listEmpl[k].description, " ")
        k += 1   
               
i = 0
while (True):
    print("\n\n1. Register empleado")
    print("2. Consultar listado")
    print("3. Salir")
    opcion = int(input("Ingrese una opción: "))
    if (opcion ==1):
        name = input("Nombre completo: ")
        description = input("Descripción del área en la que trabaja: ")
        employee1 = Employee(name, description)
        listEmpl.append(employee1)
        print("Empleado guardado con éxito.")
    elif (opcion ==2):
        #print("Ir a mostrar")
        Show()
    elif (opcion == 3):
       exit()
    else:
        print("El código funciona")
        
        

    #def add_employee(self, employee):
        #self.employees.append(employee)
        
   # def get_quant_employee(self):
       # return len(self.employees)
    
   # def get_employees(self):
       # return self.employees
    
   # def __str__(self):
    #    return f"Área: {self.name}. Descripción: {self.description}. Cantidad de empleados: {len(self.empleados)}"