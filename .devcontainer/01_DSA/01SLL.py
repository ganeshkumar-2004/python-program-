     
class Node:
     def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class SLL:
     def __init__(self,start=None):
        self.start=start
     
     def is_empty(self):
        return self.start is None
     
     def insert_at_start(self,data):
        n=Node(data,self.start)
        self.start=n
     def insert_at_last(self,data):
          n=Node(data)
          if not self.is_empty():
               temp=self.start
               while temp.next is not None:
                    temp=temp.next
               temp.next=n
       
     def search_item(self,data):
        temp=self.start
        while temp is not None:
             if temp.item==data:
                 return temp
             temp=temp.next
        return None
     def insert_after(self,temp,data):
             if temp:
                n=Node(data,temp.next)
                temp.next=n
     
     def print_item(self):
        temp=self.start
        while temp is not None:
             print(temp.item,end=" ") 
             temp=temp.next
        print()
     
     def Delete_first(self):
        if  self.is_empty():
             print("there is not any item present in the list",end=" ") 
        else:
             self.start=self.start.next
     
     def Delete_at_last(self):
        if self.is_empty():
             pass
        elif self.start.next is None:
             self.start=None
        else:
             temp=self.start
             while temp.next.next is not None:
                 temp=temp.next
             temp.next=None
     
     def Delete_item(self,data):
        if self.is_empty():
             pass
        elif self.start.item==data:
               self.start=self.start.next
        else:
             temp=self.start
             if temp.item==data:
                 self.start=None
             else:
                 while temp.next is not None:
                     if temp.next.item==data:
                         temp.next=temp.next.next
                         break
                     temp=temp.next
     def __iter__(self):
         return SLLIterator(self.start)
                   
            
class SLLIterator:
    def __init__(self,start):
        self.current  = start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data=self.current.item
        self.current=self.current.next
        return data
mylist=SLL()
mylist.insert_at_start(4)
mylist.insert_at_start(3)
mylist.insert_at_start(2)
mylist.insert_at_last(7)
mylist.insert_after(mylist.search_item(5),8)
mylist.Delete_first()
mylist.Delete_at_last()
mylist.Delete_item(5)
mylist.insert_at_start(5)
mylist.insert_at_last(27)
mylist.insert_at_last(67)
mylist.insert_at_last(10)
for x in mylist:
    print(x,end=" ")
print()
     
