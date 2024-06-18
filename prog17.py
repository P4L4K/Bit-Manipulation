#printing truth table of length n
n=int(input("Enter n: "))
for i in range(2**n):
    for j in range(n):
        print(int(bool(i & (1<<j))),end=" ")
    print()
        