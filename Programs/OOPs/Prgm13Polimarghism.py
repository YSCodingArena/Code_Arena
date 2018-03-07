from _ast import Attribute
class snakeMovement:
    'This class about moving right or left of snake'
    
    def moveRight(self):
        print ("Snake moved right!")
        
    def moveLeft(self):
        print ("Snake moved left!")
        
        
class fishMovement:
    'This class about moving left and right of fish'
    
    def moveRight(self):
        print ("Fish moved right!")
        
    def moveLeft(self):
        print ("Fish moved left!")
        

def commonFunc(action):        # using common function to handle both instances and whihc as same methods within.
    action.moveRight()
    action.moveLeft()
    
anaconda = snakeMovement()
shark = fishMovement()

commonFunc(anaconda)
commonFunc(shark)
