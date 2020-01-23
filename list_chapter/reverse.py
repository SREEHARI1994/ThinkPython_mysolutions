def reverse_pair(words):
    res=[]
    for word in words:
        index=in_bisect(words,word[::-1])
        if index>=0:
            res.append([word,words[index]])

    return res
    
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
    return -1


f=open('words.txt')
words1=[]

for line in f:
    line=line.strip()
    words1.append(line)

print(reverse_pair(words1))