
import sys


n = 4
dist = [
    [0, 1, 1, 2],
    [1, 0, 3, 2],
    [1, 3, 0, 4],
    [2, 2, 4, 0]
]

def shortestPath(path, visited, currentLength=0):
    if(len(path) == n):
        return currentLength + dist[path[0]][path[-1]]
    ret = sys.maxsize
    
    for next in range(n):
        if visited[next]:
            continue
        
        here = path[-1]
        path.append(next)
        visited[next] = True
        
        cand = shortestPath(path, visited, currentLength + dist[here][next])
        
        ret = min(ret, cand)
        visited[next] = False
        path.pop()
        
    return ret

    
if __name__ == '__main__':
    short = shortestPath([0], [True, False, False, False])
    print(short)