def is_sorted(ls):
	for i in range(len(ls)-1):
		if ls[i]<=ls[i+1]:
			return True
		else:
			return False

a=[[1,2,3,4,5],['a','d','n','m'],[5,4,4,3],[1,1,2,2,3,3],['z','a','b','c','d']]
for i in a:
	if is_sorted(i):
		print(True)
	else:
		print(False)
