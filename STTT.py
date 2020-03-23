# make it modular andrew

# what does our state look like?
"""
state = {
        "board":[]#9x9
        "current_player":0; # player making a move
        "current_board":4; # the board we are playing on
}
"""

# from stack overflow: https://stackoverflow.com/questions/39922967/python-determine-tic-tac-toe-winner
def win_indexes():
    n = 3
    # Rows
    for r in range(n):
        yield [3*r+ c for c in range(n)]
    # Columns
    for c in range(n):
        yield [3*r+ c for r in range(n)]
    # Diagonal top left to bottom right
    yield [3*i+ i for i in range(n)]
    # Diagonal top right to bottom left
    yield [3*i+ (n - 1 - i) for i in range(n)]


def get_inital_state():
    board = [[-1 for b in range(9)] for a in range(9)] # all -1
    current_player = 0
    current_board = 0
    winners = [-1 for _ in range(9)]
    state = {
            "board":board, #9x9
            "current_player":current_player, # player making a move
            "current_board":current_board, # the board we are playing on
            "winners":winners # who has won each square
    }
    return state

def get_winner(tictactoe_board):
    # check for the possible winning positions
    for indexes in win_indexes():
        if( all(tictactoe_board[i] == 0 for i in indexes)):
            return 0
        if( all(tictactoe_board[i] == 1 for i in indexes)):
            return 1
    return -1

def move_is_valid(state,action):
    action_board = action // 9
    action_pos = action %9

    if(current_board == -1):
        # check if the spot is open
        if(state['winners'][action_board] != -1):
            return 0
        if(state['board'][action_board][action_pos] != -1):
            return 0
        return 1

    if(state['current_board'] != action_board):
        return 0
    if(state['board'][current_board][action_pos] != -1):
        return 0
    return 1
    

# return a mask of valid moves
def get_valid_moves(state):
    return [1 for x in range(81) if move_is_valid(state,x)]
    

def next_state(state,action):
    # assume action is a number 0-80
    # for the position of the 
    action_board = action // 9
    action_pos = action %9
    # put a x or o in the position designated by action
    current_board = state['current_board']
    current_player = state['current_player']
    if(not move_is_valid(state,action)):
        return -1

    
    # assume the move is valid
    state['board'][current_board][action_pos] = current_player

    # check if we won this board
    if(get_winner(state['board'][action_board]) != -1):
        # we won update winners
        state['winners'][action_board] = state['current_player']
    
    state['current_player'] = (current_player + 1 )% 2
    # if we are sending to a board that is won
    # then the other player gets to choose the next board to play on
    if(state['winners'][action_board] != -1):
        state['current_board'] = -1
    else:
        state['current_board'] = action
    return state

# agents will decide how to make actions
def pretty_print_board(board,selected):
    # switch out the board things
    character_map = {
            -1 : "  ",
            0: " X",
            1: " O"
    }
    board = [character_map[x] for x in board]
    print(board)
    result_string = []
    print("pretty board:",board)
    # regular tictactoe printout
    # put a line of buffer around the board
    # print out top row
    if(selected):
        result_string.append("~"*14)
    else:
        result_string.append(" "*14)
    result_string.append(" %s | %s | %s "%(board[0],board[1],board[2]))
    result_string.append("-"*14)
    result_string.append(" %s | %s | %s "%(board[3],board[4],board[5]))
    result_string.append("-"*14)
    result_string.append(" %s | %s | %s "%(board[6],board[7],board[8]))
    if(selected):
        result_string.append("~"*14)
    else:
        result_string.append(" "*14)
    return result_string

def pretty_print(state):
    all_boards = [pretty_print_board(state['board'][i],i==state['current_board']) for i in range(9)]

    # stitch the first coulple together
    print(" "*50)
    for i in range(7):
        print(all_boards[0][i] + " || " + all_boards[1][i] + " || " + all_boards[2][i])
    print("="*50)
    for i in range(7):
        print(all_boards[3][i] + " || " + all_boards[4][i] + " || " + all_boards[5][i])
    print("="*50)
    for i in range(7):
        print(all_boards[6][i] + " || " + all_boards[7][i] + " || " + all_boards[8][i])
