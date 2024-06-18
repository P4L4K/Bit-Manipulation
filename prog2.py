"""
swap 2 numbers
soultion : xor
logic : 
        x^y = z
        z^x = y
        z^y = x 
        we get same value again after applying the xor over the result as similar values cancel out 
"""

a= int(input("Enter first no: "))
b= int(input("Enter second no: "))
print("Given:",a,b)
a=a^b #a^b
b=a^b #a^b^b = a
a=a^b #a^b^a = b
print("Swaped:",a,b)
