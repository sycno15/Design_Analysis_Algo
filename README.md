# Bellman-Ford Algorithm: Shortest Route Between Locations

## Description

This implementation of the **Bellman-Ford algorithm** calculates the shortest route between multiple locations, taking into account distance and a traffic factor.

The distance between two points is computed using the Euclidean distance formula:

```
distance = sqrt((lat2 - lat1)^2 + (lon2 - lon1)^2)
```

## Locations Used

* ZeroMile: (21.1500, 79.0882)
* Sitabuldi: (21.1458, 79.0880)
* Dharampeth: (21.1450, 79.0600)
* Sadar: (21.1660, 79.0800)
* CivilLines: (21.1540, 79.0710)
* Ambazari: (21.1334, 79.0556)
* Itwari: (21.1600, 79.1050)

## How It Works

1. **Distance Calculation:** Computes distances between each pair of locations.
2. **Traffic Factor:** Adds a random traffic multiplier (1.0–1.2) to simulate real-world conditions.
3. **Bellman-Ford Algorithm:** Calculates shortest distances from a starting point to all other locations.
4. **Path Construction:** Traces back the shortest path from start to destination.

## Usage

```bash
cd Bellman-Ford-Algo
python bellmanFord.py
```

## Example Output

```
Shortest route from ZeroMile to Ambazari:

ZeroMile->Sitabuldi:0.0044 Total Yet:0.0044
Sitabuldi->Dharampeth:0.0284 Total Yet:0.0328
Dharampeth->Ambazari:0.0212 Total Yet:0.0540

Total shortest distance from ZeroMile to Ambazari:0.0540
```

## Complexity

* **Time Complexity:** O(V^3) (due to nested loops over vertices)
* **Space Complexity:** O(V^2) (cost matrix)
