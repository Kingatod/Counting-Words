file = open("myfile.txt", "rt")
data = file.read()
words = data.split()

print('The number of words in the text file is:', len(words))