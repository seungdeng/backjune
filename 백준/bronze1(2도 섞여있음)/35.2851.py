A,score = 0,0

for i in range(10):
    score+=int(input())
    if 100-A>= abs(100-score):
        A = score
        
print(A)