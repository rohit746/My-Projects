import os 
def main():
    try:
        command="cls"
        print("All mensuration Calculator")
        print("Enter 1>> To operation related to Circle")
        print("Enter 2>> To operation related to Square")
        print("Enter 3>> To operation related to Rectangle")
        print("Enter 4>> To operation related to Triangle")
        print("Enter 5>> To Exit")
        a=int(input("Enter ====>>"))
        os.system(command)
    except ValueError:
        os.system(command)
        print("~~~~~~~~~~~~~~~~ Please Enter a valid option ~~~~~~~~~~~~~~~")
        main()
    if a==1:
        def Circle():
            try:
                radius=int(input("Enter the Radius of the Circle ===>>"))
                print("Area =",3.14*radius*radius)
                print("Cirucumference =",2*3.14*radius)
                print("Diameter =",2*radius)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                input()
                os.system(command)
            except ValueError:
                print("~~~~~~~~~~~~~~~~ Please Enter a valid option ~~~~~~~~~~~~~~~")
                Circle()
        Circle()
        print("Enter 1>> To Exit")
        print("Enter 2>> To Use again operation related to circle")
        print("Enter 3>> To go back to main menu")
        back=int(input("Enter ===>>"))
        os.system(command)
        if back ==1:
            exit()
        elif back ==2:
            Circle()
        else :
            main()
    elif a==2:
        def Square():
            try:
                side=int(input("Enter the Side of the square ===>>"))
                print("Area of the Square =",side*side)
                print("Perimeter of the Square =",4*side)
                print("Diagonal of the Square=",1.414*side)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                input()
                os.system(command)
            except ValueError:
                print("~~~~~~~~~~~~~~~~ Please Enter a valid option ~~~~~~~~~~~~~~~")
                Square()
        Square()
        print("Enter 1>> To Exit")
        print("Enter 2>> To Use again operation related to Square")
        print("Enter 3>> To go back to main menu")
        back1=int(input("Enter ===>>"))
        os.system(command)
        if back1 ==1:
            exit()
        elif back1 ==2:
            Square()
        else :
            main()
    elif a==3:
        def Rectangle():
            try:
                l=int(input("Enter the Length of the Rectangle ===>>"))
                b=int(input("Enter the Breadth of the Rectangle ===>>"))
                print("Area of the Rectangle =",l*b)
                print("Perimeter of the Rectangle =",2*(l+b))
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                input()
                os.system(command)
            except ValueError:
                print("~~~~~~~~~~~~~~~~ Please Enter a valid option ~~~~~~~~~~~~~~~")
                Rectangle()
        Rectangle()
        print("Enter 1>> To Exit")
        print("Enter 2>> To Use again operation related to Rectangle")
        print("Enter 3>> To go back to main menu")
        back2=int(input("Enter ===>>"))
        os.system(command)
        if back2 ==1:
            exit()
        elif back2 ==2:
            Rectangle()
        else :
            main()
    elif a==4:
        def Triangle():
            try:
                b1=int(input("Enter the Base of the Triangle ===>>"))
                h=int(input("Enter the Hight of the Triangle ===>>"))
                print("Area of the Triangle =",h*b1/2)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                input()
                os.system(command)
            except ValueError:
                print("~~~~~~~~~~~~~~~~ Please Enter a valid option ~~~~~~~~~~~~~~~")
                Triangle()
        Triangle()
        print("Enter 1>> To Exit")
        print("Enter 2>> To Use again operation related to Triangle")
        print("Enter 3>> To go back to main menu")
        back2=int(input("Enter ===>>"))
        os.system(command)
        if back2 ==1:
            exit()
        elif back2 ==2:
            Triangle()
        else :
            main()
    else :
        print("~~~~~~~~~~~~~~~~ Please Enter a valid option ~~~~~~~~~~~~~~~")
        main()
main()
