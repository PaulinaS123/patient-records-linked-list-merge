from src.node import Node


def merge_lists(head1, head2):
    dummy = Node(0, "", 0)
    tail = dummy

    while head1 and head2:
        if head1.ssn <= head2.ssn:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next

        tail = tail.next

    if head1:
        tail.next = head1

    if head2:
        tail.next = head2

    return dummy.next
