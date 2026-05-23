str1 = "hello"
str2 = "world"
result = str1 + " " + str2
print(result)

text = " My name is himanshu pujari"
length = len( text)
print ( "length of string" , length)

text = "I am not getting job what should i do"
uppercase = text.upper()
lowercase = text.lower()
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)

text = " today is very good day"
new_text = text.replace("good" , "bad")
print(new_text)

text = " split this string into a list"
word_list = text.split()
print("list of words:" , word_list)

# strip 
text = "   This is a test string with spaces.   "
strip_text = text.strip()
print("oiginal_text:" , strip_text)

text = "   Some spaces around   "
stripped_text = text.strip()
print("Stripped text:", stripped_text)

text = "This is a test string."
substring = "test"
if substring in text:
    print (substring ,"found in the text.")
else:
    print(substring, "not found in the text.")



# float

num1 = 10.9
num2 = 20.89

result1 = num1 + num2
print("Addition:", result1)

result2 = num1 - num2
print("Subtraction:", result2)
 
result3 = num1 * num2
print("Multiplication:", result3)

result4 = num1 / num2
print("Division:", result4)

result5 = num1 % num2
print("Modulus:", result5)

#int 
num1= 23
num2 = 45
result1 = num1 + num2
print("Addition:", result1)

result2 = num1 // num2
print("Floor Division:", result2)   

result3 = num1 % num2
print("Modulus:", result3)

result4 = abs(-5)
print("Absolute Value:", result4)


import function.py
result = function.add(5, 3)
print("Result of addition:", result)