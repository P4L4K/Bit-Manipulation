#codeforces :  https://codeforces.com/problemset/problem/1097/B (petr and combination lock)
n=int(input())
s=[]
for i in range(n):
    s.append(int(input()))
for i in range(2**n):
    result=0
    for j in range(n):
        if (i&(1<<j)):
            result+=s[j]
        else:
            result-=s[j]
    if (result%360==0):
        print("YES")
        break
else:
    print("NO")


