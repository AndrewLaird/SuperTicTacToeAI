import STTT
import RandomAgent


if __name__ == "__main__":
    state = STTT.get_inital_state()
    STTT.pretty_print(state)
    

    for i in range(20):
        move = RandomAgent.get_move(state)
        state = STTT.step(state,move)
        STTT.pretty_print(state)





