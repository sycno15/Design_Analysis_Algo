# Optimal Binary Search Tree (OBST) Algorithm

## Description

This implementation of the **Optimal Binary Search Tree (OBST)** algorithm constructs a binary search tree that **minimizes the expected search cost** given a set of sorted keys (book IDs) and their search probabilities.

OBST is widely used in **database indexing, compiler design, and search optimization**.

## How It Works

1. **Input:**

   * Sorted keys (e.g., book IDs).
   * Probabilities of successful searches for each key (p[i]).
   * Probabilities of unsuccessful searches (q[i]).
2. **Dynamic Programming Matrices:** Computes expected search costs and cumulative probabilities.
3. **Optimal Cost Computation:** Finds the tree configuration that minimizes the expected cost.

## Example Input

```
Number of books: 3
Book IDs: 10,12,20
Probabilities of successful searches (p): 0.34,0.08,0.50
Probabilities of unsuccessful searches (q): 0.1,0.1,0.05,0.05
```

## Example Output

```
The expected cost of the Optimal Binary Search Tree is: 2.24
```

## Usage

1. Navigate to the folder:

```bash
cd Optimal-Binary-Search-Tree
```

2. Run the script:

```bash
python optimalBinarySearchTree.py
```

3. Provide input as prompted for number of keys, keys, and their probabilities.

## Complexity

* **Time Complexity:** O(n^3), where n is the number of keys.
* **Space Complexity:** O(n^2) for dynamic programming matrices.

