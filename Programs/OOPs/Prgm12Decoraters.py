#Decoraters

def outsideFunc(originalFunction):
    def insideFunc():
        print ("Inside Functions execute before calling {} function".format(originalFunction.__name__))
        originalFunction()
    return insideFunc

@outsideFunc # this means, we are passing the 'display' function as a argument to function 'outsideFunc'.
def display():
    print ("Now we are running Original Function")
    
#disc = outsideFunc(display)# This how we usuall call the function
#disc() # 'disc' will be waiting to be exeuted and when we use '()' automatically 'insideFunc' will execute.


display() # This how we usally call the decoraters functions

#disc() and display() both will give same result.
