# Reverse a string using a for loop without using [::-1] or reversed().
str = input('Enter the string:')
rev_str = ''
for char in str:
  rev_str = char + rev_str
print(rev_str)

# we used loop to iterate each char from string and continue add char with rev_str