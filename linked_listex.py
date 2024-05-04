class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def insert_front(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            new=node(data)
            new.next=self.head
            self.head=new
    def end_insert(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            new=node(data)
            i=self.head
            while i.next!=None:
                i=i.next
            i.next=new
    def printing(self):
        if self.head==None:
            print("List is empty")
        i=self.head
        c=0
        while i:
            c=c+1
            print(i.data)
            i=i.next
        print("count = ",c)
    def front_del(self):
        if self.head==None:
            print("cant delete")
        else:
            '''i=self.head
            self.head=self.head.next
            del i'''
            self.head=self.head.next
    def end_del(self):
        if self.head==None:
            print("cant delete")
        else:
            '''i=self.head
            while i.next!=None:
                j=i
                i=i.next
            j.next=None
            del i'''
            i=self.head
            while i.next.next:
                i=i.next
            i.next=None
    def rev1(self):
        prev=None
        curr=self.head
        nxt=self.head.next
        while curr:
            if curr.next==None:
                self.head=curr
            curr.next=prev
            prev=curr
            curr=nxt
            if nxt:
                nxt=nxt.next
    def insert_pos(self,da,pos):
        i=self.head
        if i==None and pos==1:
            new=node(da)
            self.head=new
        elif i.next==None and pos==1:
            new=node(da)
            new.next=i
            i=new
        elif i.next==None and pos==2:
            new=node(da)
            i.next=new
        else:
            new=node(da)
            count=0
            while i.next!=None:
                count=count+1
                if pos==count:
                    break
                else:
                    j=i
                    i=i.next
            if pos==1:
                new.next=i
            else:
                j.next=new
                new.next=i
                    
l=[1,2,3,4,5]
obj=sll()
for i in l:
    obj.end_insert(i)
#obj.insert_pos(6,1)  
#obj.end_del()
obj.front_del()
obj.printing()
"""while(obj.head!=None):
    print(obj.head.data)
    obj.head=obj.head.next"""