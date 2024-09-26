import random
computer = random.choice([0, -1, 1])
youstr = input("Enter the your choise : ")
youDic = {"w": 1, "s": 0, "g": -1}
reversDic = {1:"Water", 0:"snack", -1:"gun"}
you = youDic[youstr]
print(f"Your choise: {reversDic[you]}\nComputer choise: {reversDic[computer]}")

if (computer == you):
     print("Its drow")
else:
     if(computer==-1 and you == 1):
        print("WOW! You win!")
     elif(computer==0 and you==1):
         print("WOW! You win! ")
     elif(computer==-1 and you==0):
         print("You lose!")
     elif(computer==0 and you==-1):
         print("WOW! you win!")
     elif(computer==1 and you==0):
         print("You lose!")
     elif(computer==1 and you==-1):
         print("you lose!")
     else:
         print("Somethings went wrong!")

         
     

     
     
    
