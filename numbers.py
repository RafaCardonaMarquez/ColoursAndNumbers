file = open("numbers[2479].txt")

# every line extracted from the file converted to integer and added to the list
listNumbers = []
for line in file:
    listNumbers.append(int(line))

# sort the list in ascending order to later compare the index value with the number in that index to find the missing number,
# and have already ordered dictionaries in ascending order when we create them using an already ordered list.
listNumbers.sort()

# Question 1
# to find the number that repeats the most:
# create a variable that will hold all digits in the file
stringNumbers = ""

# iterate over the list of numbers created add every number to the empty string
# at the end of this loop we will have a string variable that will hold all the numbers in the file together with no spaces
for digit in listNumbers:
    stringNumbers += str(digit)


# create a dictionary that will hold as keys, the digits in the file and, as values, the number of times each digit appears in the file
dictNumbers = {}

# iterate over the string of numbers and check if the current digit is already in the dictionary as a key,
# if it is not already in the dictionary, we add it as a key an set its value equal to 1, 
# as this would be the first time we find this digit in the string
for number in stringNumbers:
    if number not in dictNumbers:
        dictNumbers[number] = 1
    else:
    # if the digit is already in the dictionary increase by 1 the number of times we have found the digit, represented by its key.
        dictNumbers[number] += 1

# to answer question 1, we select and display in the console,
# the key with the maximum value, wich means the digit that appeared the most in the file.
mostEncounteredDigit = max(dictNumbers, key=dictNumbers.get)
print(f"Number that appears the most in the file: {mostEncounteredDigit}")  # In this case, digit 1.

# Question 2
# to find the missing number, 
# loop over the list of lines created when reading the file
for i in listNumbers:
    # check if the current iteration value (i), which will be equal to the index of the current item in the list,
    # is not equial to the (value inside this index -1).
    # after sorting the list when we created it, 
    # the indexes and values won't match by one (for the index 0 the value stored will be the value of the index +1) by default.
    # we need to find the momment our list and values are not off by 1 anymore,
    # this would mean we have skipped a number, the number missing)
    if i != listNumbers[i] - 1:
        # store in a variable the current value -1
        # (our missing number is the number before the value of the current index position)
        missingNumber = listNumbers[i] - 1

        # exit the loop when the condition is met, only the first number that meets this condition is our missing number, assuming we only miss one.
        break

# Question 2
# to answer question 2, we display in the console the number stored in the missingNumber variable.
print(f"The number missing is: {missingNumber}")  # in this case 1469.
