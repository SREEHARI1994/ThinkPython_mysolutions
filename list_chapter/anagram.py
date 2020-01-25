#f=open("words.txt")
def is_anagram(first,second):
	f=list(first)
	s=list(second)
	f.sort()
	s.sort()
	print(f)
	print(s)
	check=True
	if len(f)!=len(s):
		return False
	for i in range(len(f)):
		
		if not f[i]==s[i]:
				check=False
	return check

a=input("Enter first word\n")
b=input("Enter second word\n")
if is_anagram(a,b):
	print("the two words are anagrams")
else:
	print("the two words are not anagrams")