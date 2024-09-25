def gratest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else: 
        return c
a=int(input("Enter the nuber of a : "))
b=int(input("Enter the nuber of b : "))
c=int(input("Enter the nuber of c : "))
print(f"Greatest among the Three number is : {gratest(a,b,c)}")