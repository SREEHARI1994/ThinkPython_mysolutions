from search_words import in_bisect

def interlock(t):
    res=[]
    for word in t:
        even=word[::2]
        odd=word[1::2]
        if in_bisect(t,even) and in_bisect(t,odd):
            res.append([word,even,odd])                
                       
    return res
        


f=open('words.txt')
words=[]

for line in f:
    line=line.strip()
    words.append(line)

print(interlock(words))