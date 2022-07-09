'''
Thats some nice fizzbuzz u got there
'''

fb = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
def fizzbuzz():    
    for i in fb:
        if i %3==0 and not i%5==0:
            print('Fizz')
        elif i %5==0 and not i%3==0:
            print("Buzz")
        elif i %3==0 and i %5==0:
            print("FizzBuzz")
        else:
            print(i)
fizzbuzz()