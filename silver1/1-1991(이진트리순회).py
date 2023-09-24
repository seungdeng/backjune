
N = int(input())
tree = {}
 
for n in range(N):
    root, left, right = map(str,input().split())
    tree[root] = [left, right]
 
 
def pre(root):
    if root != '.':
        print(root, end='')  # root
        pre(tree[root][0])  # left
        pre(tree[root][1])  # right
 
 
def mid(root):
    if root != '.':
        mid(tree[root][0])  # left
        print(root, end='')  # root
        mid(tree[root][1])  # right
 
 
def post(root):
    if root != '.':
        post(tree[root][0])  # left
        post(tree[root][1])  # right
        print(root, end='')  # root
 
 
pre('A')
print()
mid('A')
print()
post('A')


# class Node:
#     def __init__(self,data,left,right):
#         self.data = data
#         self.left = None
#         self.right = None
# # 전위pre 중위mid 후위 post
# def pre(node):
#     print(node,end='')
#     if tree[node].left != None:
#         pre(tree[node].left)
#     if tree[node].right!= None:
#         pre(tree[node].right)

# def mid(node):
#     if tree[node].left !=None:
#         mid(tree[node].left)
#     print(node,end='')
#     if tree[node].right !=None:
#         mid(tree[node].rihgt)

# def post(node):
#     if tree[node].left !=None:
#         post(tree[node].left)
#     if tree[node].right != None:
#         post(tree[node].right)
#     print(node,end='')

# N = int(input())
# tree = {}    

# for i in range(N):
#     data,left,right  = map(str,input().split())
#     if left =='.':
#         left = None
#     elif right =='.':
#         right = None
#     tree[data] = Node(data,left,right)

# pre('A')
# print()
# mid('A')
# print()
# post('A')



# for i in range(N):
#     arr = list(map(str,input().split()))
#     if arr[0]=='A':
#         Binarytree()
#     # elif arr[0] != '.':
#     #     arr[0].item = arr[0]
#     elif arr[1] !='.':
#         arr[0].left = arr[1]
#     elif arr[2] !='.':
#         arr[0].right = arr[2]