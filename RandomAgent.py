import STTT
import random

def get_move(state):
    print(state)
    valid_moves = STTT.get_valid_moves(state)
    print(valid_moves,len(valid_moves))
    moves_numbers = [x for x in range(81) if valid_moves[x]]
    print(moves_numbers)
    move_index = random.randint(0,len(moves_numbers)-1)
    move = moves_numbers[move_index]

    return move



