import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(1000000)
# 이분탐색 베이스
def inpo_to_pre(inorder_start, inorder_end, postorder_start, postorder_end):
    if inorder_start > inorder_end or postorder_start > postorder_end:
        return
    
    root = post_order[postorder_end]
    print(root, end=" ")
    # 왼쪽자식의 갯수, 오른쪽자식의 갯수
    left = node[root] - inorder_start
    right = inorder_end - node[root]
    # 포스트 오더에서는 인오더랑 인덱스가 같지 않기 때문에 숫자로 따로 설정해줌
    inpo_to_pre(inorder_start, node[root] - 1, postorder_start, postorder_start + left - 1)
    inpo_to_pre(node[root] + 1, inorder_end, postorder_end - right, postorder_end -1)
    # inpo_to_pre(in_order[:root_index:], postorder[:root_index:])
    # inpo_to_pre(in_order[root_index+1::], postorder[root_index:-1:])
    
n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

node = [0] * (n + 1)
# 숫자가 몇번째에 있는지 확인
for i in range(n):
    node[in_order[i]] = i
print(node)

inpo_to_pre(0, n-1, 0, n-1)

# # 안된거 근데 답은 나옴... 인덱스에러 아마 끝까지 가도 시간초과일 것 같긴함
# def inpo_to_pre(inorder, postorder, n):
#     if len(postorder) <= 0 or len(postorder) <= 0:
#         return
#     root_node = postorder[-1]
#     perfect[n] = root_node
#     root_index = -1
#     for i in range(len(inorder)):
#         if inorder[i] == root_node:
#             root_index = i
#     inpo_to_pre(inorder[:root_index], postorder[:root_index], n*2)
#     inpo_to_pre(inorder[root_index+1:], postorder[root_index:-1], n*2+1)
    
# def preorder(i):
#     if perfect[i] == 0:
#         return
#     print(perfect[i], end = " ")
#     preorder(i*2)
#     preorder(i*2+1)

# n = int(input())
# in_order = list(map(int, input().split()))
# post_order = list(map(int, input().split()))
# perfect = [0] * 300001

# inpo_to_pre(in_order, post_order, 1)
# perfect.extend([0 for _ in range(len(perfect))])
# preorder(1)

# # 안된거 2
# def inpo_to_pre(inorder_start, inorder_end, postorder_start, postorder_end):
#     if inorder_start > inorder_end or postorder_start > postorder_end:
#         return
#     print(post_order[postorder_end], end=" ")
#     root_index = in_order.index(post_order[postorder_end])
#     inpo_to_pre(inorder_start, root_index - 1, postorder_start, root_index - 1)
#     inpo_to_pre(root_index + 1, inorder_end, root_index, postorder_end -1)
    
    
# n = int(input())
# in_order = list(map(int, input().split()))
# post_order = list(map(int, input().split()))

# inpo_to_pre(0, n-1, 0, n-1)