"""
set the ith bit of the given number
i : starts form 0
logic :
       i=1
       1    = 0001
       n=12 = 1100
       1<<i = 0010
       |    = 1110  -> 1st bit is set
"""


num= int(input("Enter the number: "))
i= int (input("Enter the no of the bit: "))
result= num | (1<<i)
print(f"Result after setting the {i}th bit:",result )
print("Given number in binary:",bin(num),"\tResult in binary:",bin(result))