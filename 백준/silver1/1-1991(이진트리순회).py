
N = int(input())
tree = {} # DICT

for n in range(N):
    root, left, right = map(str,input().split()) #메인노드 , 왼쪽,오른쪽 링크 구현
    tree[root] = [left, right] # 트리 딕셔너리 root value에 left,right 링크 key값 저장
 
 
def pre(root): #전위
    if root != '.': # 비어있는 노드가 아니라면
        print(root, end='')  # 해당 노드 출력
        pre(tree[root][0])  # 왼쪽링크 이동 (재귀)
        pre(tree[root][1])  # 위에 다 실행 후 아래링크 이동(재귀)
 
 
def mid(root):
    if root != '.':
        mid(tree[root][0])  
        print(root, end='')
        mid(tree[root][1])  

 
def post(root):
    if root != '.':
        post(tree[root][0])  
        post(tree[root][1])  
        print(root, end='')  
 
 
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