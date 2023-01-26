class EmployeeClass:
#Create a data member to count the number of Employees
    NoOfEmployees = 0
    salaries = []
    
#Create a constructor to initialize name, family, salary, department
    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
#Incrementing Employee Count        
        EmployeeClass.NoOfEmployees += 1
#Appending them to a list        
        EmployeeClass.salaries.append(self.salary)
#Create a function to average salary
    def average_salary(self):
        return sum(EmployeeClass.salaries) / EmployeeClass.NoOfEmployees   
#Create a Fulltime Employee class and it should inherit the properties of Employee class
class FulltimeEmployeeClass(EmployeeClass):
    pass
#Create the instances of Fulltime Employee class and Employee class and call their member functions
e1 = EmployeeClass("Revanth", "Bharadwaj", 8900, "IT")
e2 = EmployeeClass("Suresh", "Yadav", 2500, "IT")
e3 = EmployeeClass("Teju","Suryakantam",5730,"HR")
e4 = EmployeeClass("Pavan","Krishna",4700,"IT")
e5 = FulltimeEmployeeClass("Baba", "Ramdev", 8000, "HR")

#Using the same function in inherited class
print(e1.average_salary())
print(e5.average_salary())