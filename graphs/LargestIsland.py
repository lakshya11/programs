
def is_safe(row_index,col_index,n,m,visited,grid):
    if(row_index >=0 and col_index >=0and row_index<n and col_index< m and visited[row_index][col_index]==0 and grid[row_index][col_index]==1 ):
        return True
    return False

def dfs(grid,i,j,n,m,visited,count):
    # print "original i,j ",i,j
    visited[i][j] = 1
    # print "after setting visited ",visited
    # print "visited[1][1]", visited[1][1]
    count+=1
    neighbor_row = [-1,-1,-1,0,0,1,1,1]
    neighbor_col = [-1,0,1,-1,1,-1,0,1]
    for k in xrange(8):
        if is_safe(i+neighbor_row[k],j+neighbor_col[k],n,m,visited,grid):
            # print "calling dfs for ",i+neighbor_row[k],j+neighbor_col[k]
            # print "before calling visited ",visited
            count = dfs(grid,i+neighbor_row[k],j+neighbor_col[k],n,m,visited,count)
            # print "dfs count",count
    return count


def get_biggest_region(grid,n,m):

    result = 0
    visited = [[0 for j in range(m)]for i in range(n)]
    for i in xrange(n):
        for j in xrange(m):
            if grid[i][j]==1 and visited[i][j] ==0:
                count=0
                count = dfs(grid,i,j,n,m,visited,count)
                # print "main count",count
                if count > result:
                    result =count
    return result


n = int(raw_input().strip())
m = int(raw_input().strip())
grid = []
for grid_i in xrange(n):
    grid_temp = map(int, raw_input().strip().split(' '))
    grid.append(grid_temp)
# grid = [
#   [1,1,0,0],
#     [0,1,1,0],
#     [0,0,1,0],
#     [1,0,0,0]
# ]
# n =4
# m =4
print get_biggest_region(grid,n,m)
