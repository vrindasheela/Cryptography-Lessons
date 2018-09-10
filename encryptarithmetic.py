##---------workflow-----
##---------Create a List for Numbers
##---------Create another list for Letters
##---------Find the ASCII value of A and Z using ord() function
##---------zip(a, b) aggregates the two iterbles a and b as a single one .
##---------dict() constructes a dictionary
##---------map(). Map takes a function and an iterable as arguments. 
##---------map applies the function passed to it to every item of the iterable and returns a list.
##---------alphabet = map(chr, range(65, 91))
##---------Merge the two lists to a dictionary
list_Numbers = []
list_Alphabets = []
for number in range (0, 26):
    list_Numbers.append(number)
print(list_Numbers)
print(ord('A'))
print(ord('Z'))
for letter in range (65, 91):
    list_Alphabets.append(chr(letter))
print(list_Alphabets)
#test_variable = list(zip(list_Numbers, list_Alphabets))
Jargon_Dictionary = dict(zip(list_Numbers, list_Alphabets))
print(Jargon_Dictionary)
##---End of Task 1 
val = None
for key in Jargon_Dictionary.keys():
    val = Jargon_Dictionary[key]
    print(val)
#Word = raw_input("Enter the word to be encrypted")
#def encryption_func():





