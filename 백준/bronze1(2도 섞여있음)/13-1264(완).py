while(True):
   A = input()
   if A =="#":
        break;
   count = 0
   for i in range(len(A)):
     if A[i] in 'aeiouAEIOU':
        count+=1
   print(count)    