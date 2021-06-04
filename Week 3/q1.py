##Write a program to count frequency of characters in a paragraph.
import collections
import pprint
text_input = "This is a sample input text to count frequency of each character"
count = collections.Counter(text_input.upper())
value = pprint.pformat(count)
print(value)