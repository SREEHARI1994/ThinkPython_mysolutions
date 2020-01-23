import random

no_of_students=23
no_of_simulations=100000 

def generate_sample(n):
    
    birthdays=[]
    for i in range(n):
        birthdays.append(random.randint(1,365))
    return birthdays

def has_duplicates_my(birthdays):
   
    birthdays.sort()
  

    for i in range(len(birthdays)-1):
 
        if birthdays[i] == birthdays[i+1]:
            return True
   
    return False
        
  

def sampling(no_of_simulations):
    count=0
    for i in range(no_of_simulations):
        
        b=generate_sample(no_of_students)
      
        #print(b)
        if has_duplicates_my(b):
            count=count+1
    return count

no_of_same_birthdays = sampling(no_of_simulations)
prob=(no_of_same_birthdays /no_of_simulations)*100


print("the probability that two students will have the same birthday in a class of 23 is "
+ str(prob)+ " %")
print("or in other words, out of 10,000 random samples of 23 birthdays, two students had the same birthday in " + str(prob)
+ " % of the samples")