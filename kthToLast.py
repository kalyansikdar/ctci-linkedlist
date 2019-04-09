class node:
    def __init__(self, data):
        self.data=data
        self.next = None
        
def print_node(head):
    while head!=None:
        print (head.data)
        head = head.next
        

def findKthtoLast(head,K):
    current = head
    j=0
    while j < K:
        current = current.next
        j+=1
    
    return current


def KthtoLast(head, K):
    i=0
    j=0
    current = head
    while current!=None:
        i+=1
        current=current.next
    current = head
    
    while j < i-K:
        j+=1
        current=current.next
    
    return current


def kthToLast(head, k):
"""
Best solution: Two pointed solution
"""
    first = head
    second = head

    while k:
        first = first.next
        k -= 1
    
    while first:
        first = first.next
        second = second.next

    return second.val
    
        
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
result = findKthtoLast(head, 1)
print()
print_node(result)
print()
result = KthtoLast(head,3)
print()
print(result.data)
print_node(result)
