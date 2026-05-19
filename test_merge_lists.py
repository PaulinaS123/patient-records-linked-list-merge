import unittest
from src.linked_list import create_linked_list
from src.merge_lists import merge_lists


def linked_list_to_list(head):
    result = []

    while head:
        result.append(head.ssn)
        head = head.next

    return result


class TestMergeLists(unittest.TestCase):

    def test_basic_merge(self):
        list1 = create_linked_list([
            (101, "Alice", 30),
            (303, "Bob", 45)
        ])

        list2 = create_linked_list([
            (202, "Charlie", 25),
            (404, "David", 50)
        ])

        merged = merge_lists(list1, list2)

        self.assertEqual(
            linked_list_to_list(merged),
            [101, 202, 303, 404]
        )

    def test_empty_lists(self):
        merged = merge_lists(None, None)

        self.assertEqual(
            linked_list_to_list(merged),
            []
        )

    def test_duplicates(self):
        list1 = create_linked_list([
            (101, "Alice", 30),
            (202, "Bob", 45)
        ])

        list2 = create_linked_list([
            (202, "Charlie", 25),
            (303, "David", 50)
        ])

        merged = merge_lists(list1, list2)

        self.assertEqual(
            linked_list_to_list(merged),
            [101, 202, 202, 303]
        )


if __name__ == "__main__":
    unittest.main()
