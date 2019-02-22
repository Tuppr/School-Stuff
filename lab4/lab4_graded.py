# Lab 4 GRADED exercises
# Return only this script file

def letterCount (s1,s2):
    for i in range(0,len(s2)):
        letter = 0
        for j in range(0,len(s1)):
            if s2[i] == s1[j]:
                letter+=1
        print(s2[i], letter)    
    
def fibonacci (n):    
    a = 0
    b = 1
    c = 0   
    while c < n:
        print(a,end=',')
        d = a + b
        a = b
        b = d
        c += 1
  
def  oddChecker (t):
    a= list(t)
    for i in a:
        if i%2!=0:
            print(i)


#############################################################################
#   !!! You Can Change the parameters below to test your code!!!
#############################################################################

print ("\n**************************************")
s1 = "do you want to go to the movies tonight"
s2="qwerty"
print ("The result of letterCount ")
letterCount (s1,s2)

print ("\n**************************************")
n=10
print ("The result of fibonacci ")
fibonacci (n)

print ("\n**************************************")
t = (1,2,3,5,8,22,35,92,123)
print ("The result of oddChecker ")
oddChecker (t)    

print ("\n**************************************")