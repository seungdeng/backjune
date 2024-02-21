Pixel = []
for i in range(15):
    Pixel.append(map(str,input().split()))
for i in Pixel:
    if 'w' in i:
        print('chunbae')
        break
    elif 'b' in i:
        print('nabi')
        break
    elif 'g' in i:
        print('yeongcheol')
        break