from src.node import Node


def create_linked_list(records):
    if not records:
        return None

    head = Node(*records[0])
    current = head

    for record in records[1:]:
        current.next = Node(*record)
        current = current.next

    return head


def print_list(head):
    current = head

    while current:
        print(f"{current.ssn} -> ", end="")
        current = current.next

    print("None")
