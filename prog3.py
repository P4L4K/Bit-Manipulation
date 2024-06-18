"""
find the xor of all the number form 1 to the given number 
pattern followed : 1, n+1 , 0 , n
"""
n= int(input("Enter number to find the xor of [1,n]: "))
r=n%4
if r==0:
    print("result:",n)
elif r==1:
    print("result:",1)
elif r==2:
    print("result:",n+1)
else:
    print("result:",0)


r=0
for i in range(1,n+1):
    r=r^i
print("verify:",r)
