import time
ad=0
def conversion(a): #returns a binary string of a number which has bits equal to count
    q=""
    current_n = len(a)
    temp = count- current_n
    if (current_n != count):
        q = "0"*temp + a
    return q
def add(M,Q): #fun to add two binary number strings
  
    max_len = max(len(M),len(Q))
    result = ''
    carry = 0
    for i in range(max_len-1, -1, -1):
           r = carry
           if M[i] == '1':
               r += 1
           if Q[i] == '1':
               r += 1 
           if r % 2 == 1:
               result = "1" + result 
           else: 
               result = "0" + result
           if r<2:
               carry =0
           else:
               carry= 1  
    return result

def twoc(a):  #to find 2s compliment
    l = list(a)
    for i in range(len(l)):
         if l[i] == "1" :
             l[i] = "0"
         else: l[i] ="1"
    b = "0"*(len(l)-1) + "1" 
    return add("".join(l),b)
def right_shift(ac,q,q1): 
    a = ac[0]
    for i in range(1,len(ac)):
        a+=ac[i-1]
    b = ac[-1]
    for j in range(1,len(q)):
        b+=q[j-1]
    c = q[-1]
    return a,b,c
#Taking input and assigning values
M = int(input("Enter multiplicand: "))
Q = int(input("Enter multiplier: ")) #taking M and Q decimal numbers as input for M * Q
a = bin(M).replace("0b", "")
b = bin(Q).replace("0b", "")
negative_a=0
negative_b=0
if (a[0]=="-"):
        a = a.replace("-","")
        negative_a =1
if (b[0]=="-"):
        b = b.replace("-","")
        negative_b =1

if (len(a)>len(b)):
    count = len(a)+1
else: count = len(b) + 1

count1 = count
firstP = conversion(a) #contains the positive representation of the multiplicand 
secondP = conversion(b) #contains the positive representation of the multiplier
firstN = twoc(firstP) #contains 2's complement of the multiplicand
secondN = twoc(secondP) #contains 2's complement of the multiplier

#BOOTH ALGO IMPLEMENTATION
if negative_a ==0:
    M = firstP #M is the multiplicand and M2 contains its 2's complement
    M2 = firstN
else:
    M = firstN
    M2 = firstP
if negative_b ==0:
    Q = secondP #Q is the multiplier
else:
    Q = secondN
AC = conversion("0")
Q1 = "0" # one bit for comparision
print("\nThe table for the booth's algorithm is as follow:")
print("Count" +" "*count1 + "AC " +" "*count1 + " Q" +" "*count1 + "Q1" +" "*count1 + "Operation",sep=" \t ")
print(" "+str(count) +" "*count1 + AC +" "*count1 + Q +" "*count1 + Q1 +" "*count1 + "initial",sep="\t\t")
print("\n")

while (count>0):
    compare = Q[-1] + Q1
    
    if compare[0]==compare[-1]:
        AC, Q, Q1 =right_shift(AC,Q,Q1)
        Op = "right shift" 
    elif compare =="10":
        AC = add(AC,M2)
        ad+=1
        AC, Q, Q1 =right_shift(AC,Q,Q1)
        Op = "AC=AC-M and right shift"
        
    elif compare == "01":
        AC = add(AC,M)
        ad+=1
        AC, Q, Q1 =right_shift(AC,Q,Q1)
        Op = "AC=AC+M and right shift"
        

    print(" "+str(count) +" "*count1 + AC +" "*count1 + Q +" "*count1 + Q1 +" "*count1 + Op,sep="\t\t")
    count = count-1
answer = AC+Q
if negative_a==negative_b:
    ans_d = str(int(answer,2))
else:
    ans_d = "-" + str(int(twoc(answer),2))
    ad+=1

print("\nThe product in binary is:" + answer)
print("Decimal conversion:" + ans_d)  




