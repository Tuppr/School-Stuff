################################################################################
# HW1, CS103 Spring 2019
# name: Chandler Whittington
# blazerid: cwhitt00
################################################################################

import math      # you will need the math module to answer some of the questions

################################################################################

def myName (): 
    # PLEASE REPLACE 'James Bond' BY YOUR NAME; do not change anything else;
    # for example, leave the single quotes alone as you insert your name
    return 'Chandler Whittington'



######################################################################
# HW1 PROBLEMS
######################################################################

# check hw1.pdf file to see implemented test cases and expected outputs
def f(x):           # this is a practice problem that will not be graded
    
    return 5*x-3

def areaCircle (r):
    
    return (math.pi)*r**2

def nSnookerBall (nRow):
    
    return (nRow*(nRow+1))/2

def eApproximately (n): 
    
    return (1+(1/n))**n

def volCone (r, h):
    
    return (1/3)*(math.pi)*r**2*h

def distOrigin (x, y):
    
    return ((0-x)**2+(0-y)**2)**.5

def lengthSegment (x1, y1, z1, x2, y2, z2):
    
    return ((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)**.5





########################################################
# Function Calls
# Do not Change/modify/touch.. any code below
########################################################

print ("\n**************************************")
x=5
print ("The result of f(x)")
print(f(x))
print ("\n**************************************")

r=12.34
print ("The result of areaCircle (r) ")
print(areaCircle (r))
print ("\n**************************************")

nRow =3
print ("The result of nSnookerBall (nRow) ")
print(nSnookerBall (nRow))
print ("\n**************************************")

n=100
print ("The result of eApproximately (n) ")
print(eApproximately (n))
print ("\n**************************************")

r=3
h=2
print ("The result of volCone (r, h)")
print(volCone (r, h))
print ("\n**************************************")

x=3
y=4
print ("The result of distOrigin (x, y)")
print(distOrigin (x, y))
print ("\n**************************************")

x1=200
y1=200
z1=200
x2=203
y2=204
z2=200
print ("The result of lengthSegment (x1, y1, z1, x2, y2, z2)")
print(lengthSegment (x1, y1, z1, x2, y2, z2))
print ("\n**************************************")



