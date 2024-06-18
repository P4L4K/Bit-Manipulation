"""
given : list -> each element is repeated twice except for one element
to find : the single element
sol : xor of all the elements 
logic : xor of similar elements cancels out leaving behing the single element
"""
print(1^5)
arr=input("Enter the list: ")
arr=arr.split(" ")
s=0
for i in arr:
    s=s^int(i)
print("single element in the given list: ",s)