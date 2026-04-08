E,S,M = map(int,input().split())

year = 1

while True:
    if ((year-E)%15==0)and ((year-S)%28==0) and ((year-M)%19==0):
        break
    year+=1
   

print(year)
# year = 1

# E,S,M = input().split()
# E = int(E)
# S = int(S)
# M = int(M)
# a,b,c = 1,1,1
# while True:
    
#     if a==E and b==S and c==M:
#         break;
#     else:
#         a%16
#         b%29
#         c%20
#         a+=1
#         b+=1
#         c+=1
#         year+=1


# print(year)