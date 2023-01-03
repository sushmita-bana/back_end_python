class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singli_ll:
    def __init__(self):
        self.head=None

    def traversal(self):
        if self.head is None:
            print('list is empty')
        else:
            a=self.head
            while a is not None:
                print(a.data,end=' ')
                a=a.next

    def insert_beginning(self,val):
        nb=node(val)
        nb.next=self.head
        self.head=nb

    def insert_end(self,val):
        ne=node(val)
        a=self.head
        while a.next is not None:
            a=a.next
        a.next=ne

    def insert_bet(self,val,pos):
        nbe=node(val)
        a=self.head
        for i in range(1,pos-1):
            a=a.next
        nbe.next=a.next
        a.next=nbe

    def del_beginning(self):
        a=self.head
        self.head=a.next
        self.next=None

    def del_end(self):
        p=self.head
        a=self.head.next
        while a.next is not None:
            a=a.next
            p=p.next
        p.next=None

    def del_bet(self,pos):
        p=self.head
        a=self.head.next
        for i in range (1,pos-1):
            a=a.next
            p=p.next
        p.next=a.next
        a.next=None


n1=node(1)
sl=singli_ll()
sl.head=n1
n2=node(2)
n1.next=n2
n3=node(3)
n2.next=n3
n4=node(4)
n3.next=n4
print(sl.traversal())
sl.insert_beginning(5)
print(sl.traversal())
sl.insert_end(6)
print(sl.traversal())
sl.insert_bet(7,2)
print(sl.traversal())
sl.del_beginning()
print(sl.traversal())
sl.del_end()
print(sl.traversal())
sl.del_bet(2)
print(sl.traversal())
