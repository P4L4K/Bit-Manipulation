"""
set the last unset bit or (toogle the last unset bit)

optimised method

adding 1 from a binary number toggles the rightmost unset bit and all the bits to its right (if any) up to the least significant bit (LSB). 
All the bits to the left of the rightmost unset bit remain unchanged.

when we perform | between n & n+1 , all the bits to the right of the rightmost unset bit including the rightmost set bit is made set 
     ( bits to the right of the rightmost unset bit were already set in n) while the others remains same

    n  = 101011
    n+1= 101100
    |  = 101111  -> rightmost unset bit is set
"""

num=int(input("Enter the number: "))
print("given:",bin(num))
result= num|( num+1)
print("result:",bin(result))


"""
reference prog7 and prog9
"""
u=0
while((num&(1<<u))):
      u+=1
print("the last unset bit is",u)
result= num|(1<<u)
print("Result:",bin(result))