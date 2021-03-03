#################### problem1 ##################
#1.A) list1=[1,5.5,(10+20j),’data science’].. Print default functions and parameters exists in list1.
# B) How do we create a sequence of numbers in Python.
# C)  Read the input from keyboard and print a sequence of numbers up to that number

list1 = [1 , 5.5 , (10+20j) , 'data science']
dir(list1)# print default function and parameters exist in list1 

[x for x in range (1,100)] #creating sequence numbers


num = int(input("enter the number : "))#storing a value in variable called num
for num in range(1,num+1):#iteraring upto given number from 1
    print(num)#printing all iterated values
    
###################### problem2 ##################################################
# 2.Create 2 lists.. one list contains 10 numbers (list1=[0,1,2,3....9]) and other 
# list contains words of those 10 numbers (list2=['zero','one','two',.... ,'nine']).
#  Create a dictionary such that list2 are keys and list 1 are values..
    
list2 = [x for x in range(0,10)]#strong values from 0-9
list2
list3 = ['zero' ,'one','two','three','four','five','six','seven','eight','nine']#storing values as given in question
dict1 = {list3[i] : list2[i] for i in range(len(list3))}#creating a dictionary and storing list3 as keys and list2 as values
dict1
########################### problem3 #################################################
#3.Consider a list1 [3,4,5,6,7,8]. Create a new list2 such that Add 10 to the even number and 
#multiply with 5 if it is odd number in the list1..

list4 = [3,4,5,6,7,8]#storing values in list4 as given in question
list5 = []#decalring a list outside the loop globally
for i in range(len(list4)): #iterating values by lenghth of list4 times
    if list4[i]%2 == 0:#checking for even numbers
        a = list4[i]+10#adding  10 if its even
        list5.append(a)#appending in a list
    else:#for odd numbers
        b = list4[i]*5#multiplying by 5 if its odd
        list5.append(b)#appending in a list
print(list5)#printing the new updated list

########################## problem4 ##################################################
 # 4.Write a simple user defined function that greets a person in such a way that :
 # i) It should accept both name of person and message you want to deliver.
 # ii) If no message is provided, it should greet a default message ‘How are you’
 # Ex: Hello ---xxxx---, How are you  - default message.
 # Ex: Hello ---xxxx---, --xx your message xx---

def greetBot():#defing a user defined function using keyword def
    name = input("Enter the name :")#storing name in variable name
    msg = input("Type the message :")#storing message in variable called msg
    if msg =="":#checking for emty msg, if user enters without providing any message
        print("Hello "  +name+ ", How are you")#print the message as given in question
    else:# if user enters some message
        print("Hello " +name+ ", " +msg+ "")# greet with message provuded
greetBot()#calling a function

##########################################END###########################################
    
