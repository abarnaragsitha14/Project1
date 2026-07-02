from abc import ABC,abstractmethod
class Employee(ABC):
    def __init__(self,ename,eid,dept,salary,joindate,phno,mailId):
        self.ename=ename
        self.__eid=eid
        self.dept=dept
        self.__salary=salary
        self.joindate=joindate
        self.__phno=phno
        self.__mailId=mailId
    def get_eid(self):
        return self.__eid
    def set_salary(self,eid):
        self.__eid=eid
    def get_salary(self):
        return self.__salary
    def set_salary(self,salary):
        self.__salary=float(salary)
    def get_phno(self):
        return self.__phno
    def set_phno(self,phno):
        self.__phno=phno
    def get_mailId(self):
        return self.__mailId
    def set_mailId(self,mailId):
        self.__mailId=mailId
    def display(self):
        pass   
   
        