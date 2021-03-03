#################################Problem 1#############################################
#1.	Construct 2 lists containing all the available data types  (integer, float, string, complex and Boolean) and do the following..
#a.	Create another list by concatenating above 2 lists
#b.	Find the frequency of each element in the concatenated list.
#c.	Print the list in reverse order.

lst1 = [24 , 25.5 , 'nithin' , 5+6j , True]
lst2 = [19 , 15.9 , 'dsouza' , 3+2j , False , 24 , False]

lst3 = lst1 + lst2#concatenating 2 lists
lst3

lst3.count(24)      #calculating frequency of each elements in lst3
lst3.count(25.5)
lst3.count('nithin')
lst3.count(5+6j )
lst3.count(True)
lst3.count(19)
lst3.count('dsouza')
lst3.count(3+2j)
lst3.count(False)

lst3.reverse()      #reversing a list
lst3

#################################Problem 2##################################################
#2.	Create 2 Sets containing integers (numbers from 1 to 10 in one set and 5 to 15 in other set)
#a.	Find the common elements in above 2 Sets.
#b.	Find the elements that are not common.
#c.	Remove element 7 from both the Sets.

set1 = {1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10}     #creating sets
set2 = {5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14 , 15}

inter = set1.intersection(set2)     #finding a common elements in sets
inter

notCom = set1^set2#elements that are not common
notCom

set1.discard(7)     #removing a element, here 7
set1
set2.discard(7)
set2

############################Problem 3################################################
#3.	Create a data dictionary of 5 states having state name as key and number of covid-19 cases as values.
#a.	Print only state names from the dictionary.
#b.	Update another country and it’s covid-19 cases in the dictionary.

dict1 = {'karnataka' : 45787 , 'kerala' : 45645 , 'tamilnadu' : 36547 , 'andrapradesh' : 65874 , 'goa' : 7548 }     
dict1

dict1.keys()    #printing keys in a dict

dict1['china'] = 8458745910     #updating a country and its covid numbers into existing dict 
dict1
#########################################END#########################################################