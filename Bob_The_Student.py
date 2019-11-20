class Student(object):
    def __init__(self,age=14,height=62,weight=120,haircolor="brown",political="neutral",eyecolor="Brown"):
        self.age=age
        self.height=height
        self.weight=weight
        self.haircolor=haircolor
        self.political=political
        self.eyecolor=eyecolor
    def birthday(self):
        self.age+=1
    def grow(self,growth):
        self.height+=growth
    def eat(self,how_much):
        self.weight+=how_much
    def exercise(self,minuets):
        factor=minuets/30
        self.weight-=factor
    def poop(self):
        self.weight-=2
    def dye(self,color):
        self.haircolor=color
    def news(self, leaning):
        self.political=leaning
    def contacts(self,color):
        self.eyecolor=color