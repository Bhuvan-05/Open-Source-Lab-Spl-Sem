##Write a program to find anagrams in a given list of words.

def is_anagram(str1,str2):
    return sorted(str1) == sorted(str2)

def iterate(list1):
    for i in range(1,len(list1)):
        if is_anagram(list1[i-1],list1[i]):
            list2.append(list1[i-1])
            list2.append(list1[i])

    return list2

list1 = ['ate','eat','mellow','meow','madam','damam','cautioned','education']
list2 = []

print(iterate(list1))
