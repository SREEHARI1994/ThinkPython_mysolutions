def invert_dic(d):
    inverse=dict()
    for key,val in d.items():
   

        inverse.setdefault(val,[]).append(key)
            
    return inverse


if __name__ == "__main__":


   
    d={'a':1,'b':1,'c':1,'d':5,'e':10,'f':5,'g':12}
    print(d)
    print(invert_dic(d))