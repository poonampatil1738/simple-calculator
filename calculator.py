num1=float(input("enter first number="))
num2=float(input("enter second number="))
print("enter your choice")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")
choice=int(input("enter your choice="))
if(choice==1):
   add=num1+num2
   print("The result of addition is=",add)
elif(choice==2):
   sub=num1-num2
   print("The result of substration is=",sub)
elif(choice==3):
   mul=num1*num2
   print("The result of multiplication is=",mul)
elif(choice==4):
   if num2!=0:
       div=num1/num2
       print("The result of division is=",div)
   else:
       print("Error:cannot divide by zero")
else:
    print("invalid input!Please enter 1,2,3 or 4")       



   
