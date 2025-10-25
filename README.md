# Longest Common Subsequence (LCS) Algorithm

## Description

This implementation of the **Longest Common Subsequence (LCS)** algorithm finds the longest subsequence common to two input strings. A subsequence does not need to occupy consecutive positions in the original strings.

LCS is widely used in **text comparison, DNA sequence analysis, version control systems**, and pattern recognition.

## How It Works

1. **Dynamic Programming Matrix:** Computes LCS lengths for all prefixes of the two strings.
2. **Direction Matrix:** Helps trace back the path to reconstruct the LCS.
3. **Traceback:** Using the direction matrix, the longest common subsequence is reconstructed.

## Example Input

```
X = "AGCCCTAAGGGCTACCTAGCTT"
Y = "GACAGCCTACAAGCGTTAGCTTG"
```

## Example Output

```
Length Of Substring: 14
LCS: GCCCTAAGCGTAGCT
```

## Usage

1. Navigate to the folder:

```bash
cd Longest-Common-Subsequence
```

2. Run the script:

```bash
python longestCommonSubsequende.py
```

3. The program prints the dynamic programming matrix and the longest common subsequence.

## Complexity

* **Time Complexity:** O(m*n), where m and n are the lengths of the two strings.
* **Space Complexity:** O(m*n) for the cost and direction matrices.
