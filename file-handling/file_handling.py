#Creating new file
outputFile = open(r'temp_file.txt','w')

#write raw text
outputFile.write('This line is from string')

#write a list to file
text = ['This','line','is','from','a','list']
outputFile.writelines(text)

#write a list to file
text = ('This','line','is','from','a','tuple')
outputFile.writelines(text)

#close the file pointer
outputFile.close()

#read from the file
inputFile = open(r'temp_file.txt','r')
readText = inputFile.read()
print(readText)
inputFile.close()

#read file into seperate lines
inputFile = open(r'temp_file.txt','r')
readText = inputFile.readlines()
print(readText)
inputFile.close()

with open(r'temp_file.txt','w') as fo:
    fo.write('Sometext here.')

with open(r'temp_file.txt','r') as fo:
    print(fo.read())














