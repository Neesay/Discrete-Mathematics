import sys
from heapq import heapify, heappush, heappop

def dijsktra(graph,src,dest):
    inf = sys.maxsize
    node_data = {'A':{'cost':inf,'pred':[]},
                 'B':{'cost':inf,'pred':[]},
                 'C':{'cost':inf,'pred':[]},
                 'D':{'cost':inf,'pred':[]},
                 'E':{'cost':inf,'pred':[]},
                 'F':{'cost':inf,'pred':[]},
                 'G':{'cost':inf,'pred':[]},
                 'H':{'cost':inf,'pred':[]},
                 'I':{'cost':inf,'pred':[]},
                 'J':{'cost':inf,'pred':[]},
                 }
    node_data[src]['cost'] = 0
    visited = []
    temp = src
    for i in range(9):
        if temp not in visited:
            visited.append(temp)
            min_heap = []
            for j in graph[temp]:
                if j not in visited:
                    cost = node_data[temp]['cost'] + graph[temp][j]
                    if cost < node_data[j]['cost']:
                        node_data[j]['cost'] = cost
                        node_data[j]['pred'] = node_data[temp]['pred'] + list(temp)
                    heappush(min_heap,(node_data[j]['cost'],j))
                heapify(min_heap)
                temp = min_heap[0][1]
    print("Shortest Distance: " + str(node_data[dest]['cost']))
    print("Shortest Path: " + str(node_data[dest]['pred'] + list(dest)))
                            


if __name__ == "__main__":
    graph = {
        'A':{'B':3,'I':12},
        'B':{'A':3,'C':5},
        'C':{'B':5,'D':14,'E':6},
        'D':{'A':25,'C':14,'E':7},
        'E':{'C':6,'D':7,'F':8,'G':16},
        'F':{'E':8,'G':9,'I':7},
        'G':{'E':16,'F':9,'H':11},
        'H':{'G':11,'J':23},
        'I':{'A':12,'F':7,'J':10},
        'J':{'I':10,'H':23}
    }

    source = 'A'
    destination = 'H'
    dijsktra(graph,source,destination)
    


