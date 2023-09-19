N = str(input())

mo = ['a', 'e', 'i', 'o', 'u'] # 모음그룹 
ja = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
#자음그룹 
while N != 'end': #end 입력이 되기 전까지   
    mo_check = []  # 모음이 없는 단어 걸러내기
    for i in range(0, len(N)):
        if N[i] in mo:
            mo_check.append(i)
    if mo_check == []:
        print(f'<{N}> is not acceptable.')
        N = str(input())
        continue
    for i in range(0, len(N) - 2):
        if N[i] in ja and N[i+1] in ja and N[i+2] in ja:
            #자음연속3개시 걸러내기
            print(f'<{N}> is not acceptable.')
            N = str(input())
            continue
        if N[i] in mo and N[i+1] in mo and N[i+2] in mo: 
            #모음연속3개시 걸러내기
            print(f'<{N}> is not acceptable.')
            N = str(input())
            continue
        
    for i in range(0, len(N) - 1):
        if N[i] == N[i+1]:
            if N[i] not in ['e', 'o']:
                print(f'<{N}> is not acceptable.')
                N = str(input())
                continue        
        else:
            print(f'<{N}> is acceptable.')
            N = str(input())

            vowel = ['a', 'e', 'i', 'o', 'u']

# while True:
#     s = input()
#     if s == "end":
#         break
#     v_cnt = 0
#     v_repeat, c_repeat = 0, 0
#     last = ''
#     flag = True

#     for i in s:
#         if i in vowel:
#             if v_repeat == 2 or ((i != 'e' and i != 'o') and last == i):
#                 flag = False
#                 break
#             else:
#                 v_repeat += 1
#                 c_repeat = 0
#                 v_cnt += 1
#                 last = i

#         else:
#             if c_repeat == 2 or last == i:
#                 flag = False
#                 break
#             else:
#                 c_repeat += 1
#                 v_repeat = 0
#                 last = i
#     if v_cnt == 0:
#         flag = False

#     if flag:
#         print("<{}> is acceptable.".format(s))
#     else:
#         print("<{}> is not acceptable.".format(s))