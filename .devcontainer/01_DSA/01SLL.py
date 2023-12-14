class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class DLL:
    def __init__(self,start=None):
        self.start=start
    def insert_at_start(self,data):
        n=Node(data,self.start)
        self.start=n
    def is_empty(self):
        return self.start==None
    def insert_at_last(self,data):
        if not self.is_empty():
            

