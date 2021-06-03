##prints lines of file in reverse order

file = open("names.txt")

lines = file.readlines()

file.close()

for line in reversed(lines):

    print(line)


