#!/usr/bin/python3
class emp: 
    name='Harsh'
    salary='25000'
    def lookup(obj): 
        print (obj.name) 
        print (obj.salary) 
e1 = emp()  
print (getattr(e1,'name')) 
print (hasattr(e1,'name')) 
setattr(e1,'height',152)  
print (getattr(e1,'height')) 
delattr(emp,'salary') 