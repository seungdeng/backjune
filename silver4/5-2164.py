N = int(input())

li = list(range(1,N+1))

def switch(a):
    x = a[0]
    del a[0]
    a.append(x)
   

while True:
    del li[0]
    if len(li)==1:
        break
    switch(li)

print(li[0])

# from collections import deque

# N = int(input())
# deque = deque([i for i in range(1, N+1)])

# while(len(deque) >1):
#     deque.popleft()
#     move_num = deque.popleft()
#     deque.append(move_num)
    
# print(deque[0])