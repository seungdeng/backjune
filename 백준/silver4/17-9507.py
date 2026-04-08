T = int(input())

n = [0]*68
n[0]=1
n[1]=1
n[2]=2
n[3]=4

for i in range(4,len(n)):
    n[i]=n[i-1]+n[i-2]+n[i-3]+n[i-4]

result =0
A = []
for k in range(T):
    A.append(int(input()))
for j in A:
    print(n[j])
