# Design_Analysis_Algo

This repository contains implementations of classical **Design and Analysis of Algorithms**. Each algorithm is implemented in a separate module with clear examples, making it easy for learning, experimentation, and reference.

## 🐭 Repository Structure

```
Design_Analysis_Algo/
├── Longest-Common-Subsequence/
│   └── longestCommonSubsequence.py
├── Longest-Repeating-Subsequence/
│   └── longestRepeatingSubsequence.py
├── Bellman-Ford-Algo/
│   └── bellmanFord.py
├── Optimal-Binary-Search-Tree/
│   └── optimanBinarySearchTree.py
└── README.md
```

## 🧩 Algorithms Included

1. **Longest Common Subsequence (LCS)**
   Finds the longest subsequence common to two sequences. Useful in text comparison, DNA sequencing, and version control.

2. **Longest Repeating Subsequence (LRS)**
   Finds the longest subsequence that appears **at least twice** in a sequence without overlapping. Useful in pattern analysis.

3. **Bellman-Ford Algorithm**
   Computes shortest paths from a single source vertex to all other vertices in a weighted graph. Supports negative weight edges.

4. **Optimal Binary Search Tree (OBST)**
   Constructs a BST that **minimizes search cost** given a set of keys with access probabilities.

## ⚡ Usage Example

1. Clone the repository:

```bash
git clone https://github.com/yourusername/Design_Analysis_Algo.git
cd Design_Analysis_Algo
```

2. Navigate to the algorithm folder and run the code:

```bash
# Example: Longest Common Subsequence
cd Longest-common-subsequence
python longestCommonSubsequence.py
```

## 🗑️ Example

**LCS Example:**

```python
X = "AGGTAB"
Y = "GXTXAYB"
# Output: Length of LCS is 4
```

**Bellman-Ford Example:**

```python
# Weighted graph with 5 vertices
# Source = 0
# Output: Shortest distances from source 0: 0 -1 2 -2 1
```

## ⏱️ Time & Space Complexities

| Algorithm    | Time Complexity | Space Complexity |
| ------------ | --------------- | ---------------- |
| LCS          | O(m*n)          | O(m*n)           |
| LRS          | O(n^2)          | O(n^2)           |
| Bellman-Ford | O(V*E)          | O(V)             |
| OBST         | O(n^3)          | O(n^2)           |


## 📜 License

This project is licensed under the **MIT License**.
