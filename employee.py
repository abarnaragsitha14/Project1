from abc import ABC,abstractmethod
class Employee(ABC):
    def __init__(self,ename,eid,dept,salary,joindate,phno,mailId):
        self.__ename=ename
        self.__eid=eid
        self.__dept=dept
        self.__salary=salary
        self.__joindate=joindate
        self.__phno=phno
        self.__mailId=mailId
       
    def get_ename(self):
        return self.__ename
    def set_ename(self,ename):
        self.__ename=ename
    def get_eid(self):
        return self.__eid
    def set_eid(self,eid):
        self.__eid=eid
    def get_dept(self):
        return self.__dept
    def set_dept(self,dept):
        self.__dept=dept
    def get_salary(self):
        return self.__salary
    def set_salary(self,salary):
        self.__salary=salary
    def set_salary(self,salary):
        self.__salary=salary
    
    def display(self):
        pass
        