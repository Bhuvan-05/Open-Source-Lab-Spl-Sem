##Write a program to print each line of a file in reverse order (backwards)

file = open("names.txt")

lines = file.readlines()

file.close()

for line in (lines):

    print(line[::-1])       #using splicing


