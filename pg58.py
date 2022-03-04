import re
passw=input("enter the password")
f1=0
while True:
    if(len(passw)<8):
        f1=-1
        break
    elif not re.search("[a-z]",passw):
        f1=-1
        break
    elif not re.search("[A-Z]",passw):
        f1=-1
        break
    elif not re.search("[0-9]",passw):
        f1=-1
        break
    elif not re.search("[_@$]",passw):
         f1=-1
        break
    
