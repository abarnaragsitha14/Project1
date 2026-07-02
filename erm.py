from employee_rec import EmployeeRecord
from payroll import Payroll
class EmployeeDetails:
    def __init__(self):
        self.records=[]
        self.payroll=Payroll()
    def add_employee(self):
        ename=input("employee name:")
        eid=int(input("Emp id:"))
        for emp in self.records:
            if emp.get_eid()== eid:
                print("Employee ID already exists!")
                return
        salary=float(input("employee salary:"))
        dept=input("enter employee dept:")
        joindate=input("enter joining date:")
        phno=int(input("Enter Employee Phno:"))
        mailId=input("enter Employee MailId:")
        emp=EmployeeRecord(ename,eid,dept,salary,joindate,phno,mailId)
        self.records.append(emp)
        print("Employee Details added")
    def display_employee(self):
        for emp in self.records:
            emp.display()
    def search_employee(self):
        em_id=int(input("enter employee id to be searched:"))
        for emp in self.records:
            if emp.get_eid()==em_id:
                emp.display()
                return
        print("Employee not found")   
    def update_employee(self):
        em_id=int(input("enter employeeID to be updated:"))
        for emp in self.records:
            if emp.get_eid()== em_id:
                emp.ename=input("Enter new name")
                emp.set_salary(float(input("enter new salary")))
                emp.dept=input("enter dept name")
                emp.joindate=input("enter join date")
                emp.set_phno(int(input("enter the Phone Number")))
                emp.set_mailId(input("enter mailId"))
                print("updated successfully")
                return
        print("Employee not found")
    def delete_employee(self):
        em_id=int(input("enter employee id"))
        for emp in self.records:
            if emp.get_eid()==em_id:
                self.records.remove(emp)
                print("Deleted Successfully")
                return
        print("Employee not found")
    def payroll_manage(self):
            eid=int(input("Enter Employee id:"))
            for emp in self.records:
                if emp.get_eid()==eid:
                    allowance = float(input("Allowance: "))
                    deduction = float(input("Deduction: "))
                    net = self.payroll.calculate_salary(
                    emp.get_salary(),allowance,deduction)
                    print("\n------ PAYSLIP ------")
                    print("Employee :", emp.ename)
                    print("Basic Salary :", emp.get_salary())
                    print("Allowance :", allowance)
                    print("Deduction :", deduction)
                    print("Net Salary :", net)
                    return
            print("Employee not found")
                
            

    def highest_salary(self):
        if len(self.records) == 0:
            print("No employees")
            return

        highest = self.records[0]

        for emp in self.records:

            if emp.get_salary() > highest.get_salary():
                highest = emp

        print("Highest Paid Employee")
        highest.display()
    


        
