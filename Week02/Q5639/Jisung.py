import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

tree=[]

while True:
    try:
        tree.append(int(input()))
    except:
        break

def postorder(start,end):
    if start > end:
        return
    if start==end:
        return tree[start]
    
    mid = end+1
    for i in range(start+1,end+1):
        if tree[i]>tree[0]:
            mid = i
            break
    postorder(start+1,mid)
    postorder(mid+1,end)
    print(tree[start])

postorder(0,len(tree)-1)