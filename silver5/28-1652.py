import sys
input = sys.stdin.readline

N = int(input())

A = [[0 for j in range(N)]for i in range(N)] # N * N 리스트 

for i in range(N):
    A[i] = list(map(str,input().split()))

printsero= 0
printkaro= 0

for k in range(N):
    for a in range(N-1):
        if A[k][a] == A[k][a+1] == '.':
            printkaro+=1
            break;
    for b in range(N-1):
        if A[b][k] == A[b+1][k] == '.':
            printsero +=1
            break;



# print(printkaro,printsero)

# N = int(input())

# map_list = [input().strip() for _ in range(N)]

# rowcnt, colcnt = 0, 0
# for i in range(N) :
#   tmp_row_cnt, tmp_col_cnt = 0, 0
#   for j in range(N) :
#     if map_list[i][j] == '.' :
#       tmp_row_cnt += 1
#     else :
#       if tmp_row_cnt > 1 :
#         rowcnt += 1
#       tmp_row_cnt = 0

#     if map_list[j][i] == '.' :
#       tmp_col_cnt += 1
#     else :
#       if tmp_col_cnt > 1 :
#         colcnt += 1
#       tmp_col_cnt = 0
#   if tmp_row_cnt > 1 :
#     rowcnt += 1
#   if tmp_col_cnt > 1 :
#     colcnt += 1

# print(rowcnt, colcnt)