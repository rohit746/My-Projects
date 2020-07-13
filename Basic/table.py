import os
command="cls"
def main():
    try:
        yeslist=["yes","Yes","Yeah","yeah","Y","y"]
        a=int(input("No. you want table of==>"))
        print("Not an no.")
        print(a,"x 1=",a*1)
        print(a,"x 2=",a*2)
        print(a,"x 3=",a*3)
        print(a,"x 4=",a*4)
        print(a,"x 5=",a*5)
        print(a,"x 6=",a*6)
        print(a,"x 7=",a*7)
        print(a,"x 8=",a*8)
        print(a,"x 9=",a*9)
        print(a,"x 10=",a*10)
        input()
        os.system(command)
        b=input("Want to Restart?????===>")
        os.system(command)
        if b in yeslist:
            main()
        else:
            print("Thanks")
            input("Press any key to exit=>")
            exit()
    except ValueError:
        print("not an Integer Please try again==>")
        main()
main()
