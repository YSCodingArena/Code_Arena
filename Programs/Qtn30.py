
import random


print (round(random.random()*100, 2)) # to generate a random float where the value is between 10 and 100 using Python math module

print (random.sample(range(100), 5)) # to generate a list of random values.

asd = random.sample(range(100), 5)

print (random.choice(asd), end ="\n-----------------------\n") # to pick random number from list

print (random.randrange(7,16)) # to pick random number in given range
