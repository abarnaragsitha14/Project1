from employee_rec import EmployeeRecord
class EmployeeDetails:
    def __init__(self):
        self.records=[]
    def add_employee(self):
        ename=input("employee name:")
        eid=int(input("Emp id:"))
        for emp in self.records:
            if emp.eid== eid:
                print("Employee ID already exists!")
                return
        salary=float(input("employee salary:"))
        dept=input("enter employee dept:")
        joindate=input("enter joining date:")
        relievedate=input("enter relieve date:")
        emp=EmployeeRecord(ename,eid,salary,dept,joindate,relievedate)
        self.records.append(emp)
        print("Employee Details added")
    def display_employee(self):
        for emp in self.records:
            emp.display()
    def search_employee(self):
        em_id=int(input("enter employee id to be searched:"))
        for emp in self.records:
            if emp.eid==em_id:
                emp.display()
                return
        print("Employee not found")   
    def update_employee(self):
        em_id=int(input("enter employeeID to be updated:"))
        for emp in self.records:
            if emp.eid== em_id:
                emp.ename=input("Enter new name")
                emp.set_salary(float(input("enter new salary")))
                emp.dept=input("enter dept name")
                emp.joindate=input("enter join date")
                emp.relievedate=input("enter relieve date")
                print("updated successfully")
                return
        print("Employee not found")
    def delete_employee(self):
        em_id=int(input("enter employee id"))
        for emp in self.records:
            if emp.eid==em_id:
                self.records.remove(emp)
                print("Deleted Successfully")
                return
        print("Employee not found")    
    


        
