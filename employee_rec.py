from employee import Employee
class EmployeeRecord(Employee):
    def display(self):
        print("Employee name:",self.ename)
        print("Employee id:",self.eid)
        print("Employee dept:",self.dept)
        print("Employee salary:",self.get_salary())
        print("JoiningDate:",self.joindate)
        print("RelievingDate:",self.relievedate)