class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class CLL:
    def __init__(self,last=None):
        self.last=last
    def is_empty(self):
        return self.last==None
    def insert_at_start(self,data):
        n=Node(data)
        if not self.is_empty():
            n.next=self.last.next
            self.last.next=n
        else: 
            n.next=n
            self.last=n
       
    def insert_at_last(self,data):
        n=Node(data)
        if not self.is_empty():
            n.next=self.last.next
            self.last.next=n
            self.last=n
        else:
           n.next=n
           self.last=n
    def search_item(self,data):
        if not self.is_empty():
            temp=self.last.next
            while temp is not self.last:
                if temp.item==data:
                  return temp
                temp=temp.next
            if temp.item==data:
                return temp 
            return None
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n
            if temp==self.last:
                self.last=n
    def print_item(self):
        if not self.is_empty():
            temp=self.last.next
            while temp is not self.last:
                print(temp.item,end=" ")
                temp=temp.next
        print(temp.item)
    def Delete_at_first(self):
        if not self.is_empty():
            if self.last.next==self.last:
                self.last=None
            self.last.next=self.last.next.next
    def Delete_at_last(self):
        if not self.is_empty():
           if self.last.next==self.last:
               self.last=None
           else:
                temp=self.last.next
                while temp.next is not self.last:
                    temp=temp.next
                temp.next=self.last.next
                self.last=temp

    def Delete_item(self,data):
         if not self.is_empty():
            if self.last.next==self.last:
                self.last=None
            else:
                if self.last.next.item==data:
                    self.Delete_at_first()
                temp=self.last.next    
                while temp.next is not self.last:
                    if temp.next.item==data:
                        temp.next=temp.next.next
                        break
                    if temp.next==self.last:
                        if self.last.item==data:
                            self.Delete_at_last()
                        break
                    temp=temp.next
    def __iter__(self):
        if self.last==None:
             return CLLIterator(None)    
        else:
            return CLLIterator(self.last.next)           
class CLLIterator:
    def __init__(self,start):
        self.current=start
        self.start=start
        self.count=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current==None:
            raise StopIteration
        if self.current==self.start and self.count==1:
            raise StopIteration
        else:
            self.count=1
        data=self.current.item
        self.current=self.current.next
        return data



mylist=CLL()
mylist.insert_at_start(5)
mylist.insert_at_last(4)
mylist.insert_at_last(8)
mylist.insert_at_last(3)
mylist.insert_at_last(6)
mylist.insert_at_start(9)
mylist.insert_after(mylist.search_item(8),66)
mylist.print_item()
mylist.Delete_item(66)
for x in mylist:
    print(x,end=" ")

