import string


data = open('98-0.txt')
#create empty dictionary
dictt = {}
for line in data:
    line = line.translate(line.maketrans('.,/?!-', '      '))
    #split line into list
    lyst = line.split(' ')
    #if word in line is a key in dict, value + 1
    #else add word with default value of 1
    for word in lyst:
        if word in dictt.keys():
            dictt[word] += 1

        else:
            dictt[word] = 1

data.close()
print(dictt)
