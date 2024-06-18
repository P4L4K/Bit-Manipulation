"""
reference: prog17
subsets are representted withthe help of truth table of the length 2**n(s)
if the value is 1 - consider the  value in that subset
"""
#printig subset of the given subset
s=(input("Enter the set elements: ")).strip()
s=s.split(" ")
print("Given set:",s)
n=len(s)
for i in range(2**n):
    subset=[]
    for j in range(n):
        if (i & (1<<j)): #checking the jth bit of i
             subset.append(s[j])
    print(subset)
