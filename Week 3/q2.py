##Write a program wrap.py that takes filename and number of characters per line (width)
##as arguments. The program must wrap the lines of the file longer than entered width.
import textwrap

width = int(input('Enter the width : '))

with open('file-for-q2.txt', 'r') as file:
    data = file.read().replace('\n', '')

wrapper = textwrap.TextWrapper(width)
word_list = wrapper.wrap(data)


for item in word_list:
    print(item)