
# The 3x3 cube has 3 "KINGDOMS" or "orbits":   Center pieces, Corner pieces, Edge pieces
# In most but not all solving systems, the centers are presumed to be fixed and do not constitute an orbit

from variables.constants import STICKERS_SITTING_IN_CORNER_POSITIONS_ABCDUVWX__GROUP_1
from variables.constants import STICKERS_SITTING_IN_CORNER_POSITIONS_ABCDUVWX__GROUP_2
from variables.constants import STICKERS_SITTING_IN_CORNER_POSITIONS_ABCDUVWX__GROUP_3
from variables.constants import STICKERS_SITTING_IN_CORNER_POSITIONS_ABCDUVWX__GROUP_4
from variables.constants import STICKERS_SITTING_IN_CORNER_POSITIONS_ABCDUVWX__GROUP_5
from variables.constants import STICKERS_SITTING_IN_CORNER_POSITIONS_ABCDUVWX__GROUP_6



def find_group_and_kingdom(pattern):

    group_number = -1
    isCornerAlg = False
    stickers_sitting_in_corner_positions_ABCDUVWX = pattern[6:10] + pattern[26:30]  # indexes of positions A,B,C,D and of U,V,W,X



    # check for Group 1
    for sticker in stickers_sitting_in_corner_positions_ABCDUVWX:
        count = 0
        for i in range(8):
            if stickers_sitting_in_corner_positions_ABCDUVWX[i] == STICKERS_SITTING_IN_CORNER_POSITIONS_ABCDUVWX__GROUP_1[i]:
                count += 1

        if count == 8:
            group_number = 1       # All 8 corner stickers are in group 1 pattern
            isCornerAlg = False    # None have been swapped
        if count == 6:
            group_number = 1       # Sufficient number of corner stickers to guarantee group 1 pattern
            isCornerAlg = True     # Two are out of place and must have been swapped with each other



    # check for Group 2
    for sticker in stickers_sitting_in_corner_positions_ABCDUVWX:
        count = 0
        for i in range(8):
            if stickers_sitting_in_corner_positions_ABCDUVWX[i] == STICKERS_SITTING_IN_CORNER_POSITIONS_ABCDUVWX__GROUP_2[i]:
                count += 1

        if count == 8:
            group_number = 2       # All 8 corner stickers are in group 2 pattern
            isCornerAlg = False    # None have been swapped
        if count == 6:
            group_number = 2       # Sufficient number of corner stickers to guarantee group 2 pattern
            isCornerAlg = True     # Two are out of place and must have been swapped with each other



    # check for Group 3
    for sticker in stickers_sitting_in_corner_positions_ABCDUVWX:
        count = 0
        for i in range(8):
            if stickers_sitting_in_corner_positions_ABCDUVWX[i] == STICKERS_SITTING_IN_CORNER_POSITIONS_ABCDUVWX__GROUP_3[i]:
                count += 1

        if count == 8:
            group_number = 3       # see above
            isCornerAlg = False    # see above
        if count == 6:
            group_number = 3       # see above
            isCornerAlg = True     # see above



    # check for Group 4
    for sticker in stickers_sitting_in_corner_positions_ABCDUVWX:
        count = 0
        for i in range(8):
            if stickers_sitting_in_corner_positions_ABCDUVWX[i] == STICKERS_SITTING_IN_CORNER_POSITIONS_ABCDUVWX__GROUP_4[i]:
                count += 1

        if count == 8:
            group_number = 4      
            isCornerAlg = False    
        if count == 6:
            group_number = 4    
            isCornerAlg = True   



    # check for Group 5
    for sticker in stickers_sitting_in_corner_positions_ABCDUVWX:
        count = 0
        for i in range(8):
            if stickers_sitting_in_corner_positions_ABCDUVWX[i] == STICKERS_SITTING_IN_CORNER_POSITIONS_ABCDUVWX__GROUP_5[i]:
                count += 1

        if count == 8:
            group_number = 5    
            isCornerAlg = False   
        if count == 6:
            group_number = 5    
            isCornerAlg = True   



    # check for Group 6
    for sticker in stickers_sitting_in_corner_positions_ABCDUVWX:
        count = 0
        for i in range(8):
            if stickers_sitting_in_corner_positions_ABCDUVWX[i] == STICKERS_SITTING_IN_CORNER_POSITIONS_ABCDUVWX__GROUP_6[i]:
                count += 1

        if count == 8:
            group_number = 6   
            isCornerAlg = False  
        if count == 6:
            group_number = 6   
            isCornerAlg = True    




    return [group_number, isCornerAlg]
