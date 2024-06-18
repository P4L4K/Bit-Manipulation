"""
reference : prog6
extract the ith bit of the number n
i: starts from 0
"""
num=int(input("Enter the number: "))
i = int(input("Enter the bit number: "))
print("Given number:",bin(num))
if(num&(1<<i)):
    print(1,"is present at bit number",i)
else:
    print(0,"is present at bit number",i)