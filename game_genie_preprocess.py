#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#This script takes a file "codes.txt" as input and saves a "cleaned" list of codes (ie all 6
#characters in length, all only using appropriate uppercase letters, and duplicates removed) to a 
#file named "codes_cleaned.txt" that can be renamed for use with NES_game_genie_generator or 
#NES_game_genie_list_gen (this is done to prevent it from overwriting or changing source.txt, if 
#it exists). It also prints out a summary of changes made. 
from collections import OrderedDict
list_codes = []
list_deleted = []
list_lower = []
list_changed = []
list_codes_cleaned = []

#saves a list of letters that aren't used and can be changed to "A"
list_forbidden = ["B", "C", "D", "F", "H", "J", "M", "Q", "R", "W"]

#reads "codes.txt" and saves each line to a list, ignoring lines that are only the newline character
f = open("codes.txt")
for line in f:
    if line != ("\n"):
        list_codes.append(line.strip())
f.close()

#records the beginning length of the list 
length = len(list_codes)

#removes codes that aren't six characters or contain characters other than letters
x = 0
while x < len(list_codes):
    if len(list_codes[x]) != 6 or list_codes[x].isalpha() == 0:
        list_deleted.append(list_codes[x])
        list_codes.remove(list_codes[x])
        x-= 1
    x+= 1

#capitalizes codes that contain lowercase letters
for i in range(len(list_codes)):
    if list_codes[i].isupper() == 0:
        list_lower.append(list_codes[i])
        list_codes[i] = list_codes[i].upper()

#searches codes for the letters found in list_forbidden and changes them to "A"
for i in range(len(list_codes)):
    count = 0
    code = ''
    for j in range(len(list_codes[i])):
        if list_codes[i][j] in list_forbidden:
            code = code + 'A'
            count+= 1
        else:
            code = code + list_codes[i][j]
    list_codes_cleaned.append(code)
    if count != 0:
        list_changed.append(list_codes[i])

#removes duplicates from the remaining/processed codes, 
#recording the number of codes present before and after removal
duplicate_count = len(list_codes_cleaned)
list_codes_cleaned = list(OrderedDict.fromkeys(list_codes_cleaned))
duplicate_count-= len(list_codes_cleaned)

#sorts the list
list_codes_cleaned.sort()

#writes the list of cleaned codes to a file
f = open("codes_cleaned.txt", "w")
for i in range(len(list_codes_cleaned)):
    f.write(list_codes_cleaned[i] + "\n")
f.close()

#prints out a summary of changes made or prints "No changes have been made."
print("The input file contained " +str(length) +" codes.\n")
if len(list_deleted) != 0:
    print("The following " +str(len(list_deleted)) +" codes were not six characters or \ncontained numbers or punctuation and have been removed:")
    print(list_deleted)
    print("")
if duplicate_count != 0:
        print(str(duplicate_count) +" codes were duplicated and have been removed.\n")
if len(list_lower) != 0:
    print("The following " +str(len(list_lower)) +" codes contained lowercase letters and have been capitalized:")
    print(list_lower)
    print("")
if len(list_changed) != 0:
    print("The following " +str(len(list_changed)) +" codes contained unacceptable characters and have been edited:")
    print(list_changed)
    print("")
if duplicate_count+len(list_changed)+len(list_deleted)+len(list_lower) == 0:
    print("No changes have been made.\n")
print("The following " +str(len(list_codes_cleaned)) +" codes have been saved:")
print(list_codes_cleaned)

