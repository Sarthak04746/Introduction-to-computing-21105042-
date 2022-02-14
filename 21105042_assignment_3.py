###Q1: Python program to count the number of occurences of each word or character in the string entered by the user

print("\t Question 1 \n")

# Taking input string form user to count letters and then converting all upercase letters to make code case insensitive.

user_input = input("Enter the string: ")
user_input = user_input.lower()

print()

count_dict = {}        # Created an empty dictoinary for counting a particular word.

# spliting the string in list of words
user_words = user_input.split(" ")

# checking whether input is a single word or not so that we will be able to count diff char if string is of single word
if len(user_words) == 1:
    user_words = user_input

# usering for loop to count the occurance of words and characters.

for word in user_words:
    if word in count_dict:
        count_dict[word] += 1
    else:
        count_dict.update({word : 1})

# printing the result.

if len(user_input) == 0:
    print("No word or sentence found.")
else:
    print("Number of each word/character in string is:" ,count_dict , "\n")

###################################################################################################################

###Q2:  Write a Python program to print the next date of the input date.

print("\t Question 2 \n")


# Taking date from user.
date = int(input("Enter the date: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))
print()

# Condition for valid dates.
check_1 = (month in (1,3,5,7,8,10,12) and (1 <= date <= 31))
check_2 = (month in (4,6,9,11) and (1 <= date <= 30))
check_3 = ((year % 4) == 0 and month == 2 and (1 <= date <= 29)) or ((year % 4) != 0 and month == 2 and (1 <= date <= 29))

# Calculating next date.
if (check_1 or check_2 or check_3) and (1800 <= year <= 2025): # checking whether date is valid or not. 
    
    # calculating next date for months having 31 days.
    if month in (1,3,5,7,8,10):
        if date < 31:
            date += 1
        else:
            date = 1
            month += 1

    # Calculating next date for month having 30 days.
    elif month in (4,6,9,11):
        if date < 30:
            date += 1
        else:
            date = 1
            month += 1

    # Calculating next date for feb because it have only 28 days.
    elif month == 2:

        # calculating next date in case of leap year.
        if year % 4 == 0:
            if date < 29:
                date += 1
            else:
                date = 1
                month += 1
        else:
            if date < 28:
                date += 1
            else:
                date = 1
                month += 1

    # Calculating next date for dec.
    else:
        if date < 31:
            date += 1
        else:
            date = 1
            month = 1
            year += 1
    
     # Printing next date.
    if date == 1 and month == 1 and year == 2026:
        print("Next date is out of range.")
    else:
        print(f"Next day is: {date}/{month}/{year}")

else:
    # printing if date is not valid.
    print("Invalid Date.")
   
#####################################################################################################################

 ###Q3:  Write a pyhton code to create a list of tuples with the first enlement as the number and the second as
 ###     the square of the number.

print("\t Question 3 \n")

# initialising the input and output list.
given_list = []
output_list = []

# taking list from user.
max_input = int(input("Enter the total number of terms you gonna enter: "))
print()
for i in range(max_input):
    tmp_num = int(input(f"Enter the {i + 1} number: "))
    given_list.append(tmp_num)
print()

# appling for loop to calculate square of each item in given_list and add that in output_list as tuple.
for num in given_list:
    temp_tuple = (num,num*num)
    output_list.append(temp_tuple)

# Printing the final result.
print(output_list)

#####################################################################################################################

###Q4: Program to prompt the user to for a grade between 4 and 10. If the grade is out of range print error message.
###    If the grade is between 4 and 10 print the grade and performance using thhw index.

print("\t Question 4 \n")

# prompting user for entering the grade.
grade_num = int(input("Enter the grade number: "))
print()

# checking grade is valid or not.
if 4 <= grade_num <= 10:

    # Printing the result depending upon the input grade.
    if grade_num == 10:
        print("Your grade is 'A+' and Outstanding Performance.")
    elif grade_num == 9:
        print("Your grade is 'A' and Excellent Performance.")
    elif grade_num == 8:
        print("Your grade is 'B+' and Very Good Performance.")
    elif grade_num == 7:
        print("Your grade is 'B' and Good Performance.")
    elif grade_num == 6:
        print("Your grade is 'C+' and Average Performance.")
    elif grade_num == 5:
        print("Your grade is 'C' and Below Average Performance.")
    else:
        print("Your grade is 'D' and Poor Performance.")

else:

    # Printing the error msg if grade is invalid.
    print("Entered grade is out of range.")


#######################################################################################################################
###Q5: Write a python program to input the following pattern')

print("\t Question 5 \n")    

#initialising the printing string

string="ABCDEFGHIK"

#using loop to print the strings.

j=0
for row in range(1,7):
    for column in range(0,row-1):
        print(' ',end='')

    s=string[0:11-j]
    print(s)
    j+=2

########################################################################################################################

###Q6:Write a python script that repeatedly ask user to enter name and SID of students. Store them in a dictionary
#####keys are SID's and values are students name. Perform the given operations on the dictionary.

print("\t Question 6 \n")    
 
# initialising the dictionary.
student_info = {}

# Creating dictionary by user input.
while True:

    # checking whether we have more input or not.
    check = input("Do you want to enter detials of student?(Y or N): ")
    print()

    if check == "Y":

        # Taking sid and names and adding them in dict.
        student_sid = int(input("Enter Student's SID: "))
        student_name = input("Enter student's name: ")
        student_info.update({student_sid : student_name})
        print()

    elif check == "N":

        # Breaaking while if user have no more input.
        break

    else:

        # Printing error msg if user input is anything else than Y or N.
        print("Please enter valid input.(Y or N)")
        print()

# part a
print("\t Part a \n")
print("Student detials are: ",student_info)

# part b
print("\n\t Part b \n")

# Making two different list of names and sids to sort them.
student_names = list(student_info.values())
student_sids = list(student_info.keys())

# sorting names list using inbuilt sort function.
sorted_names = sorted(student_names)

# iniliasing the sorted dict,
sorted_dict_by_names = {}

# putting sorted values in dict.
for name in sorted_names:
    for index in range(len(student_names)):
        if student_names[index] == name:
            sorted_dict_by_names.update({student_sids[index] : name})
        
#  printing the sorted dict by names.
print("Sorted dict using students names is: " , sorted_dict_by_names)

# part c.
print("\n\t Part c.\n")

# first we convert dict into type dict items then we sorted them and before printing we converted them back into class dict.
print("Sorted dict using students SID is: " , dict(sorted(student_info.items())))

# part d
print("\n\t Part d. \n")

# Searching and printing the student's name using his/her sid.
while True:

    # Taking student's sid.
    searching_sid = int(input("Enter the Sid whose name you want to search: "))
    print()
    # searching his/her name.
    if searching_sid in student_info.keys():

        # printing student's name if found and breaking the infinite loop.
        print(f"Student's name is: {student_info[searching_sid]}")
        break

    else:

        # printing a error msg if sid not found.
        print("Please enter a valid sid.")
        print()

######################################################################################################################


###Q7:Write a python program to print Fibonacci sequence.Also print average of the resultant Fibonacci series.

print("\t Question 7 \n")

# Defining rec function to print the fabonnic series.
def fibonacci_seq(n):
    if n <= 1:
       return n
    return(fibonacci_seq(n-1) + fibonacci_seq(n-2))

# initialising variables to find the average.
sum = 0
avg_counter = 0

while True:

    # Asking user for the max number of terms to print.
    max_num_of_terms = int(input("Enter the the max number of terms you want to print: "))
    print()

    # if max number is negative.
    if max_num_of_terms <= 0:
        print("Plese enter a positive integer")

    # printing fab series using above rec function.
    else:

        print(f"Fibonacci sequence with {max_num_of_terms} terms:")

        for count in range(max_num_of_terms):
            temp = fibonacci_seq(count)
            sum += temp
            avg_counter += 1
            print(temp)
        
        print()
        break

# Calculating average of fab series.
average_fab_seq = sum/avg_counter
print("Average of fab series is: ",average_fab_seq)

#####################################################################################################################

###Q8:Given the sets below, write python statement to
### Set1={1,2,3,4,5}
### Set2={2,4,6,8}
### Set3={1,5,9,13,17}

print("\t Question 8 \n")
# initialising the sets.
set_1 = {1,2,3,4,5}
set_2 = {2,4,6,8}
set_3 = {1,5,9,13,17}

# part a
print("\t Part a \n")

# here first we take union of set 1 and set 2 then subtract the output set from the intraction of set 1 and set 2
set_sol_a = (set_1 | set_2) - (set_1 & set_2)
print("Set having all the elemets of Set 1 and Set 2 but not both is:" ,set_sol_a)

# part b
print("\n\t Part b \n")

# here we substracted union of all set from intersecton of all possible pairs and also from intersection of all sets.
set_sol_b = (set_1 | set_2 | set_3)- (set_1 & set_2 & set_3) - (set_2 & set_3) - (set_3 & set_1) - (set_2 & set_1)
print("The set having elements that present only in one sets: ", set_sol_b)

# part c
print("\n\t Part c \n")

# here we first take intraction between all the pairs then union all output after that sub the output set form the intraction of all the sets.
set_sol_c = ((set_1 & set_2) | (set_2 & set_3) | (set_1 & set_3)) - (set_1 & set_2 & set_3)
print("The set of elements that are exactly two of the sets Set1, Set2 and Set3: ", set_sol_c)

# part d
print("\n\t Part d \n")

# here we substracted set 1 from a set having all the positive int upto 10.
set_sol_d = {1,2,3,4,5,6,7,8,9,10} - set_1
print("The set having all int less than equal to 10 except that are not in set_1: ",set_sol_d)

# part e 
print("\n\t Part e \n")

# here we substracted all sets from a set having all the positive int upto 10.
set_sol_e = {1,2,3,4,5,6,7,8,9,10} - set_1 - set_2 - set_3
print("The set having all int less than equal to 10 except that are not in all the sets: ",set_sol_e)

    



    
    



    
