# Lab 6 GRADED exercises

def iSquare(n):
    i = 1
    h = 1
    while i < n:
        print(h**2)
        h += 1
        i += 1
    
def sConcatenate():
    con = ""
    while True:
        string = input("Enter a string")
        if string == "done":
            break
        if con != " ":
            con += " "
        con += string
    print("The concatenation is: " + con) 

def guessNumber():
    import random
    number=random.randrange(1, 100)
    
    user_count=1
    while(True):
        res=int(input("Enter your Guess"))
        if(res==number):
            print("Correct! you got it")
            break;
        else:
            if(res<number):
                print("your answer is too low. Try again!")
            else:
                print("your answer is too high. Try again!")
    



#############################################################################
#   !!! You Can Change the parameters below to test your code!!!
#############################################################################

print ("\n**************************************")
n = 5
print ("The result of iSquare")
iSquare(n)
print ("\n**************************************")
print ("The result of sConcatenate ")
sConcatenate()
print ("\n**************************************")
print ("The result of guessNumber ")
guessNumber()
print ("\n**************************************")