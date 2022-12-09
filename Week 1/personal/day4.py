#fizzBuzz program details
#divisible by 3, print fizz
#divisible by 5,print fuzz
#divisible by both 3 and 5, fizzBuzz
#if divisible by none, print as it is

#solution:
#for input number, we use loop
#use conditional statement to check divisiblity

for i in range(1,100):
    if i%3==0 and i%5==0:
        print('fizzbuzz');
    elif i%3==0:
        print('fizz');
    elif i%5==0:
        print('buzz');
    else:
        print(i);

