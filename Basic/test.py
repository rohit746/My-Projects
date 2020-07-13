def main():
    def base():
        try:
            print("Welcome to this advance calculator made my Rohit")
            num1 = int(input("Number 1 -->"))
            sign = input("Sign -->")
            num2 = int(input("Number 2 -->"))
            if sign == "+" or sign == "-" or sign == "*" or sign == "/":
                yes = input("Do you want to Claculat %s%s%s -=>"%(num1,sign,num2)).lower()
                if yes == "yes":
                    def add():
                        if sign == "+":
                            result = int(num1) + int(num2)
                            print("The result is -=> %s"%(result))
                    add()
                    def sub():
                        if sign == "-":
                            result = int(num1) - int(num2)
                            print("The result is -=> %s"%(result))
                    sub()
                    def multiply():
                        if sign == "*":
                            result = int(num1) * int(num2)
                            print("The result is -=> %s"%(result))
                    multiply()
                    def div():
                        if sign == "/":
                            result = int(num1) / int(num2)
                            print("The result is -=> %s"%(result))
            else:
                base()
        except ValueError:
            main()
    base()
main()
        
