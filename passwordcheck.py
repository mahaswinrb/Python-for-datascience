'''
 Author:  ---

 Exercise 00.5
 Sample progam

 This program takes a set of potential passwords from the user and print
     only those that are acceptable To qualify they need to have

1. At least 1 letter between [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]
2. At least 1 number between [0,1 2, 3, 4, 5, 6, 7, 8, 9]
3. At least 1 letter between [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z]
4. At least 1 character from [$, #, @]
5. Minimum length of transaction password: 6
6. Maximum length of transaction password: 12


'''
# importing a function to create some of the lists of validation characters
import string

# the following function validate an input password
def pword_validation (single_pword):
    if len(single_pword) < 6 or len(single_pword) > 12:
        return 'N'
    input_list = list(single_pword)
    # the following list will contain the OK/notOK for the single validation tests
    #   it has been initialized with all "N" values
    OKs_list = ['N', 'N', 'N','N']
    for elem in input_list:
            if elem in small_letters_list:
                OKs_list[0] = ('Y')
            if elem in numbers_list:
                OKs_list[1] = ('Y')
            if elem in  capital_letters_list:
                OKs_list[2] = ('Y')
            if elem in special_characters_list:
                OKs_list[3] = ('Y')
    #print 'validation_score: ', OKs_list, 'for the pword', single_pword
    if 'N' in OKs_list:
        return 'N'
    else:
        return 'Y'

# the following are the plain-lists version of the acceptable characters
'''
# the following is a no function version
small_letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
capital_letters_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
'''
# the following is a function-based version
small_letters_list = list(string.ascii_lowercase)
capital_letters_list = list(string.ascii_uppercase)
numbers_list = list(string.digits)

# no string function for the required subset of special characters
special_characters_list = ['$', '#', '@']

# the following is taking the input passwords
print '\nPlease enter the list of the passwords to be checked, separated by comma'
passwords_list = [x for x in raw_input().split(',')]

# the following print an introductory message and then check the single passwords
print '\nThe following are the passwords that have been accepted:\n'
for pword in passwords_list:
    return_value = pword_validation(pword)
    if return_value == 'Y':
        print '->', pword
    else:
        continue

print '\n ---end of the process---\n'