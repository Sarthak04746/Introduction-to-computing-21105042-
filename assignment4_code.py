#######################################################################################################################################################################################

#***** QUESTION-1 *****
# TOWER OF HANOI

print("\t \t \t Question-1 \n")

def Tower_of_Hanoi(n, source, destination, auxillary):
    if n==1:
        print("Move disc 1 from", source, "to", destination)         # only 1 move is required for n=1
    else:
        Tower_of_Hanoi(n-1, source, auxillary, destination)          # moves first (n-1) discs from source peg to auxillary peg
        print("Move disc", n, "from", source, "to", destination)     # moves the largest peg from source peg to destination peg
        Tower_of_Hanoi(n-1, auxillary, destination, source)          # moves the (n-1) pegs in auxillary peg to destination peg

n=int(input("Enter the number of discs: "))
Tower_of_Hanoi(n, 'A', 'B', 'C')                                     # A is peg-1 (source peg), B is peg-2 (destination peg), C is peg-3 (auxillary peg)

print("\n")

#######################################################################################################################################################################################
#***** QUESTION-2 *****
# PASCAL'S TRIANGLE

print("\t \t \t Question-2 \n")

from math import factorial, remainder
from tracemalloc import start
n=int(input('Enter the size of pascals triangle you want: '))

print("PASCAL TRIANGLE USING LOOPS")

for i in range(n):
	for j in range(n-i+1):
		print(end=" ") #for giving spacing in triangle

	for j in range(i+1):
		print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")	# nCr = n!/((n-r)!*r!)
	print()	# for new line
print("\n\n")

print("PASCAL TRIANGLE USING RECURSION")

def pascal_triangle(n,original_length=n):
    if n == 0:
        return
    pascal_triangle(n-1,original_length)
    print(' '*(original_length-n), end=' ')   #for print the spaces(" ")
    begin = 1                                #first number is always 1
    for i in range(1, n+1):

        print(begin, end =' ')
        
        begin = begin * (n - i) // i         #using Binomial Coefficient
    print()
pascal_triangle(n)
print("\n")

#######################################################################################################################################################################################


#***** QUESTION-3 *****
# BUILT-IN FUNCTIONS

print("\t \t \t Question-3 \n")

a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))

q=a//b
r=a%b
print("The quotient is", q, "and the remainder is", r)

# PART-(a)
# callable function checks if functions/values are callable or not
print(callable(q))
print(callable(r))

# PART-(b)
# check if values are non-zero or not
print(q!=0)
print(r!=0)

# PART-(c)
my_list=[q, r]+[4, 5, 6]                        # adding elements in list
print(my_list)
my_list=(list(filter(lambda i: i<=4, my_list))) # filters out values  greater than 4
print(my_list)

# PART-(d)
my_set=set(my_list)                             # makes set from list
print(my_set)

# PART-(e)
my_set=frozenset(my_set)                        # makes set immutable
print(my_set)       

# PART-(f)
max_num=max(my_set)                             # finds max value
print(max_num)
print(hash(max_num))                            # finds hash value
        
print("\n")

#######################################################################################################################################################################################


#***** QUESTION-4 *****
# CLASS STUDENT

print("\t \t \t Question-4 \n")

class Student:
    def __init__(self, student,roll_no):
        self.name = student
        self.roll_no = roll_no
    
    def __del__(self):
        print("Object destroyed")

#creating object
student_1 = Student("SARTHAK", 21105042)
print("Object created")                  #printing the assigned values
print(f"The name of the student it {student_1.name} and SID is {student_1.roll_no}.")
del student_1                             #deleting object
print("\n")

#######################################################################################################################################################################################

#***** QUESTION-5 *****
# CLASS EMPLOYEE

print("\t \t \t Question-5 \n")

class factory():                        # Creating a class names factory.

    def __init__(self,name,salary):     # Storing data of employees
        self.name = name
        self.salary = salary
        print(f"Object created named {self.name}.")

    def show_info(self):                # Data of employees
        print("\tShowing info of the employee.")
        print(f"Name of the employee working in this factory is {self.name}")
        print(f"Salary of {self.name} is {self.salary}.")

    def update_salary(self,new_salary): # Update the salary of employee
        self.salary = new_salary
        print(f"Updated salary of the employee {self.name} is {self.salary}\n")

    def __del__(self):                  # Deleting data of employee
        print(f"Record of the employee {self.name} is deleted.")
    
# Employees
Mehak = factory('Mehak', 40000)
Ashok = factory("Ashok", 50000)
Viren = factory('Viren', 60000)
print()

# DATA of employees
Mehak.show_info()
print()
Ashok.show_info()
print()
Viren.show_info()
print()

# Updating salary of employee
print("Updating mehak's salary.")
Mehak.update_salary(70000)

# Removing data of employee
print("Calling destructor to delete viren's record.")
del Viren

print("\n")

#######################################################################################################################################################################################

#***** QUESTION-6 *****
# ANAGRAM TEST

print("\t \t \t Question-6 \n")

george_word=input("Enter George's word: ")
barbie_word=input("Enter Barbie's word: ")

def anagrams(s):                            # function to find list of anagrams
    if s=="":
        return [s]
    else:
        ans=[]                              # list of anagrams
        for w in anagrams(s[1:]):           # iterates over anagrams of tail of the string
            for pos in range(len(w)+1):     # puts first letter in different positions in the anagrams of the remaining letters
                ans.append(w[:pos]+s[0]+w[pos:])
        return ans

correct_words=anagrams(george_word)
if barbie_word in correct_words:            # checks if Barbie's word is an anagram of George's word
    print("Friendship is True.")
else:
    print("Friendship is Fake.")
#######################################################################################################################################################################################

