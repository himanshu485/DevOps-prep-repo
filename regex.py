#findall
import re 

text = "The rain in Spain stays mainly in the plain"
pattern = r"stays"
search_result = re.findall(pattern, text)
if search_result:
 print("Pattern found:", search_result) 

else:
    print("Pattern not found.")


import re

text = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")




#match 

import re
 
text = "I will definately get job i will do hardwork how much i can do "
pattern = r"job"
 
match = re.match(pattern, text)
if match :
   print("matched:", match)
else:
   print("match not found")


import re

text = "The quick brown fox"
pattern = r"quick"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")



import re

text = "The rain in Spain stays mainly in the plain"
pattern = r"rain"

replacement = "snow"
new_text = re.sub(pattern, replacement, text)
print ("New text:", new_text)


import re 

text = "let me give some time to analyze the problem in my life"
pattern = r"in"
 
search = re.search(pattern, text)

if search:
     print("Pattern found:", search.group())
else:
     print("Pattern not found.")



#split

import re

text = "himanshu,pujari,is,a,good,person"
pattern = r","
split = re.split(pattern, text)
print("Split result:", split)
