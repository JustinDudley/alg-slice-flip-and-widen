
from variables.constants import GET_CODE_FROM_TURN


def get_single_turn_code(turn):
    if turn in GET_CODE_FROM_TURN:
        return GET_CODE_FROM_TURN[turn]   #  !!!   It is the rotation of the turns themselves, not of their complements, that determine how each subsequent turn in the rippling should be altered.
    else:
        return 0