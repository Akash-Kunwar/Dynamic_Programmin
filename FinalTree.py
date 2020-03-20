class Node:
    def __init__(self,data):
        self.right=None
        self.left=None
        self.data=data
def insert(root,data):
    if root == None:
        root = Node(data)
        return root
    else:
        curr=root
        OrigRoot =root
        newNode=Node(data)
        while(root!=None):
            curr=root
            if root.data >= data:
                root=root.left
            else:
                root=root.right
        if curr.data>=data:
            curr.left = newNode
        else:
            curr.right=newNode
        return OrigRoot



def preorder(root):
    if(root):
        print(root.data)
        preorder(root.left)
        preorder(root.right)

def LevelOrderTraversal(root):
    q=[]
    q.append(root)
    while(len(q)!=0):
        n=len(q)
        for i in range(n):
            node=q.pop(0)
            if node != None:
                if i==0:
                    print(node.data,end=' ')
                    if node.left!=None:
                        q.append(node.left)
                    if node.right!=None:
                        q.append(node.right)

        

root = insert(None,10)
root =insert(root,8)
root =insert(root,20)
root =insert(root,7)
root =insert(root,9)
root =insert(root,15)
root =insert(root,24)
# preorder(root)
LevelOrderTraversal(root)