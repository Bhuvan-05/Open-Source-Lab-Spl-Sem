#Provide an implementation for map using list comprehensions.

def square(n):
    return n*n

list_1 = [str(i) for i in range(1, 6)]      #['1','2',...'5']

list_2 = list(map(int, list_1))             #[1,2,3,4,5]

#squaring each element of list
list_2 = list(map(square, list_2))
print(list_2)