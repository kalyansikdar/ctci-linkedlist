class node:
    def __init__(self, data):
        self.val = data
        self.next = None

def print_node(head):
    curr = head
    while curr:
        print (curr.val, end="->")
        curr = curr.next

def remove_dups_with_dict(head):
    holder = {}
    curr = head
    prev = None

    while curr:
        if curr.val not in holder:
            holder[curr.val] = 1
            prev = curr
        else:
            prev.next = curr.next
        curr = curr.next
    
    return head

def remove_dups(head):
    curr = head
    while curr:
        curr_fast = curr
        while curr_fast.next:
            print(curr.val, curr_fast.val)
            if curr.val == curr_fast.next.val:
                curr_fast.next = curr_fast.next.next
            else:
                curr_fast = curr_fast.next
        curr = curr.next    
    return head

n1 = node(5)
n2 = node(7)
n3 = node(1)
n4 = node(5)
n5 = node(9)
n6 = node(7)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6

print_node(n1)
print()
print(print_node(remove_dups(n1)))
