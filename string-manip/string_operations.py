text = 'this is a sample text to perform some string operations'

#Capitalize the first letter
print(text.capitalize())

#Capitalize the first letter of every word
print(text.title())

#Uppercase all charachters
print(text.upper())

#Count all a's in the string
print(text.count('a'))

#Does the string start with "This"?
print(text.startswith('This'))

#Does the string start with "this"?
print(text.startswith('this'))

#Does the string end with "op"?
print(text.endswith('op'))

#Does the string start with "ons"?
print(text.endswith('ons'))

#Find the first occerance of character "s" in the string
print(text.find('s'))

#Find the first occerance of character "s" after the 20th index, in the string
print(text.find('s',20))

#Find the first occerance of character "z"
print(text.find('z'))

#Find the first occerance of character "s" in the string
print(text.index('s'))

#Seperate the string into words on the space character
print(text.split(' '))

#Seperate the string into words on the character "s"
print(text.partition('s'))

#Encode/Convert the string into HEX
print(text.encode('hex'))

#Replace the characters in the string
print(text.replace(' ','_'))