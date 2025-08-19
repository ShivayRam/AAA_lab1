#deque seems like a good choice for BFS from all the examples ive seen online
from collections import deque

#function to swap positions in the string
def swap_pos(state, i, j):

    state = list(state)
    state[i], state[j] = state[j], state[i]
    
    return ''.join(state)


#function to get all possible moves from the current state
def get_moves(state):

    i = state.index('#')

    neighbors = []

    #movement directs

    #up
    if i >= 3:
        neighbors.append(swap_pos(state, i, i - 3))

    #down
    if i <= 5:
        neighbors.append(swap_pos(state, i, i + 3))

    #left
    if i % 3 != 0:
        neighbors.append(swap_pos(state, i, i - 1))

    #right
    if i % 3 != 2:
        neighbors.append(swap_pos(state, i, i + 1))

    return neighbors

def shortest_path(start, goal):

    #if we are already at the goal then return 0, duhh
    if start == goal:
        return 0
    
    #queue for bfs plus dict to keep track of visitedf states and their depth
    q = deque([start])

    visited = {start: 0}

    while q:

        curr = q.popleft()

        steps = visited[curr]


        for nxtState in get_moves(curr):

            if nxtState not in visited:

                visited[nxtState] = steps + 1
                if nxtState == goal:

                    return visited[nxtState]
                
                q.append(nxtState)

    #if we dont reach goal
    return -1


#now we can test the functions

if __name__ == "__main__":

    startState = input().strip()
    goalState = input().strip()

    res = shortest_path(startState, goalState)

    print(res)