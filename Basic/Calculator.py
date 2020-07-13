import os
import platform
command="cls"
yeslist=["yes","y","yeah","Yes","Y","Yeah"]
alpha=["a"]
def main():
    try:
        print("Simple Calculator")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1. To Add")
        print("2. To Subtract")
        print("3. To Multiply")
        print("4. To Divide")
        print("5. To Exit")
        op=int(input("Choose the operation:"))
        if op==1:
            def add():
                try:
                    a=int(input("Enter No.1:"))
                    b=int(input("Enter No.2:"))
                    print("Addition is:",a+b)
                except ValueError:
                    print("~~~~~~Enter a no. only~~~~~~~~~~")
                    add()
            add()
        elif op==2 :
            def sub():
                try:
                    a1=int(input("Enter No.1:"))
                    b1=int(input("Enter No.2:"))
                    print("Subtraction is:",a1-b1)
                except ValueError:
                    print("~~~~~~~~~Enter a no. only~~~~~~~~~~~~~")
                    sub()
            sub()
        elif op==3 :
            def multi():
                try:
                    a2=int(input("Enter No.1:"))
                    b2=int(input("Enter No.2:"))
                    print("Multiplication is:",a2*b2)
                except ValueError:
                    print("~~~~~~~~~~~Enter a no. only~~~~~~~~~~~~~")
                    multi()
            multi()
        elif op==4 :
            def div():
                try:
                    a3=int(input("Enter No.1:"))
                    b3=int(input("Enter No.2:"))
                    print("Division is:",a3/b3 )
                except ValueError:
                    print("~~~~~~~~~~~~~~~~Enter a no. only~~~~~~~~~~~~~~~~~~~~~")
                    div()
            div()
        elif op==5 :
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Bye")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            exit()
        else :
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Invalid input")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            os.system(command)
            main()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        re=input("Do You Want to Restart??:")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        os.system(command)
        if re in yeslist:
            main()
        else :
            print("Bye")
            exit()
    except ValueError:
        os.system(command)
        print("Enter a valid input")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        main()
main()