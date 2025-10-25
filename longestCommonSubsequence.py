#Taking different strings as input
X="AGCCCTAAGGGCTACCTAGCTT"
Y="GACAGCCTACAAGCGTTAGCTTG"

#creating and printing the dynamic programming matrix
def createAndPrintMatrix(s1,s2):
    x=len(s1)+1
    y=len(s2)+1
    cost=[[0 for _ in range(y)]for _ in range(x)]
    direction=[['' for _ in range(y)]for _ in range(x)]
    for i in range(x):
        cost[i][0]=0
        direction[i][0]='H'
    for i in range(y):
        cost[0][i]=0
        direction[0][i]='H'
    for i in range(1,x):
        for j in range(1,y):
            if s1[i-1]==s2[j-1]:
                cost[i][j]=cost[i-1][j-1]+1
                direction[i][j]='D'
            elif cost[i-1][j]>cost[i][j-1]:
                cost[i][j]=cost[i-1][j]
                direction[i][j]='U'
            else:
                cost[i][j]=cost[i][j-1]
                direction[i][j]='L'
    for i in range(x):
        for j in range(y):
            print(f"{cost[i][j]}{direction[i][j]}",end=' ')
        print("\n")
            
    return cost,direction

#printing the longest common subsequence
def printSubstring(s1,s2,c1,d1):
    i=len(s1)
    j=len(s2)
    s=''
    print("Length Of Substring:",c1[i][j])
    while(d1[i][j]!='H'):
        if d1[i][j]=='U':
            i-=1
        elif d1[i][j]=='L':
            j-=1
        else:
            s+=s1[i-1]
            i-=1
            j-=1
    print("LCS:",s[::-1])

c1,d1=createAndPrintMatrix(X,Y)

printSubstring(X,Y,c1,d1)