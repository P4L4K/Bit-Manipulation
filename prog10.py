"""
reference prog6
unset the ith bit of the no n
logic: 
       i=3
       1<<3 = 0001000

       n=43   = 0101011
       ~(1<<3)= 1110111  # all bits as 1 and only ith bit as 0 
       &      = 0100011
"""
num= int(input("Enter the number: "))
i= int (input("Enter the no of the bit: "))
mask=~(1<<i)
result= num & mask
print(f"Result after unsetting the {i}th bit:",result )
print("Given number in binary:",bin(num),"\tResult in binary:",bin(result))
