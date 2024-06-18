"""
bin and (&)
      0 & 1 : 0      any one 0: 0
      1 & 1 : 1      all 1: 1
bin or (|)
      0 & 0 : 1      all 0: 0
      1 & 0 : 1      any one 1: 1

xor (^)
      same : 0        (1^1) or (0^0)
      different : 1   (0 ^ 1)

      5^3=6 
      6^3=5
      6^5=3

      x^x=0
      cancels out 2 similar 

nor (~)
      0 : 1 
      1 : 0 
      eg: ~101 : 010 

right shift (>>)
      divide by 2 to the power
      5>>1 : 101 >>1 : _10 : 010
             101 = 1* 2**2 + 0 * 2**1 + 1* 2**0
             5/2 = 2 =  10 = 1* 2**1 + 0 * 2**0
      similarly 5>>2 : 101 >> 2 : __1 
             (5/2)/2 : 2/2 : 1 : 1 * 2**0

      8>>5 : (((((8//2)//2)//2)//2)//2)

left shift (<<)
      multiply by 2 to the power
      5<<1: 101 : 101_ : 1010 
            101 = 1* 2**2 + 0 * 2**1 + 1* 2**0
            5*2 = 10 =  1010 = 1* 2**3 + 0 * 2**2 + 1 * 2**1 + 0 * 2**0
      8<<4 : 8 * 2 * 2 * 2 * 2
      
      NOTE: 2**N == 1<<N  
Binary addition: 
   1 + 0 = 1
   0 + 1 = 1
   0 + 0 = 0
   1 + 1 = 0 carry 1 

   Adding 1 from a binary number toggles the rightmost unset bit and all the bits to its right (if any) up to the least significant bit (LSB). 
   All the bits to the left of the rightmost unset bit remain unchanged.

Binary substraction: 
   1 - 0 = 1
   0 - 1 = 1  borrow 1
   0 - 0 = 0
   1 - 1 = 0 

      initial weights:  1x16  0x8   0x4   0x2   0x1
      after borrow:     0x16  2x8(16)
                        0x16  1x8   2x4(8) 
                        0x16  1x8   1x4    2x2(4)
      final weights:    0x16  1x8   1x4    1x2   2x1(2)  

            n1            1     0     0     0     0
            n2            0     1     1     1     1
      result:     -       0     0     0     0     1
                        (0-0) (1-1) (1-1) (1-1) (2-1)

      Subtracting 1 from a binary number toggles the rightmost set bit and all the bits to its right (if any) up to the least significant bit (LSB). 
      All the bits to the left of the rightmost set bit remain unchanged.

sets : 
 When combining all the subsets of a set S, each element in S appears an even number of times in the final combination.
 For every element included in a subset of size k (excluding the empty set), there is a corresponding subset of size (n-k), where n is the total number of elements in the set, that does not include the same element.
 subsets can be obtained by utilizing truth table including the value coresponing to 1s.

 """
print(1<<2,1<<4)
for i in range(0,12):
    print(i,bin(i))

print("\n")
print(5^3,6^3,6^5)
print(8<<4,8 * 2 * 2 * 2 * 2)
print(8>>5,(((((8//2)//2)//2)//2)//2))

print("\n")
print(2^1)
print(3^1, 3^2)
print("x",2^5,"y",7^1,"z",6^2,"f",4^5)
print(bin(2),bin(1),bin(5))
