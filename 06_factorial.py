# Calculate the factorial of a number without using any built-in factorial function.
n = int(input('Enter the number:'))
total = 1
for i in range(1,n+1):
  total = total * i
print(f'The factorial of the number is {total}')

# took total = 1 and multiply with the range for that n it will give multiplication upto that n