import os
command="cls"
ans=["a","A"]
anss=["b","B"]
ansss=["c","C"]
anssss=["d","D"]
score=0
def main():
    try:
        yeslist=["Yes","yes","Y","y","Yeah","yeah"]
        print("Welcome To Quize By Rohit")
        print("Enter 1> To Start")
        print("Enter 2> To Exit")
        q=int(input("Enter ==>"))
        os.system(command)
        if q==1:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Your First question is ==>")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("1.Which crop is sown on the largest area in India???")
            print("A.Rice")
            print("B.Wheat")
            print("C.Sugarcane")
            print("D.Maze")
            ans1=input("Enter Your Answer Here==>")
            os.system(command)
            if ans1 in ans:
                os.system(command)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("xxxxx+++++_______Wola! Your Answer is correct_________+++++++xxxxx")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                score=score+1
                print("Current score",str(score))
            else:
                os.system(command)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Sorry!Your answer is Wrong")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Current score",str(score))
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Your second question is")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("2.Entomology is the science that studies")
            print("A.Behaviour of human beings")
            print("B.Insects")
            print("C.The origin and history of technical and scientific terms")
            print("D.The formation of rocks")
            ans2=input("Enter Your Answer Here==>")
            os.system(command)
            if ans2 in anss :
                os.system(command)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Wola! Your Answer is correct")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                score=score+1
                print("Current score",str(score))
            else:
                os.system(command)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Sorry!Your answer is Wrong")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Current score",str(score))
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Your third question is")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("3.Grand Central Terminal, Park Avenue, New York is the world's")
            print("A.highest railway station")
            print("B.longest railway station")
            print("C.largest railway station")
            print("D.None of the above")
            ans3=input("Enter Your Answer Here==>")
            os.system(command)
            if ans3 in ansss :
                os.system(command)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Wola! Your Answer is correct")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                score=score+1
                print("Current score",str(score))
            else:
                os.system(command)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Sorry!Your answer is Wrong")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Current score",str(score))
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Your Fourth question is")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("4.Galileo was an astronomer who")
            print("A.developed the telescope")
            print("B.discovered four satellites of Jupiter")
            print("C.discovered that the movement of pendulum produces a regular time measurement")
            print("D.All the above.")
            ans4=input("Enter Your Answer Here==>")
            os.system(command)
            if ans4 in anss :
                os.system(command)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Wola! Your Answer is correct")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                score=score+1
                print("Current score",str(score))
            else:
                os.system(command)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Sorry!Your answer is Wrong")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Current score",str(score))
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Your Fifth question is")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("5.Corey Anderson who has hit the fastest ODI century in 36 balls is from")
            print("A.England")
            print("B.Australia")
            print("C.West Indies")
            print("D.New Zeland")
            ans5=input("Enter Your Answer Here==>")
            os.system(command)
            if ans5 in anssss :
                os.system(command)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Wola! Your Answer is correct")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                score=score+1
                print("Current score",str(score))
            else:
                os.system(command)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Sorry!Your answer is Wrong")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Your Final Score is:",str(score))
            resatrt=input("Do You Want to restart the game==>>")
            if resatrt in yeslist:
                os.system(command)
                main()
            else:
                os.system(command)
                print("Thankyou for Playling")
                input()
                exit()
        elif q==2:
                exit()
        else :
            print("Enter a Valid Option!!!")
            input("(Press Enter To Resatrt)==>")
            os.system(command)
            main()
    except ValueError:
        print("<<<<<<<<<<<<<< Enter a Valid Input >>>>>>>>>>>>>>>>>")
        main()
main()