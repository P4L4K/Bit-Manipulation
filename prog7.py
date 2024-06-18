"""
reference: prog6
To find the last(first from the right) set and the last unset bit of the given number 
"""
num=int(input("Enter the number: "))
print("Given number:",bin(num))
s=0
x=1
while(not(num & x)):
    s+=1
    x=1<<s
print("The last set bit is",s)
s=0
x=1
while((num & x)):
    s+=1
    x=1<<s

print("The last unset bit is",s)