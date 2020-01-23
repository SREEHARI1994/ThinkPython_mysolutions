import time
f=open('words.txt')
words1=[]
start=time.time()
for line in f:
    line=line.strip()
    words1=words1+[line]
stop=time.time()
print("the time for normal method is %f ms" % (stop-start))
print(words1[:15])
words2=[]


start=time.time()
for line in f:
    line=line.strip()
    words2.append(line)

stop=time.time()
print("the time for append method is %fms" % (stop-start))
print(words2[:15])