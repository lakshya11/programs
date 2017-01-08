class AreaDescriptor(object) :   # if object class is not inherited then when square.area is called it will return <__main__.AreaDescriptor instance at 0xb720ccac>

	def __get__(self,instance,type=None):
		if instance is None :
			return self
		else :
			return instance.side ** 2

	def __set__(self,instance,value):
		instance.side = value
	


class Square(object):
	area = AreaDescriptor()
	

square = Square()
square.side = 5
print type(square.area).mro()
print square.area
print square.__dict__
a = AreaDescriptor()
b=a.__get__(square)
print b

