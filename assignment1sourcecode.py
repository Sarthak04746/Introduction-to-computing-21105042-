# # ASSIGNMENT - 1

###  1. Write a Python program to find average of three numbers entered by the user.  ###

### input from user ###
Numb1=float(input("Enter first number -"))
Numb2=float(input("Enter second number -"))
Numb3=float(input("Enter third number - "))

### formula ###
avg=(Numb1+Numb2+Numb3)/3


print("Average of three numbers is-",avg)


###  2. Write a python program to compute a person's income tax.... ###

### input from user ###
gross_income=float(input("enter Gross Income to the nearest penny -"))
dependents=int(input("enter the number of Dependents -"))

### formula ###
Taxable_income = gross_income - 10000 - (3000*dependents)
Tax=(Taxable_income*20)/100

if Tax<0:
    print("Your income tax is 0$")
else:
    print("Total tax is-",Tax)

####  3. Write a python program to store different data type values into a list. ####

### input from user ###
SID=int(input("Enter your SID-"))
name=input("Enter your name-")
gender=input("Enter your Gender-(M,F,U) -  ")
course=input("Enter the course name-")
cgpa=float(input("Enter the CGPA-"))

### list ###
Student=[SID,name,gender,course,cgpa]

print(Student)


####  4. Write a python program to enter marks of 5 students into a list and display them in sorted manner.####

### input from user ###
M1=float(input("Enter the marks in Subject 1 = "))
M2=float(input("Enter the marks in Subject 2 = "))
M3=float(input("Enter the marks in Subject 3 = "))
M4=float(input("Enter the marks in Subject 4 = "))
M5=float(input("Enter the marks in Subject 5 = "))

### list ###
Marks=[M1,M2,M3,M4,M5]
Marks.sort()
print(Marks)


####5.a) List: color ['Magenta', 'Green', 'White', 'Black', 'Pink', 'Yellow'] ####

color=['Magenta', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color.remove('Black')
print(color)


#### 5. b) List: color ['Magenta', 'Green', 'White', 'Black', 'Pink', 'Yellow'] ####

color=['Magenta', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color[3:5]=["Purple"]
print(color)





