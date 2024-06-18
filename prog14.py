"""
find the total no of set bits in the given number
not optimised o(bit no of the leftmost set bit)
"""
num=int(input("enter the number:"))
c=0
x=num
while(x):
    if(x&(1)):
        c+=1
    x=x>>1 #remove the rightmost bit : shorted the number of bits 
print("Total no of set bits:",c)

"""
optimised O(no of set bits)
reference: prog11
convert the first set bit to unset bit repeatedly till the num becomes 0
"""
c=0
x=num
while(x):
    x=x&(x-1)
    c+=1
print("Total no of set bits:",c)