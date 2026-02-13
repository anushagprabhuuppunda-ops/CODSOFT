def one():
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))
    op=input("Enter an operation(+,-,/,*):")
    if op=="+":
        print(num1+num2)
    elif op=="-":
        print(num1-num2)   
    elif op=="/":
        if num2!=0:
            print(num1/num2)
        else:
            print("Cannot divide by zero")
    elif op=="*":
        print(num1*num2)
    else:
        print("Invalid operation")
        
while True:
    try:
        print("Enter your choice:")
        print("1.Calculate")
        print("2.Exit")
        choice=int(input("Enter your choice:"))
        if choice==1:
            one()
        elif choice==2:
            print("Are you sure you want to exit?")
            ch=int(input("1.No\n2.Yes\nEnter a number:"))
            if ch==1:
                continue
            elif ch==2:
                print("Thank you and bye!~")
                break
                
        else:
            print("Please choose between 1 and 2!")
    except:
        print("Invalid choice")

            
