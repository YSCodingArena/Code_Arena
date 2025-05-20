import requests
import paramiko


class Queue:
    mobList = []

    def __init__(self, mobile, price):
        self.mobile = mobile
        self.price = price
        Queue.mobList.append(self.__dict__)

    def totalMobiles(self):
        print(Queue.mobList)

    def process(self):
        Queue.mobList.remove(self.__dict__)

 
mob1 = Queue("Redmi 5A", 10000)
mob1.totalMobiles()
mob2 = Queue("Samsung Galaxy", 12000)
mob3 = Queue("Apple X", 100000)
Queue.totalMobiles(mob1)
mob1.price = 9999
mob1.totalMobiles()
mob1.process()
mob1.totalMobiles()
