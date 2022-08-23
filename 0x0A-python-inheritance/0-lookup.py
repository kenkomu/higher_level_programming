#!/usr/bin/python3
class Number :
      
    # Class Attributes
    one = 'first'
    two = 'second'
    three = 'third'
      
    def __init__(self, attr):
        self.attr = attr
          
    def lookup(obj): 
        print(obj.one, obj.two, obj.three, obj.attr)
          
n = Number(2)
n.lookup()
