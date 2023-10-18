# Assignment of the Week2_day1

# 1. Accept two user ages as inputs and give us the difference between them. 
# (The Answer should always be a positive output)

user1_age = int(input("Enter the age of user 1: "))
user2_age = int(input("Enter the age of user 2: "))

# Calculate the abosolute age difference
age_diff = abs(user1_age - user2_age)
print(f" the difference between user1 and user2 is", age_diff, "years.")
print('\n')

#  2. Accept 3 user inputs for variables named noun, verb and adjective. 
#  Print out a formatted string using the outputs.

noun = input("Please, Enter a noun: ")
verb = input("Please, Enter a verb: ")
adjective = input("Please, Enter an adjective: ")

formatted_string = f"The {noun} {verb} {adjective}"
print(formatted_string)
print('\n')

# 3. Take in a users input for their age, 
# if they are younger than 18 print kids, 
# if they're 18 to 65 print adults, 
# else print seniors

# Take in a user's age as input
age = int(input('Enter your age: '))

# Check the age and catagoried the user
if age < 18:
    print('kids')
elif 18 <= age <= 65:
    print('adult')
else:
    print('seniors')
print('\n')

# 3. Take in a number from a user input, 
# output the number squared.

# take a user to enter a number
number = int(input("Enter a number: "))

# print the square of the number
squared_number = number**2 
print('\n')

square = 5**2
print(square)
print('\n')

# Check the below variables' length. 
# If the length of the word is greater than 5 
# output True, 
# if it is less than 5, 
# output False
word1 = "panini"
word2 = "bulbasaur"
word3 = "pie"
word4 = "dolphin"
word5 = "dog"

# check the length of a word.
def check_length(word):
# args:
    # word: the word to check the length of.
#Returns:
    #True if the length of the word is greater than 5, 
    # if it is less than 5, print False

    return len(word) > 5

# check the length of each of word and print the result.
print('length of {} is greater than 5: {}'.format(word1, check_length(word1)))
print('length of {} is greater than 5: {}'.format(word2, check_length(word2)))
print('length of {} is greater than 5: {}'.format(word3, check_length(word3)))
print('length of {} is greater than 5: {}'.format(word4, check_length(word4)))
print('length of {} is greater than 5: {}'.format(word5, check_length(word5)))


