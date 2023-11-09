H,M = input().split()

H = int(H)
M = int(M)


if M-45<0 or H-1<0:
    if M-45<0:
        H-=1
        M+=15    
    
    if H-1<0:
        H+=24

else:
    M-=45

print(H,M)
