file = open("colours[2478].txt")

#used the strip and split method to remove empty spaces and comas from the file.
colorsArray = []
for line in file:
    lineNoSpaces = line.strip()
    listColorInLine  = lineNoSpaces.split(",")
    colorsArray.append(listColorInLine)

#dictionary that will store 
# as keys, the colors in the file and 
# as values, the ammount of times each color was found in the file.
colorsDictionary = {}

#dictionary that will store 
# as keys, the colors in the file and 
# as values, in how many lines each color has appeared.
linesContainingEachColor = {}


greenButNotBlue= 0
sameColorLine = 0
differentColorLine = 0
linesWithAlphabeticalPair = 0

# read each colour in the file by iterating over every line, and for every line, every word in the line.
for singleLine in colorsArray:

    # questions 1 and 2
    # when we encounter a color we add it to the dictionary that will hold number of times it appears in the file, 
    # if it's already added we just add 1 its value.
    for color in singleLine:
        if color not in colorsDictionary:
            colorsDictionary[color] = 1
            #we also add the new color to the second dictionary, wich will later hold in how many lines each color appeared.
            #we also fill the keys for this dictionary in this loop, 
            # so we will only have to iterate over the whole file once.
            linesContainingEachColor[color] = 0
        else:
            colorsDictionary[color] += 1

    # we check and add to the second dictionary the ammount of lines each color has appeared on
    for colorKey in linesContainingEachColor.keys():
        if colorKey in singleLine:
            linesContainingEachColor[colorKey] += 1
    # when we finish iterating over the file we would have created a dictionary with every color and the ammount of times each one appears,
    # and a second dictionary with all the colors in the file and in how many lines each one appeared on.

    #question 3
    #using "in", "and" and "not in" on every line, we check if the current line contains GREEN but not BLUE
    #when the condition is met we add 1 to the variable that keeps track of how many times we find a line the meets this contidion.
    if "GREEN" in singleLine and "BLUE" not in singleLine:
        greenButNotBlue += 1

    #question 4
    #using .count() function on every line we check if the first element in the line is repeated across the whole line,
    #if it does, the line contians a single color repeated.
    #using count() and len() instead of the hardcoded value (3), 
    # allows us to use the code even if the number of items per line were to change at some point.
    colorOcurrencesInLine = list(singleLine).count(singleLine[0])
    if colorOcurrencesInLine == len(singleLine):
        # add 1 to the variable that keeps track of the lines that meet this confition
        sameColorLine += 1

    #question 5
    # using the not equal operator we check if the colors in each line are all different from each other. 
    # if they are, we add 1 to the variable that keeps track of how many times we find a line the meets this contidion.
    elif singleLine[0] != singleLine[1] and singleLine[0] != singleLine[2] and singleLine[1] != singleLine[2]:
        differentColorLine += 1

    #question 6
    #using the < operator on strings and the "or" operator, we check if there is at least a pair of colours ordered alphabeticaly,
    #using the lesser than operatos with strings, Python will compare the ASCII values of the first character in the string (color).
    #if a string is lesser than the next, means they are ordered alphabetically,
    # then we will add one to the counter that keeps track of how many times we encounter a line that meets this condition.
    if singleLine[0] < singleLine[1] or singleLine[1] < singleLine[2]:
        linesWithAlphabeticalPair += 1

    
# Question 1
# to answer question 1, we select and display from the first dictionary created,
# the key with the maximum value, wich means the color that appeared the most in the file.
mostEncounteredColor = max(colorsDictionary, key=colorsDictionary.get)
print(f"Color that appears the most in the file: {mostEncounteredColor}")# in this case, RED

# Question 2
#to answer question 2, we select and display from the second dictionary created, 
#the key with the minimum value, wich means the color that appeared in the fewest ammount of lines.
colorInFewestNumberOfLines= min(linesContainingEachColor, key=linesContainingEachColor.get)
print(f"Color that appears in the fewest number of lines: {colorInFewestNumberOfLines}")#in this case, MAGENTA

# Question 3
# print the variable that holds the number of lines that contain GREEn but not BLUE
print(f"Lines containing GREEN but not BLUE: {greenButNotBlue}")# 1332

# Question 4
# print the variable that holds the number of lines that contain three of the same color
print(f"Lines with three times the same color: {sameColorLine}")# 526

# Question 5
# print the variable that holds the number of lines that contain three different colors
print(f"Lines with three different colors: {differentColorLine}")# 1114

# Question 6
# print the variable that holds the number of lines that contain at least a pair of colors in alphabetical order
print(f"Lines with at least one pair in alphabetical order: {linesWithAlphabeticalPair}")# 3185




