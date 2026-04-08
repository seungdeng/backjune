burger = []
drink = []

for i in range(3):
    burger.append(int(input()))
for k in range(2):
    drink.append(int(input()))

burger.sort()
drink.sort()

result = burger[0] + drink[0]

print(result-50)