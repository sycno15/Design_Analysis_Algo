import numpy as np
import math

# Calculating Distance between 2 places
def distance(lat1,lon1,lat2,lon2):
    return math.sqrt((lat2-lat1)**2+(lon2-lon1)**2)

locations ={
    "ZeroMile":(21.1500, 79.0882),
    "Sitabuldi":(21.1458, 79.0880),
    "Dharampeth":(21.1450, 79.0600),
    "Sadar":(21.1660, 79.0800),
    "CivilLines":(21.1540, 79.0710),
    "Ambazari":(21.1334, 79.0556),
    "Itwari":(21.1600, 79.1050),
}

li =list(locations.keys())
n =len(li)
INF =float('inf')

# Building cost matrix using distance formula
cost_matrix =np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i==j:
            cost_matrix[i][j]=0
        else:
            lat1,lon1 =locations[li[i]]
            lat2,lon2 =locations[li[j]]
            dist =distance(lat1,lon1,lat2,lon2)
            # Adding a traffic factor by multiplying distance with traffic factor to determine weights
            cost_matrix[i][j] =round(dist*np.random.uniform(1.0,1.2),4)

# Bellman-Ford Algorithm
def bellman_ford(cost, start):
    n=len(cost)
    distances=[INF]*n
    predecessors=[None]*n
    distances[start]=0

    for i in range(n-1):
        for u in range(n):
            for v in range(n):
                if cost[u][v]!=0 and distances[u]+cost[u][v]<distances[v]:
                    distances[v]=distances[u]+cost[u][v]
                    predecessors[v]=u

    return distances,predecessors

# Test Case: Starting from ZeroMile to Ambazari
start ="ZeroMile"
end ="Ambazari"

start_idx =li.index(start)
end_idx =li.index(end)

distances, predecessors =bellman_ford(cost_matrix, start_idx)

def shortest_path(predecessors, start, end):
    path =[]
    node =end
    while node is not None:
        path.append(node)
        node=predecessors[node]
    path.reverse()
    return path

path =shortest_path(predecessors,start_idx,end_idx)

print(f"\nShortest route from {start} to {end}:\n")
total =0
for i in range(len(path)-1):
    a,b =path[i], path[i+1]
    distance =cost_matrix[a][b]
    total +=distance
    print(f"{li[a]}->{li[b]}:{distance:.4f} Total Yet:{total:.4f}")
print(f"\nTotal shortest distance from {start} to {end}:{total:.4f}")