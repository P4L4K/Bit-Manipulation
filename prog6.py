"""
given (N,i): to check if the ith bit of N is set(1) or unset(0)
solution : 1<<i & N
     Eg: 
      i=2 (START FORM 0)
      1 =   0001
        N=11= 1011
        1<<2= 0100 
        &   = 0000    -> UNSET

        N=7 = 0111
        1<<2= 0100
        &   = 0100     -> SET   
"""
num=int(input("Enter the number: "))
i=int(input("Enter the bit no: "))
print("Given number: ",bin(num))
if(num&(1<<i)):
    print("Set")
else:
    print("Unset")