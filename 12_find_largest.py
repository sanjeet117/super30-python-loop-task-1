# Find the largest number from a list without using max().
L = [1,2,3,4,5,9,11]
largest = L[0]
for i in L:
  if i > L[0]:
    largest = i
print('The largest of list is:',largest)

# through the  loop we compare each element with the largest if any found that will be largest