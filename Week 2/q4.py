##Write a function “lensort” to sort a list of strings based on length.

my_list = ['dddd','a','bb','ccc']

def lensort(x):
    return sorted(x, key=len)

print(lensort(my_list))

