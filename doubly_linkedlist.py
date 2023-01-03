class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class doubly_ll:
    def __init__(self):
        self.head=None

    def foward_traversal(self):
        if self.head is None:
            print('list is empty')
        else:
            a=self.head
            while a is not None:
                print(a.data,end=' ')
                a=a.next
    def reverse_traversal(self):
        if self.head is None:
            print('list is empty')
        else:
            a=self.head
            while a.next is not None:
                a=a.next
            while a is not None:
                print(a.data, end=' ')
                a=a.prev

    def insert_beggining(self,data):
        nb=node(data)
        a=self.head
        nb.next=a
        a.prev=nb
        self.head=nb

    def insert_end(self,data):
        ne=node(data)
        a=self.head
        while a.next is not None:
            a=a.next
        a.next=ne
        ne.prev=a

    def insert_bet(self,data,pos):
        nbe=node(data)
        a=self.head
        for i in range(1,pos-1):
            a=a.next
        nbe.prev=a
        nbe.next=a.next
        a.next.prev=nbe
        a.next = nbe
    def del_beginning(self):
        a=self.head
        self.head=a.next
        a.next=None
    def del_end(self):
        p=self.head
        a=self.head.next
        while a.next is not None:
            a=a.next
            p=p.next
        a.prev=None
        p.next=None
    def del_bet(self,pos):
        p=self.head
        a=self.head.next
        for i in range(1,pos-1):
            a=a.next
            p=p.next
        p.next=a.next
        a.next.prev=p
        a.next=None
        a.prev=None

n1=node(1)
dl=doubly_ll()
dl.head=n1
n2=node(2)
n1.next=n2
n2.prev=n1
n3=node(3)
n2.next=n3
n3.prev=n2
n4=node(4)
n3.next=n4
n4.prev=n3
print(dl.foward_traversal())
print(dl.reverse_traversal())
dl.insert_beggining(6)
print(dl.foward_traversal())
print(dl.reverse_traversal())
dl.insert_end(7)
print(dl.foward_traversal())
print(dl.reverse_traversal())
dl.insert_bet(8,3)
print(dl.foward_traversal())
print(dl.reverse_traversal())
dl.del_beginning()
print(dl.foward_traversal())
print(dl.reverse_traversal())
dl.del_end()
print(dl.foward_traversal())
print(dl.reverse_traversal())
dl.del_bet(3)
print(dl.foward_traversal())
print(dl.reverse_traversal())







