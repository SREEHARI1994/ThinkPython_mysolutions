def chop(ls):
	del ls[0]
	del ls[len(ls)-1]
	return None

t=[1,2,3,4,5,6]
chop(t)
print(t)