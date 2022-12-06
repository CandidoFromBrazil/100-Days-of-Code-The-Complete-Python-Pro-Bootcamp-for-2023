#FizzBuzz for job interview

fizz = "Fizz"
buzz = "Buzz"
for item in range(1, 101):
  if item % 3 == 0 and item % 5 == 0:
    print(fizz + buzz)
  elif item % 3 == 0:
    print(fizz)
  elif item % 5 == 0:
    print(buzz)
  else:
    print(item)
