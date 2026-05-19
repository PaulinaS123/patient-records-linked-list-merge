# patient-records-linked-list-merge

This project solves the problem of merging two sorted linked lists that represent patient records from two healthcare providers.

Each linked list is already sorted by SSN number. The goal is to merge both lists into one sorted linked list while preserving all patient records, including duplicates.

# Clarifying Questions

1. Are both linked lists guaranteed to already be sorted?
2. Can duplicate SSNs exist?
3. Should duplicates remain in the merged list?
4. Can one or both linked lists be empty?
5. Should the merge happen in-place or create a new list?
6. What should happen if both lists contain identical patient records?

# Data Structure Design

Each node contains:
- SSN
- Patient Name
- Age
- Pointer to next node

# Linked List Merge Diagram

## Input Lists

### Healthcare Provider A

```text
[101 | Alice] → [303 | Bob] → [505 | Carol] → None
```

### Healthcare Provider B

```text
[202 | David] → [404 | Emma] → [606 | Frank] → None
```

---

# Merge Process

```text
Compare 101 and 202
↓
101 is smaller → add 101

Merged List:
101
```

```text
Compare 303 and 202
↓
202 is smaller → add 202

Merged List:
101 → 202
```

```text
Compare 303 and 404
↓
303 is smaller → add 303

Merged List:
101 → 202 → 303
```

```text
Continue until all nodes are merged...
```

---

# Final Merged List

```text
101 → 202 → 303 → 404 → 505 → 606 → None
```

---

# Algorithm Flowchart

```text
Start
  ↓
Compare current nodes
  ↓
Select smaller SSN
  ↓
Attach node to merged list
  ↓
Move pointer forward
  ↓
Repeat until one list is empty
  ↓
Attach remaining nodes
  ↓
End
```

# Algorithm Explanation

The algorithm compares the current nodes from both linked lists.

- The smaller SSN is added to the merged list.
- The pointer for that list moves forward.
- This continues until one list becomes empty.
- The remaining nodes are appended at the end.

# Time and Space Complexity

## Time Complexity
O(n + m)

n = number of nodes in list 1
m = number of nodes in list 2

## Space Complexity
O(1)

The merge is performed in-place using existing nodes.

# How to Run the Project

## 1. Clone the Repository

git clone https://github.com/your-username/patient-records-linked-list-merge.git

## 2. Navigate Into the Project Folder
``` bash
cd patient-records-linked-list-merge
```
## 3. Run the Unit Tests
``` bash
python -m unittest discover tests
```
## Test Cases

- Normal Case 1 — Basic Merge
Input
List A:
101 -> 303 -> 505

- List B:
202 -> 404 -> 606
Expected Output
101 -> 202 -> 303 -> 404 -> 505 -> 606

Purpose
Tests standard alternating merge behavior.

- Normal Case 2 — Different List Sizes
Input
List A:
100 -> 300

- List B:
150 -> 250 -> 350 -> 450
Expected Output
100 -> 150 -> 250 -> 300 -> 350 -> 450

Purpose
Ensures the algorithm handles lists with different lengths.

- Normal Case 3 — Duplicate SSNs
Input
List A:
101 -> 202

- List B:
202 -> 303
Expected Output
101 -> 202 -> 202 -> 303

Purpose
Verifies duplicate patient records remain in the merged list.

## Edge Test Cases

- Edge Case 1 — One Empty List
Input
List A:
empty

- List B:
100 -> 200
Expected Output
100 -> 200

Purpose
Ensures the algorithm works if one healthcare provider has no records.

- Edge Case 2 — Both Lists Empty
Input
List A:
empty

- List B:
empty
Expected Output
empty

Purpose
Tests completely empty input.

- Edge Case 3 — All Values Smaller in One List
Input
List A:
100 -> 200 -> 300

- List B:
400 -> 500
Expected Output
100 -> 200 -> 300 -> 400 -> 500

Purpose
Tests appending the remaining nodes efficiently.

