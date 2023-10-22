N = input()
pw = []

for i in range(len(N)):
    if N[i] == ' ' or ord(N[i]) < ord('A'):
        pw += N[i]
    else:
        if ord(N[i]) + 13> 122:
            pw += chr(96+(ord(N[i])+13)-122)
        elif ord(N[i]) + 13> 90 and ord(N[i])<91:
            pw += chr(64+(ord(N[i])+1)-90)
        else:
            pw +=chr(ord(N[i])+13)

print(''.join(pw))