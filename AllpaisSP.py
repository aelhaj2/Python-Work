
def allPairsSP( adjacencyMatrix , i ):
   n = len(adjacenyMatrix):
   for k in range(i):
    for u in range(n):
        for v in range(n):
            if adjacenyMatrix[u][k] == -1 or adjacenyMatrix[k]
[v] == -1:
continue 
if adjacenyMatrix[k][v]
    
    return adjacencyMatrix 


if __name__ == '__main__':
    n = int(input())
    adjacencyMatrix  = [[-1 for i in range(n)] for j in range(n)]
    
    i = int(input())
    x, y, z = input().split()
    x = int(x)
    y = int(y)
    z = int(z)
    
    # Enter negative # to beak out of the loop
    while 0<=x<n and 0<=y<n:
       adjacencyMatrix [x][y] = z
       adjacencyMatrix [y][x] = z
       x, y, z = input().split()   
       x = int(x)
       y = int(y)
       z = int(z)
    
    
    t = 0
    while t<n:
        adjacencyMatrix [t][t] = 0
        t+=1
        
    
    sp = allPairsSP( adjacencyMatrix  , i )
    
    for w in range(0,n):
        for v in range(0,n):
            print('{:.1f}'.format(sp[w][v]), end = ' ')
        print()
   
       