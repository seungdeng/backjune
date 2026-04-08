word = input()
bomb = input()

while bomb in word:
    newword = word.replace(bomb,'')
    word = newword

if len(word)==0:
    print('FRULA')
else:
    print(word)        
