def cumsum(col):
	csum=0
	new=[]
	for i in range(len(col)):
		csum=csum+col[i]
		new[i]=csum
	return new
	

t=[1,2,3,4,5,6,7]
print(cumsum(t))
