'''
ES Data Structures
Homework 1
Areg Karapetyan
'''

class DequeArray:
    def __init__(self,size):
        # Create empty deque and fill with 'None' using the given size of the list
        self.deque = []
        for i in range(size):
            self.deque.append(None)

    def addFirst(self,NewVal):
        # Add new element at the beginning of the deque
        if self.deque[0] is None:
            self.deque[0]=NewVal
        elif self.deque[-1] is None:
            a = 1%len(self.deque)
            self.deque = self.deque[-a:]+self.deque[:-a]
            self.deque[0] = NewVal
        else:
            self.resize()
            a = 1 % len(self.deque)
            self.deque = self.deque[-a:] + self.deque[:-a]
            self.deque[0] = NewVal

    def addLast(self,NewVal):
        # Add new element to the end of the deque
        for i in range(len(self.deque)):
            if self.deque[i] is None:
                self.deque[i]=NewVal
                return
        self.resize()
        last_index=int(len(self.deque)/2)
        self.deque[last_index]=NewVal

    def removeFirst(self):
        # Remove the first element of the deque
        self.deque.pop(0)
        self.deque.append(None)

    def removeLast(self):
        # Remove the last element of the deque
        last_index = self.last_index()
        self.deque[last_index]=None

    def first(self):
        # Returns the first element of the deque
        return self.deque[0]

    def last(self):
        # Returns the last non-"None" element of the deque
        l_index = self.last_index()
        return self.deque[l_index]

    def last_index(self):
        # Returns the index of the last non-"None" element of the deque
        for i in range(len(self.deque)):
            if self.deque[i] is None:
                return i-1
        return len(self.deque)-1

    def resize(self):
        # Resizes the deque after the size limit is reached by adding "None" elements, so that the deque will double its size
        b = []
        for i in range(len(self.deque)):
            b.append(None)
        self.deque = self.deque + b

    def print_deq(self):
        # Prints the deque
        print (self.deque)

class Node:
    # Class to create nodes for linked list
    def __init__(self,DataVal=None):
        self.DataVal = DataVal
        self.NextVal = None
        self.PrevVal = None

class DLinkedList:
    last = None     #to keep the last element

    def __init__(self):
        self.HeadVal= None

    def listprint(self, node):
        # Prints the linked list
        while node is not None:
            print(node.DataVal),
            node = node.NextVal

    def addFirst(self,NewData):
        # Adds new element to the beginning of the list
        NewNode = Node(NewData)
        NewNode.NextVal = self.HeadVal
        if self.HeadVal is None:
            self.last = NewNode
        if self.HeadVal is not None:
            self.HeadVal.PrevVal = NewNode
        self.HeadVal = NewNode

    def addLast(self, NewData):
        # Adds new element to the end if the list
        NewNode = Node(NewData)
        NewNode.NextVal = None
        if self.HeadVal is None:
            NewNode.PrevVal = None
            self.HeadVal = NewNode
            return
        last = self.HeadVal
        while (last.NextVal is not None):
            last = last.NextVal
        last.NextVal = NewNode
        NewNode.PrevVal = last
        self.last = NewNode
        return

    def InsertAfter(self, PrevNode, NewData):
        #   Inserts new element after the given element
        if PrevNode is None:
            return
        NewNode = Node(NewData)
        NewNode.NextVal = PrevNode.NextVal
        PrevNode.NextVal = NewNode
        NewNode.PrevVal = PrevNode
        if NewNode.NextVal is not None:
            NewNode.NextVal.PrevVal = NewNode

    def InsertBefore(self, NextNode, NewData):
        #   Inserts new element before the given element
        if NextNode is None:
            return
        NewNode = Node(NewData)
        NewNode.PrevVal = NextNode.PrevVal
        NextNode.PrevVal = NewNode
        NewNode.NextVal = NextNode
        if NewNode.NextVal is not None:
            NewNode.PrevVal.NextVal = NewNode

    def RemoveNode(self, RemoveKey):
        # Removes an elements from linked list using the provided remove key
        HeadVal = self.HeadVal

        if HeadVal is not None:
            if HeadVal.DataVal == RemoveKey:
                self.HeadVal = HeadVal.NextVal
                HeadVal = None
                return
        while HeadVal is not None:
            if HeadVal.DataVal == RemoveKey:
                break
            prev = HeadVal
            HeadVal = HeadVal.NextVal
        if HeadVal == None:
            return
        prev.NextVal = HeadVal.NextVal

        HeadVal = None

    def RemoveFirst(self):
        #   Removes the first element of the list
        self.RemoveNode(self.First())

    def RemoveLast(self):
        #   Removes the last element of the list
        self.RemoveNode(self.last.DataVal)
        self.last = self.last.PrevVal

    def First(self):
        #   Returns the first element of the list
        return self.HeadVal.DataVal

    def Last(self):
        #   Returns the last element of the list
        return self.last.DataVal

    def IndexOf(self,node):
        #   Returns the index of the needed element of the list
        elem = self.HeadVal
        index = 0
        while elem is not None:
            if elem.DataVal == node:
                return index
            elem = elem.NextVal
            index += 1

    def Size(self):
        #   Returns the size of the list
        size = 1
        elem = self.HeadVal
        if elem == None:
            return 0
        while elem is not None:
            if elem.NextVal == None:
                return size
            elem = elem.NextVal
            size += 1

def sort_by_indexes(dll):
    # Function which parses the linked list into two lists based on their indexes(odd, even)
    even_sub = []
    odd_sub = []
    compare = dll.HeadVal # value which is getting parsed into even/odd lists
    counter = 0 #counter which plays the role of the index in the linked list
    while compare is not None:
        if counter % 2 == 0:
            even_sub.append(compare.DataVal)
            counter += 1
            compare = compare.NextVal
        elif counter % 2 == 1:
            odd_sub.append(compare.DataVal)
            counter += 1
            compare = compare.NextVal
    return even_sub, odd_sub

def main():
    '''
    #    Tests for checking how Deque class works based on cyclic array (Exrecise 1)

    deq_test = DequeArray(3)#size = 3
    deq_test.addFirst("Tue")
    deq_test.addFirst("Mon")
    deq_test.addLast("Wed")
    deq_test.addLast("Thu")
    deq_test.addLast("Fri")

    deq_test.print_deq()
    print(deq_test.last())
    deq_test.removeLast()
    deq_test.removeFirst()
    deq_test.print_deq()
    print(deq_test.first())
    '''

    '''
    #    Tests for checking how Deque works based on double linked list (Exercise 2)
    
    deq_test = DLinkedList()
    deq_test.addFirst("Tue")
    deq_test.addLast("Wed")
    deq_test.addFirst("Mon")
    deq_test.addLast("Thu")
    deq_test.addLast("Fri")
    print("----------------")
    deq_test.listprint(deq_test.HeadVal)
    print("----------------")
    deq_test.RemoveFirst()
    deq_test.RemoveLast()
    print("----------------")
    deq_test.listprint(deq_test.HeadVal)
    print("----------------")
    print(deq_test.First())
    print(deq_test.Last())
    '''

    '''
    #   Test for checking how double linked list works (Exercise 3)
    
    dll_test = DLinkedList()
    dll_test.addFirst("Mars")
    dll_test.addLast("Jupiter")
    dll_test.addFirst("Venus")
    dll_test.addLast("Saturn")
    dll_test.addFirst("Mercury")
    dll_test.addFirst("Sun")
    dll_test.addLast("Uranus")
    dll_test.addLast("Neptune")
    print(dll_test.last.DataVal)
    print("--------Initial Linked List--------")
    dll_test.listprint(dll_test.HeadVal)
    print("-----------------------------------")

    dll_test.RemoveFirst()
    dll_test.InsertAfter(dll_test.HeadVal.NextVal,"Earth")
    dll_test.RemoveLast()
    dll_test.RemoveNode("Mars")

    print("--------Linked list after removing first and last elements, removing 'Mars' and adding 'Earth'--------")
    dll_test.listprint(dll_test.HeadVal)
    print("--------First and last elements right now--------")
    print(dll_test.First())
    print(dll_test.Last())
    '''

    '''
    #   Parsing two lists from double linked list according to even/odd indexes (Exercise 4)
    
    dll = DLinkedList()
    dll.addFirst("Tokyo")
    dll.addLast("Rio")
    dll.addFirst("Nairobi")
    dll.addLast("Moscow")
    dll.addFirst("Berlin")
    dll.addLast("Stockholm")
    dll.addFirst("Helsinki")
    dll.addLast("Oslo")
    dll.addFirst("Denver")
    dll.addLast("Lisbon")
    print("----------------")
    dll.listprint(dll.HeadVal)
    print("----------------")

    even,odd=sort_by_indexes(dll)
    print(even,odd)
    '''

main()