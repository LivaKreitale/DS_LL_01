class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
        

    def find_middle_node(self):
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
def valid_numbers(prompt):
    num_str = input(prompt).strip()
    num_list = num_str.split()
    while not all(num.isdigit() for num in num_list):
        print("invalid input")
        num_str = input(prompt).strip()
        num_list = num_str.split()
    return [int(num) for num in num_list]

num_nodes = valid_numbers("Enter the numbers ")
if len(num_nodes) > 0:
    my_linked_list = LinkedList(num_nodes[0])
    
    for value in num_nodes[1:]:
        my_linked_list.append(value)
    
    print("Middle Node :", my_linked_list.find_middle_node().value)
else:
    print("enter atleast one number.")





