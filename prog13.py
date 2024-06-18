"""
check whether the given no is the power of 2 or not

powers of 2 : 
        2 = 010
        4 = 0100
        8 = 01000
        16= 010000

        pattern: 1+ all zeros

    if we sub 1 from the num, all the the 0 in the right of the one would become 1 and 1 become 0 while the digits on the left remains same
    4=0100                          5=0101
    3=0011                          4=0100
    &=0000 ->(0) power of 2         &=0100 -> not a power of 1
"""

n=int(input("Enter the number: "))
if(n&(n-1)):
    print(f"{n} is not a power of 2")
else:
    print(f"{n} is a power of 2")