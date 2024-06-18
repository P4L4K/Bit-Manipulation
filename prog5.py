"""
find whether the given no is even or odd
solution : & 
logic : 
        even : has 0 as the right most bit
        odd  : has 1 as the right most bit 

        let e= 10100
            1= 00001
          1&e= 00000 

        let o= 10101
            1= 00001
          1&o= 00001 

        hence when we apply & with 1 only the last bit will have some value or the result will either be 0 or 1
"""
num=int(input("Enter the number: "))
if(num&1):
    print(num,"is Odd")
else :
    print(num,"is Even")