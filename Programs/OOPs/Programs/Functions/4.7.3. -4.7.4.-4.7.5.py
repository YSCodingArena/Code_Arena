def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))
    

def concat(*args, sep="/"):
    return sep.join(args)


>>> list(range(3, 6)) # normal call with separate arguments
[3, 4, 5]
>>> args = [3, 6]
>>> list(range(*args)) # call with arguments unpacked from a list
[3, 4, 5]

def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")
    
def make_incrementor(n):
    return lambda x: x + n

