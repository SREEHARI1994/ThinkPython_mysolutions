import time
def build_dict(f):
    words={}
    for line in f:
        line=line.strip()
        words[line]=""
    return words
    
def build_list(f):
    words=[]

    for line in f:
        line=line.strip()
        words.append(line)
    return words

    




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

        


f1=open('words.txt')
f2=open('words.txt')
d=build_dict(f1)
l=build_list(f2)
print(l[:5])
start=time.time()
print("zymurgy" in l)
stop=time.time()
print("the time for list is %f ms" % (stop-start))
start=time.time()
print("zymurgy" in d)
stop=time.time()
print("the time for dict is %f ms" % (stop-start))
start=time.time()
print(in_bisect(l,"zymurgy"))
stop = time.time()
print("the time for binary search is %f ms" % (stop-start))




