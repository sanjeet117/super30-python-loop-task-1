# Take an integer n and print its multiplication table from 1 to 20.
n = int(input('Enter the number:'))
for i in range(1,21):
  print(f'{n} * {i} = {n*i}',end = ' ')

# input function takes input from user in string format convert it in integer by using int
# took range from 1 to 21 and multiply i with the each element in that range