
from variables.constants import CODE


def get_single_turn_code(turn):
    if turn in CODE:
        return CODE[turn]   #  !!!   It is the rotation of the turns themselves, not of their complements, that determine how each subsequent turn in the rippling should be altered.
    else:
        return 0