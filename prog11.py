"""
unset the last set bit or (toogle the last set bit)

optimised method

Subtracting 1 from a binary number toggles the rightmost set bit and all the bits to its right (if any) up to the least significant bit (LSB). 
All the bits to the left of the rightmost set bit remain unchanged.

when we perform & between n & n-1 , all the bits to the right of the rightmost set bit including the rightmost set bit is made unset 
     ( bits to the right of the rightmost set bit were already unset in n,) while the others remains same

    n  = 101010
    n-1= 101001
    &  = 101000  -> rightmost set bit is unset
"""

num=int(input("Enter the number: "))
print("given:",bin(num))
result= num&( num-1)
print("result:",bin(result))


"""
reference prog7 and prog10

"""
s=0
while(not(num&(1<<s))):
      s+=1
print("the last set bit is",s)
result=num&(~(1<<s))
print("result:",bin(result))




