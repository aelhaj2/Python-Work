def maximumST( matrix):
   n = len(matrix)
   in_mst = [False] * n
   key = [-1] * n
   key[0] = 0 

   for _ in range(n - 1): 
      max_key = -1
      max_index = -1
      for v in range(n):
         if not in_mst[v] and key[v] > max_key:
            max_key = key[v]
            max_index = v

            in_mst[max-index] = True 

            for v in range(n):
               if matrix[max_index][v] > 0 and not in_mst[v] amd key[v] < matrix[max_index][v]:
                  key[v] = matrix[max_index]

                  return sum(key) 

    return 42.0


if __name__ == '__main__':
    n = int(input())
    matrix = [[0 for i in range(n)] for j in range(n)]
    x, y, z = input().split()
    x = int(x)
    y = int(y)
    
    # Enter negative # to beak out of the loop
    while 0<=x<n and 0<=y<n:
       matrix[x][y] = float(z)
       matrix[y][x] = float(z)
       x, y, z = input().split()   
       x = int(x)
       y = int(y)

    print(matrix)
    print("The value of the maximum spanning tree is {:.1f}" .format(maximumST( matrix )) )

       