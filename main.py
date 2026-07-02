from erm import EmployeeDetails
obj=EmployeeDetails()
while True:
    print("---EMPLOYEE RECORD MANAGEMENT---")
    print("1.Add employee details")
    print("2.Display Details")
    print("3.Search Details")
    print("4.Update Details")
    print("5.Delete Details")
    choice=int(input("Enter your choice"))
    if choice==1:
        obj.add_employee()
    elif choice==2:
        obj.display_employee()
    elif choice==3:
        obj.search_employee()
    elif choice==4:
        obj.update_employee()
    elif choice==5:
        obj.delete_employee()
    elif choice==6:
        print("Thank you") 
        break
    else:
        print("Invalid choice")   