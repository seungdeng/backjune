# T = int(input())

# for i in range(T):
#     line = sorted(map(int,input().split()))
#     # line.sort(reverse=0)
#     print('Case #'+str(i+1)+':',end=' ')

#     if line[-1] > line[0]+line[1]:
#         print('invalid!')
#     elif line[0]==line[1]==line[2]:
#         print('equilateral')
#     elif line[0]==line[1] or line[1]==line[2] or line[0]==line[2]:
#         print('isosceles')
#     else:
#         print('scalene')


# for i in range(T):
#     tri = list(map(int,input().split()))
#     tri.sort(reverse=1)
#     print('Case #'+str(i+1)+':',end=' ')
#     if tri[0]==tri[1]==tri[2]:
#         print('equilateral')
#     elif tri[0]==tri[1] or tri[0]==tri[2] or tri[1]==tri[2]:
#         print('isosceles')
#     elif tri[0]*tri[0] <= tri[1]*tri[1] + tri[2]*tri[2]:
#         print('scalene')
#     else:
#         print('invalid!')
        
for case in range(int(input())):
    li = sorted(map(int, input().split()))
    print(f"Case #{case+1}: ", end='')
    if li[0]+li[1] <= li[2]:
        print("invalid!")
    elif li[0] == li[1] == li[2]:
        print("equilateral")
    elif li[0]==li[1] or li[1]==li[2] or li[2]==li[0]:
        print("isosceles")
    else:
        print("scalene")