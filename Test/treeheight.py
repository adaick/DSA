class Node:
    def __init__(self,data):
        self.data = data
        self.left  = None
        self.right = None

def insert(node,data):
    if node is None:
        return Node(data)

    if data <= node.data:
        node.left = insert(node.left,data)
    else:
        node.right = insert(node.right,data)

    return node

def treeheight(node): 
    if node is None: 
        return 0
    else:  
        Dleft = treeheight(node.left) 
        Dright = treeheight(node.right) 
 
        if (Dleft > Dright): 
            return Dleft+1
        else: 
            return Dright+1



inp = int(input("Enter the number of nodes: "))
root = None
print('Now enter nodes:')
node=list(map(int,input().split()))

if len(node)==inp:
    for data in node:
        root = insert(root, data)
else:
    print("you didn't entered correct node" )
print(treeheight(root))