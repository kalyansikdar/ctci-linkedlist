class node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_node(head):
    while head!=None:
        print (head.data)
        head = head.next
  
def delete_node(head, value):
  fakeHead = node(None)     # Needs to create a fake head in case the node has to be deleted.
  current = head
  fakeHead.next = current

  while current:
    if current.next.data == value:
      current.next=current.next.next
    current=current.next
  return head


head = node(None)
n1 = node(5)
n2 = node(7)
n3 = node(1)
n4 = node(5)

head.next = n1
n1.next = n2
n2.next = n3
n3.next = n4

print_node(head)
print()
result = delete_node(head, 5)
print()
print_node(result)
