import random

#lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'abcdefghijklmnopqrstuvwxyz'.upper()
number = '0123456789'
#symbols = """[]()*;/,._-'"""
all = upper + number
length = 8
password = ''.join(random.sample(all, length))
print(password)
