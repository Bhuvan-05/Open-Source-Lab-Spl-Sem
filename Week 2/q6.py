## Use Python Built-in Functions ‘open’, ‘read’, ‘’readline, ‘write’,’writeline’ to work with
##files.

# create new file (comment after creating once)
#f = open("names.txt", "x")

"""
#open this file and append
f = open("names.txt", "a")
f.write("New Line\n")
f.close()

#read from this file
f = open("names.txt")
print(f.read())
f.close()
"""

#only reads one line
f = open("names.txt")
print(f.readline())
f.close()

#write multiple lines
#f = open("names.txt", "a")
#f.writelines(["\nline1", "\nline2", "\nline3"])
#f.close()


#read from this file
f = open("names.txt")
print(f.read())
f.close()
