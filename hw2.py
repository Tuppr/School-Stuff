################################################################################
# HW2, CS103 Spring 2019
# name:
# blazerid:
################################################################################

import math      # you may need the math module to answer some of the questions


######################################################################
# HW2 PROBLEMS
######################################################################

# check hw2.pdf file to see implemented test cases and expected outputs

def p(x): # this is a practice problem that will not be graded
    if x<0 or x>1:
        return 0
    else:
        return 1
def isOdd (n1):
    if n1%2==1 and type(n1)==int:
        return True
    else:
        return False

def grader (avg_exams, avg_hw, attendance):
    if attendance>=20 and avg_exams>=70 and avg_hw>=70 and avg_exams >=85 or avg_hw >=85:
        return True
    else:
        return False
    

def tupleCounter (t): 
    c=0
    for i in t:
        if i%2!=0:
            c=c+1
    return c

def cubeOfOdd (n2): 
    for i in range(n2):       
        if i % 2 != 0:            
            print(i**3)


def sec2Days (n3):
    d = n3//(24 * 3600)
    n3 = n3%(24 * 3600)
    h = n3//3600   
    n3= n3%3600 
    m = n3//60
    n3 %= 60
    s = n3
    
    day= "%02d:%02d:%02d:%02d" % (d, h, m, s)
    return day

def cellPhoneBill (m,tx):
    a= m-50
    b= tx-50
    c= a*.25
    d= b*.15
    p= (15+(c)+(d)+.44)
    e= (15+(c)+(d)+.44)*.05
    return e+p





########################################################
# Function Calls
# Do not Change/modify/touch.. any code below
########################################################

print ("\n**************************************")
x=5
print ("The result of p(x)")
print(p(x))
print ("\n**************************************")

n1=5
print ("The result of isOdd (n1) ")
print(isOdd (n1))
print ("\n**************************************")

avg_exams = 72
avg_hw = 88
attendance =22
print ("The result of grader (avg_exams, avg_hw, attendance) ")
print(grader(avg_exams, avg_hw, attendance))
print ("\n**************************************")

t = (2,4,6,7,9,121,1)  
print ("The result of tupleCounter (t) ")
print(tupleCounter (t))
print ("\n**************************************")

n2=5
print ("The result of cubeOfOdd (n2)")
print(cubeOfOdd (n2))
print ("\n**************************************")

n3=750000
print ("The result of sec2Days (n3)")
print(sec2Days (n3))
print ("\n**************************************")

m=70
tx=120
print ("The result of cellPhoneBill (m,tx)")
print(cellPhoneBill (m,tx))
print ("\n**************************************")



