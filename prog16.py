"""
find the xor of all the elements in the combination of all the subsets of a set s
eg: s={1,2,3}
    n(s)=3
    xor=0       
      subsets:
       {}               xor: 0
       {1},{2},{3}      xor:0^2^3^1
       {1,2},{1,3},{2,3}xor:0^2^3^1^2^1^3^2^3^1
       {1,2,3}          xor:0^1^2^3^1^2^3 = 0
    if s={1}
       n(s)=1
          subsets:
            {}       xor: 0
            {1}      xor:0^1  = 1

When combining all the subsets of a set S, each element in S appears an even number of times in the final combination.
For every element included in a subset of size k (excluding the empty set), there is a corresponding subset of size (n-k), where n is the total number of elements in the set, that does not include the same element.

since all element are occuring even no of time they would get canceled out in xor
so the result would always be 0 :-)
"""
s= (input("Enter the elements of the set: ")).strip()
s=list(s.split(" "))
if (len(s)!=1):
  print(f"Result: 0")
else:
  print(f"Result:",0^int(s[0]))