'''
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
��
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point.
If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2
'''

#Solution 1 --> Mine

import math

lines = {'UP':0,"DOWN":0,"LEFT":0,"RIGHT":0}
new_line = []
while True:

    line = input()
    if line:
        new_line = line.split(" ")
        lines[new_line[0]] += int(new_line[1])
    else:
        break

newTuple = (lines['UP'] - lines['DOWN'], lines['LEFT'] - lines['RIGHT'])
print (int(math.sqrt((newTuple[0]**2)+(newTuple[1]**2))))

#solution 2

import math
pos = [0,0]
while True:
    s = raw_input()
    if not s:
        break
    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])
    if direction=="UP":
        pos[0]+=steps
    elif direction=="DOWN":
        pos[0]-=steps
    elif direction=="LEFT":
        pos[1]-=steps
    elif direction=="RIGHT":
        pos[1]+=steps
    else:
        pass

print int(round(math.sqrt(pos[1]**2+pos[0]**2)))
