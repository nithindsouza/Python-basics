################################Program 1############################################
# 1.	For the dataset “Indian_cities”, 
# a)	Find out top 10 states in female-male sex ratio
# b)	Find out top 10 cities in total number of graduates
# c)	Find out top 10 cities and their locations in respect of  total effective_literacy_rate.

import pandas as pd
city = pd.read_csv("C:/Users/hp/Downloads/Python Problem Statements/Indian_cities.csv")#loading the dataset to variable called city

top_state_sex_ratio = city.nlargest(10 , "sex_ratio")[["state_name" , "sex_ratio"]]#getting top 10 sex_ratio values and printing them along state_name

top_city_total_graduates = city.nlargest(10 , "total_graduates")[["name_of_city" , "total_graduates"]]#getting top 10 values of total_graduates and printing them along name_of_city 

top_city_effective_literacy_total = city.nlargest(10 , "effective_literacy_rate_total")[["name_of_city" , "location" , "effective_literacy_rate_total"]]
#getting top 10 values of effective_literacy_rate_total and printing them along name_of_city and location
                                                                                                                
########################Program 2####################################################
# 2.	For the data set “Indian_cities”
# a)	Construct histogram on literates_total and comment about the inferences
# b)	Construct scatter  plot between  male graduates and female graduates

import matplotlib.pyplot as plt
plt.hist(city["literates_total"])
#inferences about above histogram:
        #"literates_total" is positively skewed
        #most of the values lies in the range if 0.1*1e7 to 1.1*1e7
        #there are presence of outliers
        
plt.scatter(city["male_graduates"] , city["female_graduates"])
#inferences about above scatterplot:
    #positive associtation since y increases as x increases
    #Strong association which is very predictable
    #linear association
    #here its difficult to say about outliers
    #we can cluster them by 2, one is data points which are tooo clumzy and other is data points which are spreaded
    
##################################Program3############################################
# 3.	For the data set “Indian_cities”
# a)	Construct Boxplot on total effective literacy rate and draw inferences
# b)	Find out the number of null values in each column of the dataset and delete them.

plt.boxplot(city["effective_literacy_rate_total"])
    #there are presence of outliers
    #distribution is negatively skewed
    #Quartile 1(25%) is 81
    #Quartile 3(75) is 98
    #median(50%) is 85
    #least oiutlier is 49

city.isna().sum() #finding out number of null values in each column 
city.dropna()   #droping na values in the dataset

