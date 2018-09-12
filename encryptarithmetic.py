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
list_encrypted = []
for number in range (0, 26):
    list_Numbers.append(number)
#print(list_Numbers)
#print(ord('A'))
#print(ord('Z'))
for letter in range (65, 91):
    list_Alphabets.append(chr(letter))
#print(list_Alphabets)
#test_variable = list(zip(list_Numbers, list_Alphabets))
Jargon_Dictionary = dict(zip(list_Numbers, list_Alphabets))
#print(Jargon_Dictionary)
##---End of Task 1 ---------------------------------------------------
list_word_number = []
Input_Word = input("Enter the word to be encrypted")
Input_Number = input("Enter the number")
Input_Number = int(Input_Number)

for c in Input_Word:
    for key in Jargon_Dictionary.keys():
        val = Jargon_Dictionary[key]
        if c == val:
            list_word_number.append(key)
#print(list_word_number)
for num in range (0,len(list_word_number)):
    list_word_number[num]=list_word_number[num]+Input_Number
#print(list_word_number)
for number in list_word_number:
    for key in Jargon_Dictionary.keys():
        key1 = key
        if number == key1:
            list_encrypted.append(Jargon_Dictionary[key])
#print(list_encrypted)
print("The encrypted code is")
string_encrypted = "".join(str(x) for x in list_encrypted)
print(string_encrypted)