import math

class Solution:
    def minimumMoves(self, grid):
        n = len(grid)
        
        def illegal_move(snake):
            tail, head = snake[0], snake[1]
            if head[0] >= n or head[1] >= n:
                return True
            if grid[head[0]][head[1]] == 1 or grid[tail[0]][tail[1]] == 1:
                return True
            return False
        
        def moveRight(snake):
            tail, head = snake[0], snake[1]
            return ((tail[0],tail[1]+1), (head[0], head[1]+1))
        
        def moveDown(snake):
            tail, head = snake[0], snake[1]
            return ((tail[0]+1,tail[1]), (head[0]+1, head[1])) 
        
        def rotateClock(snake):
            tail, head = snake[0], snake[1]
            if tail[0] == head[0]:
                return (tail, (head[0]+1, head[1])) 
            else:
                return ((-1,-1), (-1,-1))
        
        def rotateAntiClock(snake):
            tail, head = snake[0], snake[1]
            if tail[1] == head[1]:
                return (tail, (head[0], head[1]+1)) 
            else:
                return ((-1,-1), (-1,-1))
        
        def costToReachGoal(snake, cost, goal):
            if snake == goal:
                return cost
            if illegal_move(snake):
                return float('inf')
            return min(costToReachGoal(moveRight(snake), cost+1, goal), costToReachGoal(moveDown(snake), cost+1, goal), costToReachGoal(rotateClock(snake), cost+1, goal), costToReachGoal(rotateAntiClock(snake), cost+1, goal))
    
        goal = ((n-1,n-2), (n-1,n-1))
        tail, head = (0,0), (0,1)
        snake = (tail, head)
        cost = costToReachGoal(snake, 0, goal)
        return -1 if math.isinf(cost) else cost
