##Write a function “duplicate” to find all duplicates in the list.

def Duplicate(x):

    import collections
    print([item for item, count in collections.Counter(x).items() if count > 1])

my_list = [1,2,3,2,1,5,6,5,5,5]
Duplicate(my_list)
