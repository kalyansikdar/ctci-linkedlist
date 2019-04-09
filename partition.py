class node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_node(head):
    while head!=None:
        print (head.data)
        head = head.next

def add_node(head, value):
  current = head
  new_node = node(value)
  if current == None:
    current.next = new_node
  else:
    while current.next!= None:
      current = current.next
    current.next = new_node
  

def partition(head, value):
  current = head
  list1 = node(None)
  list2 = node(None)

  while current != None:
    if current.data < value:
      add_node(list1, current.data)
    else:
      add_node(list2, current.data)

    current = current.next
  
  current = list1
  while current.next != None:
    current = current.next
  current.next = list2.next

  return list1.next


def partition(head, key):
    curr = head
    holder = {'less':[], 'more': []}
    while curr:
        if curr.val < key:
            holder['less'].append(curr.val)
        else:
            holder['more'].append(curr.val)
        curr = curr.next
    
    res = node(None)
    dummy = res
    print(holder)
    for k in holder:
        for v in holder[k]:
            print (v)
            dummy.next = node(v)
            dummy = dummy.next
    
    return res.next

n1 = node(3)
n2 = node(5)
n3 = node(8)
n4 = node(5)
n5 = node(10)
n6 = node(2)
n7 = node(1)


n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7

print_node(n1)
print()
result = partition(n1, 5)
print_node(result)
