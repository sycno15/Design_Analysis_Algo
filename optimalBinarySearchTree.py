import pandas as pd
import numpy as np
'''
Taking input as: 

First line: integer n — number of book IDs.
Second line: n integers representing the sorted book IDs (keys).
Third line: n real numbers — probabilities of successful searches (p[i]).
Fourth line: n+1 real numbers — probabilities of unsuccessful searches (q[i]).

'''

n=int(input("Enter Number of books:"))
bookID=map(int,input("\nEnter Integer Book ids seperated by \",\":").split(','))
p=map(float,input("\nEnter probabilities of successful searches seperated by \",\":").split(','))
q=map(float,input("\nEnter probabilities of unsuccessful searches seperated by \",\":").split(','))

def optimalBST(p1,q1,n):
    e=np.zeros((n+2,n+2))
    w=np.zeros((n+2,n+2))
    for i in range(1,n+2):
        e[i,i-1]=q1[i-1]
        w[i,i-1]=q1[i-1]
    for l in range(1,n+1):
        for i in range(1,n-l+2):
            j=i+l-1
            e[i,j]=float('inf')
            w[i,j]=w[i,j-1]+p1[j-1]+q1[j]
            for r in range(i,j+1):
                t=e[i,r-1]+e[r+1,j]+w[i,j]
                if t<e[i,j]:
                    e[i,j]=t
    return e[1,n]
try:
    result=optimalBST(list(p),list(q),n)
    print(f"\nThe expected cost of the Optimal Binary Search Tree is:{result:.4f}")
except ValueError as ve:
    bookID=list(bookID)
    if sorted(bookID)!=bookID:
        raise ValueError("Book IDs are not sorted. Please enter sorted Book IDs.")
    elif len(bookID)!=n or len(list(p))!=n or len(list(q))!=n+1:
        raise ValueError(f"Number of Book IDs is not {n}")

