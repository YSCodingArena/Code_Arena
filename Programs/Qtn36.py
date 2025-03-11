class Queue:

    def __init__(self):
        self.EmpCount = []

    def add(self, *args):
        self.EmpCount.append(args)

    def process(self):
        if len(self.EmpCount) > 0:
            del self.EmpCount[0]
        else:
            print("Queue is Empty. Can't process further!!")

    def display(self):
        if len(self.EmpCount) > 0:
            print("Here is the list:\n", "\n".join(map(str, self.EmpCount)))
        else:
            print("Nothing is here to display!!")


q1 = Queue()
q1.add("Hemanth Kumar Y S", 160000)
q1.add("Prahibha", 50000)
q1.add("Naveen", 150000)
q1.display()
# print (globals().keys())
q1.process()
q1.display()
q1.process()
q1.display()
q1.process()
q1.display()
q1.process()
