def addition1(num1, num2, *args):
  sum = num1 + num2;

  if (len(args) > 0):
    for i in args:
      sum += i;

  return sum;


print(addition1(1, 3, 1, 4))