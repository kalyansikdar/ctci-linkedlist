class node():
    def __init__(self, data):
        self.data = data
        self.next = None

def print_node(head):
    current = head
    while current!=None:
        print(current.data)
        current = current.next

def sumLists(ll1, ll2):
    cur1 = ll1
    cur2 = ll2
    count1=0
    count2=0
    result = []
    r1 = node(None)
    temp = 0
    while cur1!=None:
        count1+=1
    while cur2!=None:
        count2+=1

    cur1 = ll1
    cur2 = ll2

    if count2 > count1:
        ll1, ll2 = ll2, ll1

    while cur1 != None:
        temp = temp + cur1.data+cur2.data
        if (temp < 10):
            result.append(temp)
        else:
            result.append(temp-10)
            temp = 1
        cur1=cur1.next
        cur2=cur2.next
    print(result)

    current = r1
    for i in result:
        current.next = node(i)
        current = current.next

    return r1.next


def sumLists_correct(ll1,ll2):
    """
    Determine while llist is longer, make cur1 as the longer one and run loop based on that. Maintain carry in temp var
    :param ll1:
    :param ll2:
    :return:
    """
    cur1 = ll1
    cur2 = ll2
    r1 = node(None)
    current = r1
    length1 = 0
    length2 = 0
    while cur1!=None:
        length1 +=1
        cur1 = cur1.next
    while cur2!=None:
        length2 +=1
        cur2 = cur2.next

    if length2> length1:
        ll1, ll2 = ll2, ll1
    temp = 0
    cur1 = ll1
    cur2 = ll2
    print_node(cur1)
    print()
    print_node(cur2)

    while cur1 != None:
        c = cur2.data

        temp = temp + cur1.data + cur2.data
        if temp < 10:
            current.next = node(temp)
            temp =0
        else:
            current.next = node(temp%10)
            temp =1

        current = current.next
        if cur2.next == None:
            cur2.next = node(0)
        cur1 = cur1.next
        cur2 = cur2.next
    return r1.next


def sumLists_another_time(head1, head2):
    l1 = head1
    l2 = head2
    count1, count2 = 0,0

    while l1:
        l1 = l1.next
        count1 += 1

    while l2:
        l2 = l2.next
        count2 += 1

    l1 = head1
    l2 = head2

    if count2 > count1:
        l1, l2 = l2, l1

    reminder = 0
    result = node(None)
    r = result
    while l2:
        add_val = l1.val + l2.val + reminder
        if add_val <= 9:
            result.next = node(add_val)
        else:
            res = add_val%10
            result.next = node(res)
            reminder = 1

        result = result.next
        l2 = l2.next
        l1 = l1.next
    
    if l1:
        result.next = l1

    return r

e1 = node(7)
e2 = node(1)
e3 = node(6)

e1.next = e2
e2.next = e3

f1 = node(5)
f2 = node(9)
f3 = node(2)
f1.next = f2
f2.next = f3

print_node(e1)
print()
print_node(f1)
print()
result = sumLists1(e1, f1)
print_node(result)
