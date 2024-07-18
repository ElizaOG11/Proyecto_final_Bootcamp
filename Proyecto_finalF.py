# Creación de clase:

class Employee:
    def __init__(self, name, surname, age, sal, id, date_vin):
        self.name = name
        self.surname = surname
        self.age = age
        self.sal = sal
        self.id = id
        self.date_vin = date_vin
    
    def getFull_name(self):
        return f"{self.name} {self.surname}"
    
    def getSal(self):
        return f"Empleado: {self.getFull_name()}, ID: {self.id}, salario: {self.sal}"
    
    def getFull_info(self):
        return f"Nombre completo: {self.getFull_name()}, ID: {self.id}, Edad: {self.age}, Fecha de vinculación: {self.date_vin}"     
    
class Boss(Employee):
    def __init__(self, name, surname, age, sal, id, date_vin):
        super().__init__(name, surname, age, sal, id, date_vin)
        self.employeeCharged = []
        
    def add_employeeCharged(self, employee):
        for emp in self.employeeCharged:
            if emp == employee:
                print(f"El empleado {employee.getFull_name()} ya se encuentra registrado en el sistema a cargo del jefe {self.getFull_name()}.")
                return 
        self.employeeCharged.append(employee)
        print(f"El empleado {employee.getFull_name()} ha sido agregado correctamente a cargo del jefe {self.getFull_name()}")
        
    def get_employeeCharged(self):
        return [employee.getFull_name() for employee in self.employeeCharged]

        
class Area:
    def __init__(self, name, info):
        self.name = name
        self.info = info
        self.employees = []
        self.area_boss = None 
        
        print("\nInformación de conformación de áreas\n")
        
    def add_employee(self, employee):
        for emp in self.employees:
            if emp == employee:
                print(f"El empleado ya se encuentra dentro de la base de datos dentro del área: {self.name}")
                return
        self.employees.append(employee)
        print(f"El empleado {employee.getFull_name()} ha sido agregado exitosamente a la base de datos dentro del área de: {self.name}, a cargo del jefe {self.get_area_boss()}")
        
    def del_employee(self, employee):
        for emp in self.employees:
            if emp.id == employee.id:
                self.employees.remove(emp)
                print(f"El empleado {emp.getFull_name()} ha sido eliminado del área: {self.name}")
                return
        print(f"El empleado con identificado con id {employee.id}, no se encuentra registrado en el área {self.name}")
        
    def del_boss(self, boss):
        if self.area_boss and self.area_boss.id == boss.id:
            self.area_boss = None
            print(f"El jefe {boss.getFull_name()} ha sido eliminado del área: {self.name}")
        else:
            print(f"El jefe con identificado con id {boss.id}, no se encuentra registrado en el área {self.name}")
        
    def get_asign_boss(self, boss):
        if isinstance(boss, Boss):
            self.area_boss = boss
            print(f"El jefe: {boss.getFull_name()} está asignado al área de: {self.name}")
          
    def get_area_boss(self):
        return self.area_boss.getFull_name() if self.area_boss else "No hay ningún jefe asignado al área\n"
    
    def get_info(self):
        employees_str = ", ".join(self.get_employees()) or "Ninguno\n"
        boss_str = self.get_area_boss()
        return f"Área: {self.name}, Info: {self.info}\n Jefe de área: {boss_str}, Empleados del área: {employees_str}.\n"
        
    def get_employees(self):
        return [employee.getFull_name() for employee in self.employees]
      
print("\nCargue de (info) empleados:\n")
    
employee1 = Employee("Carito", "Barrantes", 33, 1350000, "09876", "2024-13-09")
employee2 = Employee("Lina", "Aguilar", 35, 1350000, "65432", "2024-19-08")
employee3 = Employee("Ana","Pérez", 25, 2500000, "24567", "2024-08-11")
employee4 = Employee("Milena", "Ibarra", 36, 1450000, "36547", "2024-13-12")
employee5 = Employee("Aleja", "Hoyos", 32, 1150000, "26745", "2024-22-08")
employee6 = Employee("Joha","Quintero", 35, 2500000, "64583", "2024-08-10")

boss = Boss("Eliza", "Galíndez", 33, 4000000, "38643", "2024-01-20")
boss.add_employeeCharged(employee1)
boss.add_employeeCharged(employee2)
boss.add_employeeCharged(employee3)

boss1 = Boss("Sonia", "Monsalve", 42, 4000000, "64758", "2024-07-07")
boss1.add_employeeCharged(employee4)
boss1.add_employeeCharged(employee5)

boss2 = Boss("Lina", "Martínez", 36, 3500000, "75428", "2024-13-09")
boss2.add_employeeCharged(employee6)

area = Area("Mantenimiento", "Esta área se encarga del mantenimiento de maquinaria y del correspondiente a la planta")
area.get_asign_boss(boss)
area.add_employee(employee1)
area.add_employee(employee2)
area.add_employee(employee3)

area1 = Area("Operación", "Esta área se encarga de la operación de maquinaria 24/7")
area1.get_asign_boss(boss1)
area1.add_employee(employee4)
area1.add_employee(employee5)

area2 = Area("Desarrollo", "Esta área se encarga de la actualización del sistema operativo")
area2.get_asign_boss(boss2)
area2.add_employee(employee6)

print("\nInformación de empleados:\n")

print(employee1.getFull_info())
print(employee2.getFull_info())
print(employee3.getFull_info())
print(employee4.getFull_info())
print(employee5.getFull_info())
print(employee6.getFull_info())

print("\nInformación por áreas:\n")

print(area.get_info())
print(f"Información del jefe: {area.get_area_boss()}, {boss.getFull_info()}")

print(area1.get_info())
print(f"Información del jefe: {area1.get_area_boss()}, {boss1.getFull_info()}")

print(area2.get_info())
print(f"Información del jefe: {area2.get_area_boss()}, {boss2.getFull_info()}")

print("\n¿Qué operación desea hacer?\n")

listEmpl = []

class SimpleEmployee:
    def __init__(self, name, area):
        self.name = name
        self.area = area

def Show():
    k = 0
    while k < len(listEmpl):
        print(listEmpl[k].name, " ", listEmpl[k].area, " ")
        k += 1   
               
while True:
    print("\n\n1. Registrar empleado")
    print("2. Consultar listado")
    print("3. Eliminar empleado")
    print("4. Modificar empleado")
    print("5. Salir")
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        name = input("Nombre completo del empleado a registrar: ")
        area = input("Nombre del área en la que trabaja: ")
        employee7 = SimpleEmployee(name, area)
        listEmpl.append(employee7)
        print("Empleado guardado con éxito.")
    elif opcion == 2:
        Show()
    elif opcion == 3:
        name_eliminar = input("Ingrese el nombre del empleado a eliminar: ")
        for emp in listEmpl:
            if emp.name == name_eliminar:
                listEmpl.remove(emp)
                print(f"Empleado {emp.name} eliminado con éxito.")
                break
        else:
            print(f"No se encontró el empleado con nombre {name_eliminar}.")
    elif opcion == 4:
        name_modificar = input("Ingrese el nombre del empleado a modificar: ")
        for emp in listEmpl:
            if emp.name == name_modificar:
                emp.name = input("Ingrese el nuevo nombre: ")
                emp.area = input("Ingrese la nueva área: ")
                print(f"Empleado {name_modificar} modificado con éxito.")
                break
        else:
            print(f"No se encontró el empleado con nombre {name_modificar}.")
    elif opcion == 5:
        break
    else:
        print("Opción no válida.")
