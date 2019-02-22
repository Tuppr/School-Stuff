# -*- coding: utf-8 -*-
#hw3
import math
def MyName():
    return "Chandler Whittington"
    
def sumOfTwo(x,y):
    return x+y
    
def listBuilder(l1,length):
    newlist=[]
    for w in l1:
        if len(w)>=length:
            newlist.append(w)
    return newlist

def lettersOnly(s):
    newstr=""
    for l in s:
        if l.isalpha():
            newstr +=l
    return newstr
    
def elementLengthIsIndex(l1):
    l=[]
    for i in l1:
        num=l1.index(i)
        if len(i)==num:
            l.append(i)            
    return l
    
def typeMatters(par):
    if type(par) == str:
        return par * len(par)
    elif type(par) == int:
        new = ''
        for i in range(1, par+1):
            new += str(i) + ' '
        return new
    elif type(par) == float:
        return "I am a float of value: " + str(par)
    elif type(par) == list:
        par.sort(reverse=True)
        return par
    else:
        return "I am not a string, int, float, or list."
    
def paintTheRoom(length, width, height):
    wall1=((length*height)*2)
    wall2=((width*height)*2)
    ceiling=length*width
    return math.ceil((wall1+wall2+ceiling)/400)
    
    

print("************* result of MyName ***********")   
print(MyName())

print("************* result of sumOfTwo *********")
x,y=12,23
print(sumOfTwo(x,y))

print("************* result of listBuilder ******")
l1=["Hello", "I", "am", "a", "list"]
length=4
print(listBuilder(l1,length))

print("************* result of lettersOnly ******")
s ="CS103 is kind of fun."
print(lettersOnly(s))

print("************* result of elementLength ****")
l1=["I'm", "a", "tricky", "one"]
print(elementLengthIsIndex(l1))

print("************* result of typeMatters ******")
par= "Hello"
print(typeMatters(par))

print("************* result of paintTheRoom *****")
length,width,height=10,12,8
print(paintTheRoom(length, width, height))