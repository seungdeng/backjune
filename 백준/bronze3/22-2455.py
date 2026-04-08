result = 0 
S =[]
for i in range(4):
    OUT,IN = map(int,input().split())
    S.append(result-OUT+IN)
    result = result-OUT+IN
    
print(max(S))