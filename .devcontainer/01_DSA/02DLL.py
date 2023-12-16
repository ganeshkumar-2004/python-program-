class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next
class DLL:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None
    def insert_at_first(self,data):
        n=Node(None,data,self.start)
        if not self.is_empty():
            self.start=n
            self.start.prev=n
        else:
            n.next=None
            self.start=n
    def insert_at_last(self,data):
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            n=Node(temp,data)
            if temp is None:
                self.start=n
            temp.next=n
        else:
            self.start=n
    def search_item(self,data):
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                if temp.item==data:
                    return temp
                temp=temp.next
            return None
        return None
    def print_data(self):
        temp=self.start
        while temp.next is not None:
            print(temp.item, end=" ")
            temp=temp.next
        print(temp.item) 
    def insert_after(self,temp,data):
        if not self.is_empty():
            n=Node(temp,data,temp.next)
            if temp.next is not None:
                temp.next.prev=n
            temp.next=n
    def Delete_first(self):
        if not self.is_empty() and self.start.next is not None:
            self.start=self.start.next
    def Delete_at_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.prev.next=None
    def Delete_item(self,data):
        if self.start is None:
            pass
        else:
            temp=self.start
            while temp is not None:
                if temp.item==data:
                    if temp.next is not None:
                        temp.next.prev=temp.prev
                    if temp.prev is not None:
                        temp.prev.next=temp.next
                    else: 
                        self.start=temp.next
                    break
                temp=temp.next 
    def __iter__(self):
        return DLLIterator(self.start)    
          
class DLLIterator:
    def __init__(self,start):
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current=self.current.next
        return data
    
        


mylist=DLL()
mylist.insert_at_first(4)
mylist.insert_at_first(3)
mylist.insert_at_first(2)
mylist.insert_at_last(5)
mylist.insert_at_last(6)
mylist.insert_after(mylist.search_item(4),7)
for x in mylist:
    print(x,end=" ")
print()

