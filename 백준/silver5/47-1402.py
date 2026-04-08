# T = int(input())



# for i in range(T):
# 	A,B = map(int,input().split())
# 	li = []
# 	for k in range(2,int(A**0.5)+1):
# 		if A% k == 0:
# 			li.append(k)
# 			if A // k != k:
# 				li.append(k)
# 	if sum(li) == B:
# 		print('YES')
# 	else:
# 		print('NO')

			
for _ in range(int(input())):
    A, B = map(int, input().split())
    print("yes")