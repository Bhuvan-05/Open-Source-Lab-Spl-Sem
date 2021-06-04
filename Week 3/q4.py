# Provide an implementation for filter using list comprehensions

def even(n):
    if n%2:
        return True
    return False

list_1 = [int(i) for i in range(1,6)]

# Filtering even numbers only
list_2 = list(filter(even, list_1))
print(list_2)