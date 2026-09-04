# Count how many vowels exist in a user-provided string.
str = input('Enter the string:')
str = str.lower()
count = 0
for i in str:
  if i in ('a','e','i','o','u'):
    count = count + 1
print('The count of vowel in string is:',count)

# took input from user lower the string iterate each element of the string through loop
# and searched against vowels then print count



