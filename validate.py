class Validation:
    def validate_phone(phno):
        phno = str(phno)
        if len(phno) != 10:
            return False
        if not phno.isdigit():
            return False
        return True
   
