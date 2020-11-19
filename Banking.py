import random

import time 

print("Welcome To Mallaya Bank:")
time.sleep(0.44)
print("")
print("")
print("TO CREATE AN ACCOUNT,WAIT FOR 5 SECONDS WITHOUT TERMINATION")
time.sleep(5)
print("Enter the Details as per your aadhar card")
time.sleep(3)
b=int(input("Enter your 16 digit AADHAR NUMBER:"))
b = str(b)
d = input("Enter Your Name:")
if len(b)==16:
   print('Yes, 16 numbers are there')
   print(d)

e=int(input("Enter your Indian Phone Number: +91"))    
c=input("Enter Your Plot number:")
f=input("Enter your street name:")
g=input("Enter your area name:")
h=input("Enter your City and State")
print("Congratulations" ,d, "Your account has been created in the name of:",d)
print("Your Mailing Address And Ph.no  Will be:",c,",",f,",",g,",",h,",",e)


anum=0
acc = ""
for i in range(13):
    num = (random.randint(0,9))
    acc += str(num)
print("Your new account number is     ",acc)
print("You will have a minimum account balance of Rs.500")
anum+=500
time.sleep(2)

print("Welcome Again:")
time.sleep(2)
print("ENTER 1 TO ATTAIN A DEBIT CARD OR A CREDIT CARD")
print("ENTER 2 TO APPLY FOR A LOAN:")
    
print("ENTER 3 FOR  WITHDRAWLS OR DEPOSITS")
print("ENTER 7 FOR FOREIGN EXCHANGE")
print("ENTER 8 TO KNOW ABOUT YOUR A/C STATUS/BALANCE  ")
    
output=int(input("Enter the required number:"))
   


if output==1:
    DE=""
    re=""
    DE=input("ENTER DR TO APPLY FOR DEBIT CARD,ENTER CR TO APPLY FOR CREDIT CARD:")
    if DE=="DR":
            
        re=int(input("Enter your account number:"))
        print("Welcome ",d)
        cx = ""
        for i in range(16):
            nume = (random.randint(0,9))
            cx += str(nume)
            print("Your new debit card  number is     ",cx )
            oo = ""
            for i in range(3):
                numer = (random.randint(0,9))
                oo += str(numer)
            print("Your CVV is:",oo)
            WE=input("IF YOU WANT YOUR OWN PIN NUMBER,TYPE'YES',ELSE TYPE 'NO':")
            if WE =='YES':
                ddd=int(input("Enter Your New Pin:"))
                print(ddd,"is your new pin")
            else:
                oo0 = ""
                for i in range(4):
                    numeroid = (random.randint(0,9))
                    oo0 += str(numeroid) 
                print(oo0,"is your pin number")
        else:
            eds=int(input("CREDIT CARD CHECK:Enter 1 if you are 21,and with  a job with a 6 digit income,,,if you have an exception press 2"))
            if eds==1:
                print("you are eligible")
                oo00 = ""
                for i in range(17):
                    numeroid = (random.randint(0,9))
                    oo00 += str(numeroid) 
                print(oo00,"is your credit card number:")
                WEd=input("IF YOU WANT YOUR OWN PIN NUMBER,TYPE'YES',ELSE TYPE 'NO':")
                if WEd =='YES':
                    dddi=int(input("Enter Your New Pin:"))
                    print(dddi,"is your new pin")
                else:
                        oo03 = ""
                        for i in range(5):
                                numeroid = (random.randint(0,9))
                                oo033 += str(numeroid) 
                        print(oo03,"is your pin number")
                oo11111=""
                for i in range(4):
                    numerthala = (random.randint(0,9))
                    oo11111 += str(numerthala)
                print("Your CVV is:",oo11111)

            else:
                print("Sorry,You aren't eligible")

elif output==2:
    print("You will only be considered as a loan candidate only if your CIBIL is above 580:")
    d09=int(input("ENTER YOUR CIBIL SCORE:"))
    if d09<=580:
        print("PLease have a minimum CIBIL score of 580 ")
    else:
        print("You are eligible")
        lml=int(input("Enter the amount you wish to take as a loan"))
        if lml<=400000:
            print("The loan amount has been transferred to your account")
            anum+=lml
            
      



         
    



