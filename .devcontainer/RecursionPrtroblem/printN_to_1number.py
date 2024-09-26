#the function Print the number from 1 to n
def printN_To_1(n):
    if(n==1):
        print(n ,end=" ")
        return
    printN_To_1(n-1)
    print(n , end=" ")
#The function Print the number from n to 1
# def printN_To_1(n):
#     if(n==1):
#         print(n ,end=" ")
#         return
#     print(n , end=" ")
#     printN_To_1(n-1)

n= int(input("Enter the number : "))
print(f"The number from 1 to {n} is : ",end=" ")
printN_To_1(n)