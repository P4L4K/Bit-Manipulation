"""
reference: prog7, prog6 , prog1
given : list of element occuring twice except the 2 elements which occurs only once
to find: the elements that occurs once
logic:
       l=[2,1,2,5,4,4,7,3,3,1]
       x = xor of all the elements 
       x =num1 ^ num2
       for any set bit of x , one among num1 or num2 will  have set and other have unset bit at that place 
          5  num1 : 101
          7  num2 : 111
             x    : 010
       divid the elements of the given list into 2 parts
           5: 1,5,4,4,1  # all with 1 as unset bit
              xor of these elements = 5
           7: 2,2,7,3,3  # all with 1 as set bit
               xor of these elements = 7
"""

def last_setbit(num):
    i=0
    x=1
    while(not(num & x)):
        i+=1
        x=1<<i
    return i  #index of the last set bit


l=input()
l=l.split(" ")
x=0
for i in l:
    x=x^int(i)  # x will contain the xor of the 2 single elements

s=last_setbit(x)  #last set bit of x
num1=0   #with s as set bit
num2=0   #with s as unset bit
for i in l:
   i=int(i)
   if(i&(1<<s)): #check if the sth bit is set or not 
      num1=num1^i
   else:
      num2=num2^i
print(f"The 2 single digits are {num1} and {num2}")