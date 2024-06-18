def binary_to_decimal(binary_str):
    decimal = 0
    power = len(binary_str) - 1  # Initialize power of 2 to the length of the binary string - 1

    # Iterate over each character in the binary string
    for bit in binary_str:
        # If the bit is '1', add 2^power to the decimal number
        if bit == '1':
            decimal += 2 ** power
        # Decrease the power of 2 for the next bit
        power -= 1

    return decimal



def badd(M,Q): #fun to add two binary number strings
    if (len(M)>len(Q)):
        #swap to maintain min in M
        f=M
        M=Q
        Q=f
    c=len(Q)-len(M)
    M=('0'*c)+M
  
    max_len = len(M)
    result = ''
    carry = 0
    for i in range(max_len-1, -1, -1):
           r = carry
           if M[i] == '1':
               r += 1
           if Q[i] == '1':
               r += 1 
           if r % 2 == 1:
               result = "1" + result 
           else: 
               result = "0" + result
           if r<2:
               carry =0
           else:
               carry= 1  
    print("add: ",M,"+",Q,"=",result)
    return result
def add(bin1, bin2):
    # Pad the binary strings with zeros to make them of equal length
    max_len = max(len(bin1), len(bin2))
    bin1 = bin1.zfill(max_len)
    bin2 = bin2.zfill(max_len)

    # Initialize variables for carrying and the result
    carry = 0
    result = ''

    # Iterate through the binary strings in reverse order
    for bit1, bit2 in zip(reversed(bin1), reversed(bin2)):
        # Perform binary addition with carry
        temp_sum = int(bit1) + int(bit2) + carry

        # Update result and carry
        result = str(temp_sum % 2) + result
        carry = temp_sum // 2

    # Add any remaining carry
    if carry:
        result = '1' + result
    print("add: ",bin1,"+",bin2,"=",result)
    return result


r=15
s=15
m=bin(15)[2:]
q=bin(15)[2:]
print("\nGiven:",f"Multiplicand: {m} ({r}) ",f"Multiplier: {q} ({s})",sep="\n")
x=[]
ls=0
print("\nIndividual Multiplications:")
for i in range(-1,-(len(q)+1),-1):
    if q[i]=='0':
        y='0'*len(m)
    else:
        #left shift by 1
        ls+=1
        y=bin(r<<((i*(-1))-1))[2:]
        x.append(y)
    
    print("multiply :" ,q[i],"*",m,"=",y)
    

print("\nAdditions:")
ad=0
while(len(x)>1):
    z=x[-1]
    d=x[-2]
    x.pop()
    x.pop()
    x.append(add(d,z))
    ad+=1

print("\nBinary Result:",x[0])
print("Decimal Result:",binary_to_decimal(x[0]))




