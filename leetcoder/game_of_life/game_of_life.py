
"""
@Schwinn Zhang

Game Rules (source: LeetCode, https://leetcode.com/problems/game-of-life/)
Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.


"""
def gameOfLife(board: list):
    """
    Do not return anything, modify board in-place instead
    Input should be a list that consists lists of integer 0 and 1
    """
    # check empty list 
    if not board or [] in board:
        return
    
    # check input type
    assert type(board) == list

    for sublist in board:
        assert type(sublist) == list
        for num in sublist:
            assert type(num) == int
            assert num == 1 or num == 0

    # first, set the borders of 2D world
    south_limit = len(board)
    east_limit = len(board[0])
    
    # function that returns the number of live neighbors of a cell
    def get_live_neighs(row, col):
        live_neighs = 0 
        #north
        if row - 1 >= 0 and board[row-1][col] == 1:
            live_neighs += 1            
        #south
        if row + 1 < south_limit and board[row+1][col] == 1:
            live_neighs += 1
        #west
        if col - 1 >= 0 and board[row][col-1] == 1:
            live_neighs += 1
        #east
        if col + 1 < east_limit and board[row][col+1] == 1:
            live_neighs += 1
        #northwest
        if row -1 >=0 and col -1 >=0 and board[row-1][col-1] == 1:
            live_neighs += 1
        #northeast
        if row -1 >=0 and col + 1 < east_limit and board[row-1][col+1] == 1:
            live_neighs += 1
        #southwest
        if row + 1 < south_limit and col - 1 >=0 and board[row+1][col-1] == 1:
            live_neighs += 1
        #southeast
        if row + 1 < south_limit and col + 1 < east_limit and board[row+1][col+1] == 1:
            live_neighs += 1
            
        return live_neighs
            
    # figure out next state for each cell and store in state_map
    state_map = {}
    for row in range(south_limit):
        for col in range(east_limit):
            cur_state = board[row][col]
            live_neighbors= get_live_neighs(row, col) 
            # dead -> live if 3 live neighbs
            if cur_state == 0:
                if live_neighbors == 3:
                    state_map[(row,col)] = 1
                else:
                    state_map[(row,col)] = 0
            # alive
            else:
                if live_neighbors == 2:
                    state_map[(row,col)] = 1
                elif live_neighbors == 3:
                    state_map[(row,col)] = 1
                else:
                    state_map[(row,col)] = 0
    
    # update state
    for key in state_map.keys():
        row, col = key
        new_state = state_map[key]
        board[row][col] = new_state


if __name__ == '__main__':
    # an easy test case
    board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    print('board in initial state:' + str(board))
    gameOfLife(board)
    print('board in new state: {}'.format(board))


