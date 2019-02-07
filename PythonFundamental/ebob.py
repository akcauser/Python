 
def x(x,y):

	while y!=0:

		(x,y)=(y,x%y)
		
	return x

print(x(2,3))
