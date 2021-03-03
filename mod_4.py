#################Problem 1################################################################################
#1.	 Take a variable ‘age’ which is of positive value and check the following:
#a.	If age is less than 10, print “Children”.
#b.	If age is more than 60 , print ‘senior citizens’
#c.	 If it is in between 10 and 60, print ‘normal citizen’

age = int(input("Enter Age:"))
if age < 10:
    print("Children")
elif age > 60 :
    print("Senior citizen")
else :
    print("Normal Citizen")

#######################Problem 2 #################################################
#2.	Find  the final train ticket price with the following conditions. 
#a.	If male and sr.citizen, 70% of fare is applicable
#b.	If female and sr.citizen, 50% of fare is applicable.
#c.	If female and normal citizen, 70% of fare is applicable
#d.	If male and normal citizen, 100% of fare is applicable
#[Hint: First check for the gender, then calculate the fare based on age factor..
#For both Male and Female ,consider them as sr.citizens if their age >=60]

age1 = int(input("Enter the age:"))
gender = str(input("Enter the gender(M / F):"))
if age1 >= 60 and gender == 'M':
    print("70% fare on ticket")
elif age1 >= 60 and gender == 'F':
    print("50% fare on ticket")
elif age1 < 60 and gender == 'F':
    print("70% fare on ticket")
elif age1 < 60 and gender == 'M':
    print("100% fare on ticket")
    
#################Problem 3#####################################################
#3.	Check whether the given number is positive and divisible by 5 or not.  
num = float(input("Enter a number:"))
if num > 0:
    print("Number is positive")
    if num % 5 == 0:
        print("Divisible by 5")
    else :
        print("Not divisible by 5")        
else:
    print("Number is negative")
    if num % 5 == 0:
        print("Divisible by 5")
    else :
        print("Not divisible by 5")
################################END#################################################