'''
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200
...
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
'''
#Solution 1

bankLog = {'D':0, 'W':0}
while True:
    entry = input()
    if entry:
        s = entry.split(" ")
        bankLog[s[0]] +=int(s[1])
    else:
        break

print (bankLog['D']-bankLog['W'])

#Solution #2

netAmount = 0
while True:
    s = raw_input()
    if not s:
        break
    values = s.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation=="D":
        netAmount+=amount
    elif operation=="W":
        netAmount-=amount
    else:
        pass
print netAmount
