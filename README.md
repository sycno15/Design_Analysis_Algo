# Longest Repeating Subsequence (LRS) Algorithm

## Description

This implementation of the **Longest Repeating Subsequence (LRS)** algorithm finds the longest subsequence that appears **at least twice** in a string without overlapping positions.

LRS is useful in **pattern recognition, text analysis, and bioinformatics** for identifying repeated sequences.

## How It Works

1. **Dynamic Programming Matrix:** Computes LRS lengths for all positions in the string.
2. **Direction Matrix:** Tracks the direction of computation to reconstruct the LRS.
3. **Traceback:** Reconstructs the longest repeating subsequence using the direction matrix.

## Example Input

```
X = "AABCBDC"
Y = "AABCBDC"
```

## Example Output

```
Length Of Substring: 3
LRS: ABC
```

## Usage

1. Navigate to the folder:

```bash
cd Longest-Repeating-Subsequence
```

2. Run the script:

```bash
python longestRepeatingSubsequence.py
```

3. The program prints the dynamic programming matrix and the longest repeating subsequence.

## Complexity

* **Time Complexity:** O(n^2), where n is the length of the string.
* **Space Complexity:** O(n^2) for the cost and direction matrices.

## Contributing

Contributions are welcome! You can:

* Improve existing implementations
* Add related algorithms
* Fix bugs or optimize code

Please fork the repository, create a branch for your changes, and submit a pull request.

## License

This project is licensed under the MIT License.
