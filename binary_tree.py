class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left==None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right==None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data=data

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

    def in_order(self,root):
        res=[]
        if root:
            res=self.in_order(root.left)
            res.append(root.data)
            res=res+self.in_order(root.right)
        return res

    def pre_order(self,root):
        res=[]
        if root:
            res.append(root.data)
            res=res+self.pre_order(root.left)
            res=res+self.pre_order(root.right)
        return res

    def post_order(self,root):
        res=[]
        if root:
            res=self.post_order(root.left)
            res=res+self.post_order(root.right)
            res.append(root.data)
        return res

    def find_val(self,data):
        if data<self.data:
            if self.left is None:
                return str(data) +' not found'
            return self.left.find_val(data)
        elif data>self.data:
            if self.right is None:
                return str(data) + ' not found'
            return self.right.find_val(data)
        else:
            return str(self.data) + ' found'

root=Node(10)
root.insert(6)
root.insert(11)
root.insert(2)
root.insert(15)
root.print_tree()
print(root.in_order(root))
print(root.pre_order(root))
print(root.post_order(root))
print(root.find_val(11))
print(root.find_val(9))
print(root.find_val(15))
