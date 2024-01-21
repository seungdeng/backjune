N = int(input())

S = list(map(int,input().split()))

result =0 
result+=sum(S)
result+= (len(S)-1)*8
print(result)