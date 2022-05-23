#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Please note this program requires gamegenie.py (reused under MIT license) as a
#dependency. Please ensure it is present in python's root directory. 
#If not included with this script, you can download it here: 
#https://github.com/Jarhmander/gamegenie
#just remember to change the "xrange" in line 16 to "range" if you wish for it 
#to work in Python 3.
import gamegenie as gg
import random
from collections import OrderedDict
list_codes = []
list_final = []

#opens and reads game genie codes from "source.txt", then puts them in a list
f = open("source.txt")
for line in f:
    list_codes.append(line.strip())
f.close()
length = len(list_codes) - 1
x = 0

#This controls how many iterations the program runs for. I've found that 300,000*(number of codes
#that you give the program as input) is a reasonable default that finds ~99.99% of the codes possible
#without an inordinately long runtime but feel free to experiment with lower values or with values 
#up to 1,000,000*(number of codes given as input) which is what I ended up using to produce an 
#exhaustive list.
number_of_codes = (length+1)*300000

#indicates how often to print out progress. Make this lower if you want more frequent progress 
#indicators, higher if you want them to be less frequent, or make higher than number_of_codes if 
# you want no progress indicator. Every 1,000,000 iterations is a reasonable default.
progress = 1000000

#Controls how many iterations pass before duplicates are removed. This prevents excessive
#memory usage from a very long list forming with very little cost to runtime. 10,000,000 is a 
#reasonable default. 
remove_duplicates = 10000000

while x < number_of_codes:
    
    #takes two random codes from the list and combines the first 3 letters of one with the last 3 of 
    #another
    code = list_codes[random.randint(0, length)][:3] + list_codes[random.randint(0, length)][3:]
    
    #deciphers the code into an address and value
    a = gg.decode(code)
    
    #replaces the value with a random number between 0 and 255, then re-encodes
    b = gg.encode(a["address"], random.randint(0, 255))
    
    #adds the code to a list
    list_final.append(b)
    
    #periodically prints out progress
    if x%progress == 0:
        print("progress: " + str(round(100*x/number_of_codes, 2)) +"%")
        
    #periodically removes duplicates 
    if x%remove_duplicates == 0:
        list_final = list(OrderedDict.fromkeys(list_final))
    x+= 1
    
#indicates to the user that the codes are finished generating
print("Codes generated. Removing duplicates and sorting.")

#removes duplicates and sorts
list_final_2 = list(OrderedDict.fromkeys(list_final))
list_final_2.sort()

#writes the alphabetical list to a file
f = open("output.txt", "w")
for i in range(len(list_final_2)):
    f.write(list_final_2[i] + "\n")
f.close()
print("done")

