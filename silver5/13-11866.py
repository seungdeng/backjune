from sys import stdin

N, K = map(int,stdin.readline().split())
index = 0
array = list(range(1,N+1))
result = []

while len(array) != 0: # 리스트 수가 0이 아니면 반복
    index += (K-1)
    index = index % len(array)
    result.append(array.pop(index))

## 문자
print("<",end="")
for i in range(N-1):
    print(result[i],end=", ")
print(result[N-1], end = "")
print(">",end="")
# N,K = input().split()

# N = int(N)
# K = int(K)

# A = list(range(1,N+1))
# x = 0


# # def exist(a,b):
# #      return (0<= b<len(a) or (-len(a) <= b<0))


# B =[]


# while A:
#     x += K-1
#     if x >= len(A):
#           x %= len(A)
    
#     B.append(str(A.pop(x)))


# print("<",",".join(B),">",sep="")


