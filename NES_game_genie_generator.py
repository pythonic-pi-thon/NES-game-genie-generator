#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Please note this program requires gamegenie.py (reused under MIT license) as a
#dependency. Please esure it is present in python's root directory. 
#If not included with this script, you can download it here: 
#https://github.com/Jarhmander/gamegenie
#just remember to change the "xrange" in line 16 to "range" if you wish for it 
#to work in Python 3.
import gamegenie as gg
import random
list_codes = []

#opens and reads game genie codes from "source.txt", then puts them in a list
f = open("source.txt")
for line in f:
    list_codes.append(line.strip())
f.close()

#saves the length of the (input) code list as a variable
length = len(list_codes) - 1

#generates the number of codes specified by the user
x = 0
number_of_codes = int(input("How many codes would you like to generate? "))
while x < number_of_codes: 
    
    #takes two random codes from the list and combines the first 3 letters of one with the last 3 of another
    code = list_codes[random.randint(0, length)][:3] + list_codes[random.randint(0, length)][3:]
    
    #deciphers the code into an address and value
    a = gg.decode(code)
    
    #replaces the value with a random number between 1 and 255, then re-encodes
    print(gg.encode(a["address"], random.randint(0, 255)))
    
    x+= 1


# In[ ]:




