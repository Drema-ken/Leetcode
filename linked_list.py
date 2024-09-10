class Node:
    data = None
    next_node = None

    def __init__(self,data):
        self.data = data

    def __repr__(self) -> str:
        return '<Node data: %s>' % self.data
    
class linked_list:
    """singly linked list"""
    def __init__(self) -> None:
        self.head = None

    def is_empty(self):
        return self.head  == None
    """returns number of nodes in list takes linear time"""
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count

    """Adds new node containing data at the head of the list takes 0(1)"""
    def add(self,data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def insert(self,index,data):
        """insert node at index takes linear time for searching =O(n) and inserting = O(1) """
        new_node = Node(data)
        if index == 0 :
            self.add(new_node)
        else:
            position = index
            current = self.head

            while position > 1:
                current= current.next_node
                position -= 1

            next_node = current.next_node
            current.next_node= new_node
            new_node.next_node = next_node
                
        
    def search(self,key=False,index=False):
        """searches list based on value provided i.e index or key
            if key is provided  only first value found is returned
        """
        if index:
            if index == 0:
                return self.head
            else:
                position = index
                current = self.head
                while position >= 1:
                    current = current.next_node
                    position -= 1
                return current
        else:
            current = self.head
            position = 0
            found = False
           
            if current.data == key:
                     print(current.data,key)
                     return 'Found %s at index : %s' % (key,position)
            while current and not found:
                if current.data == key:
                    found = True
                    return 'Found %s at index : %s' % (key,position)
                else: 
                    position +=1
                    current = current.next_node
                return 'List does not contain key: %s' % key
            
    def remove(self,key=False,index=False):
        if key:
            current = self.head
            prev = None 
            found = False
            
            while current and not found:
                if current.data == key and current is self.head:
                    found =True
                    self.head = current.next_node
                    print('found at start')
                elif current.data == key:
                    found =True
                    prev.next_node = current.next_node
                    
                else:
                    prev = current
                    current = current.next_node
            return current
        else:
            position = 0
            current = self.head
            prev = None

            while position <= index:
                if position == 0 and index == 0:
                    prev = current.next_node
                    self.head = prev
                    return current
                elif position == index:
                    prev.next_node = current.next_node
                    return current
                else:
                    prev = current
                    current = current.next_node
                    position += 1
           
        
    def __repr__(self) -> str:
        node = []
        current = self.head
        
        while current:
            if current == self.head:
                node.append('[Head %s]' % current.data)
            elif current.next_node == None:
                node.append('[Tail %s]' % current.data)
            else:
                node.append('[%s]' % current.data)
            current = current.next_node
        
        return '%s' % node

n1 = Node(10)
n2= Node(20)
n1.next_node = n2

l = linked_list()
l.head = n1


l.add(20)
l.add(40)
print(l)

print(l)


