while True:
    num = int(input())
    if num == -1: 
        break
    numlist = []
    for i in range(1, num):
        if num % i == 0:
            numlist.append(i)
    if sum(numlist) == num:
        print(num, " = ", " + ".join(str(i) for i in numlist), sep="")
    else:
        print(num, "is NOT perfect.")
# while 1:
#     num=int(input())
#     if num==-1:
#         break
#     i=1
#     numlist=[]
#     while i<num:
#         if num%i==0:
#             numlist.append(i)
#         i+=1
#     numlist.sort(reverse=0)
#     if sum(numlist)!=num:
#         print(str(num)+' is NOT perfect')
#     else:
#         print(num,'= ',end='')
#         print(numlist[0],end=' ')
#         for i in range(1,len(numlist)-1):
#             print('+',numlist[i],end=' ')
#         print('+ '+str(numlist[-1]))


# numlist = []

# def solution(x):

#     for i in range(1, int(x**(1/2)) + 1):
#         if (x % i == 0):
#             numlist.append(i) 
#             if ( (i**2) != x) : 
#                 numlist.append(x // i)  
#     numlist.sort(reverse=0)             
#     return sum(numlist)

# while 1:
#     num = int(input())
#     if num=='-1':
#         break
#     if solution(num)!=num:
#         print(str(num)+' is NOT perfect')
#     else:
#         for i in numlist:
#             print(str(i))