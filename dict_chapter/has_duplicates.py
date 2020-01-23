def duplicates(t):
    d={}
    for i in t:
        
        if i in d:
            return True
        d[i]="pappara"
    return False

print(duplicates([1,2,1,3,4]))
   
        