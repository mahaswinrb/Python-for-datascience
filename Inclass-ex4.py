'''
Author:  ---

Exercise 00.4
Sample progam

This program takes 3 numbers from the user and print
    - the factorial for the first one,
    - the solution of the linear equation created from the other 2 numbers

'''

# this function checks if a value is numeric
#   if yes, returns 'y', if not 'n'
def is_numeric(value):
    try:
        float(value)
        return 'y'
    except:
        return 'n'

# this recursive function calculates n!
def factorialize (num) :
    if num == 0:
        return 1 # 0! is equal 1
    else :
        return num * factorialize(num - 1) # implementing recursion


# this function calculates the solution of the linear equation
#   a*x + b = 0
def linear_equation (num_list):
    solution = -float(num_list[2])/float(num_list[1])
    return solution



# initializing a list containing the 3 numbers
numbers_list = []

# populating the list with the user input
counter = 0 # initializing a counter
while counter <= 2: #looping to get the numbers and use them to populate a list
    print '\nPlease, enter a number (', counter + 1, 'out of 3 )'
    num_in = raw_input('  -> ')
    if is_numeric(num_in) == 'y':
        numbers_list.append(int(num_in))
        counter += 1
    else:
        continue

# printing the factorial for the 1st number
print '\n---The factorial for the number', numbers_list[0], 'is', factorialize(numbers_list[0])

# calling the function for the summation and multiplication of the input numbers
linear_equation_solution = linear_equation (numbers_list)

# printing the results
print '\n---The solution of the linear equation from the second two numbers is', linear_equation_solution

print '\n---end of the process---\n'