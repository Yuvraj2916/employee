employee=[]
print("    :-   MENU:")
print("1. ADD EMPLOYEE DATA")
print("2. DELETE EMPLOYEE DATA")
print("3. DISPLAY EMPLOYEE DATA")
print(" ")
while True:
    ch=int(input("Enter your choice:"))
    if ch==1:
        while True:
            a=int(input("Enter employee number:"))
            b=input("Enter employee name:")
            c=input("Do you want to add another record:")
            s=[a,b]
            employee.append(s)
            if c in "yesYESy":
                  continue
            else:
                break
    elif ch==2:
        if employee==[]:
            print("Stack empty")
        else:
            pop=employee.pop()
            print("Deleted element:",pop)
    elif ch==3:
        l=len(employee)
        for i in range(l-1,-1,-1):
            print(employee[i])
    else:
        print("Wrong choice")
        
