"""
reference: prog3.py
find the xor of all the number form the given start to the given end 
pattern followed : 1, n+1 , 0 , n   (if start from 1)
sol: xor[s,n] = xor[1,n]^xor[1,s-1]
                 
"""
def xor_till(n):
    r=n%4
    if r==0:
        return n
       
    elif r==1:
        return 1
        
    elif r==2:
        return n+1
        
    else:
        return 0
        

s=int(input("Enter the lower range: "))
n= int(input("Enter upper range: "))
print("RESULT: ",xor_till(n)^xor_till(s-1))


r=0
for i in range(s,n+1):
    r=r^i
    
print("verify:",r)