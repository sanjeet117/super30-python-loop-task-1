'''
Given

numbers = [12, 7, 9, 20, 33, 42, 8, 15]

Print only the numbers divisible by 3.
'''
numbers = [12, 7, 9, 20, 33, 42, 8, 15]
for i in numbers:
  if i % 3 == 0:
    print(i,end = ' ')

# used modulus operator for finding remainder if remainder is 0 means it is devided by 3