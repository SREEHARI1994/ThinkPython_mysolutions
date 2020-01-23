def in_bisect(t,word):
    a=0
    b=len(t)
    
    while a<b:
        mid=(a+b)//2
        if t[mid]==word:
            return mid
        if t[mid]<word:
            a=mid+1
        else:
            b=mid
    return False



f=open('words.txt')
words1=[]

for line in f:
    line=line.strip()
    words1.append(line)

print(in_bisect(words1,'dog'))    