#!/usr/bin/env python
# coding: utf-8

# In[23]:


# Write a program to ask a student for their  percentage mark

mark_grade =float(input("what is your target grade: "))
total_pass_grade = 100
if (mark_grade >= 90) and mark_grade <= total_pass_grade:
    print("You have got A+")
elif mark_grade >= 80:
    print("You have got B")
elif mark_grade >= 70:
    print("You have got a C")
elif mark_grade >= 50:
    print("You have got a D")
        
else: 
    print("You did not make the cut off mark")
        
print(mark_grade)


# In[ ]:


# Write a program that allows you to enter 4 numbers and stores them in a file called 'numbers'
# 3, 45, 83, 21
nbr_file = open("numbers.txt", "w")
nbr_file = open("numbers.txt", "a")
nbr_file.write("3, 45, 83, 21")
nbr_file.close()


# In[9]:


# Write a program to ask a student for their percentage mark and convert this to a grade, use function called mark_grade

def mark_grade():
    mark_grade =float(input("what is your target grade: "))
    exam_pass_grade = 70
    percentage = 100
    
    if mark_grade > exam_pass_grade:
        print("You have got A+")
    elif mark_grade == exam_pass_grade:
        print("You have got A")
    elif mark_grade < exam_pass_grade:
        print("You did not make the cut off mark")
        
        
mark_grade()
        


# In[10]:


# Motorbike Depreciation

def function_1():
    bike_cost= 2000.00
    cost= bike_cost
    year = 0
    print("yearly depreciation of motorbike value:")
    
    while cost >= 1000.00:
        print("Year", year, ":", cost)
        year = year + 1
        cost = cost - (cost/10)
    
function_1()


# In[25]:


# Asking for 2 numbers from a user and using any of math operator selected by the user
def two_numbers():
    number_1 = int(input("Enter a first number? "))
    number_2 = int(input("Enter a second number"))
    print("Enter which operation you would like to perform? ")
    ch = input("Enter any of these operator +, -, *, /: ")
   
    if ch == "+":
        print (number_1 + number_2)
    elif ch == "-":
        print(number_1 - number_2)
    elif ch == "*":
        print(number_1 * number_2)
    elif ch == "/":
         print(number_1 / number_2)
       
    
two_numbers()


# In[ ]:


def procedure_1():
    name = input("What is your name? ")
    age = int(input("What is your age? "))
    
    print("Hello " , name , "! You will be" , age + 1, "For your next birthday!")

procedure_1()


# In[ ]:



    

