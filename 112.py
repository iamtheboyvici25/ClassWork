class Node:
    def __init__(self,data):
        self.data=data
        self.next=None



class LinkedList:
    def __init__ (self):
        self.head= None

    def InsertAtTheBeginning(self,new_data):
        new_node=Node(new_data)
        new_node.next= self.head
        self.head=new_node


    def printLinkedList(self):
        temp=self.head
        while temp:
            print(temp.data,end=' ')

            temp= temp.next
        print()

    def insertAtTheEnd(self,new_data):
        new_node= Node(new_data)

        if self.head is None:
         self.head=new_node
         return None



        last =self.head


        while last.next:
            last = last.next
        last.next=new_node


if __name__ =='__main__':
    llist=LinkedList()

    llist.InsertAtTheBeginning("Fox")
    llist.InsertAtTheBeginning("Brown")
    llist.InsertAtTheBeginning("Quick")
    llist.InsertAtTheBeginning("The")

    llist.printLinkedList()

llist.insertAtTheEnd("Jumps")
llist.printLinkedList()

