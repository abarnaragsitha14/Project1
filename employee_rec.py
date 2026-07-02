from employee import Employee
class EmployeeRecord(Employee):
    def display(self):
        print("Employee name:",self.ename)
        print("Employee id:",self.get_eid())
        print("Employee dept:",self.dept)
        print("Employee salary:",self.get_salary())
        print("JoiningDate:",self.joindate)
        print("Employee phno:",self.get_phno())
        print("Employee Email:",self.get_mailId())