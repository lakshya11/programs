
'''
class Celsius:
	def __init__(self):
		self._temperature = 0;

	def __

c = Celsius()
print "initial temp",c._temperature
c._temperature = 300
print c._temperature
'''

class Square:
	def get_area(self):
		return self.side**2

square = Square()
print type(square)
print square.__dict__  # empty dictionary as of yet
square.side = 5
print square.get_area() #---> return 25
"""
 conclusion
	Get an attribute
		1)try in the __dict__ ---> a.__dict__['x']
		2) try in the type  ----->type(a).__dict__['x']
		3) raise the Attribute error

When getting the attribute
		__dict__[attribute]
When setting the attribute
		__dict__[attribute]= val
"""






