
from variables.constants import WHAT_BRINGS_Q_HERE, SLICE_COMPS, ROTATION_VECTOR, COMPLEMENT, X_INVERSE
from variables.dataframes import df_Ripple_R, df_stickers_turned, df_turn_attributes


def ripple_right(turn, WCR):
	column = "%sA-->B%s"%(WCR, WCR)
	return df_Ripple_R.at[turn, column]


def move_sticker_once(sticker, WCR):
	return df_stickers_turned.at[sticker, WCR]


def replace_Trailing_WCRs_with_either_ONE_or_TWO_equivalent_YorZ_notations(WCRs):
	sticker = "Q"
	for WCR in WCRs:
		sticker = move_sticker_once(sticker, WCR)
	trailing_YorZ_Xs_dual = WHAT_BRINGS_Q_HERE[sticker]
	return trailing_YorZ_Xs_dual



# NEW METHOD FOR THIS BRANCH
# in the case where leading_X is  X',  we essentially add   X' X  to the beginning of the alg (which changes nothing), then ripple the second component, the X, right. It ripples through the alg, changing each turn one by one. The X ends up at the end of the alg, which is the same as ending up at the beginning of the trailing_WCRs (where it is therefore pre-pended)
def X_ripples_right(stic_turns, trailing_WCRs, leading_X):     # trailing_WCRs is, by this time, often just a long list of 4 or 5 WCRs

    for i in range(len(stic_turns)):   # alter every turn in the alg (doesn't affect trailing_WCRs)
        stic_turns[i] = ripple_right(stic_turns[i], X_INVERSE[leading_X])
    trailing_WCRs.insert(0, X_INVERSE[leading_X])   # pre-pend the inverse of leading_X to trailing_WCRs


    return[stic_turns, trailing_WCRs]




def sub_in_slices_and_ripple_right(stic_turns, trailing_WCRs, leading_X):
    slice_opportunity_positions = []
    for i in range(len(SLICE_COMPS)):
        for j in range(len(stic_turns)):
            if SLICE_COMPS[i] == stic_turns[j]:
                slice_opportunity_positions.append(j)

   

    if slice_opportunity_positions:  # returns True if a Python list is non-empty
        
        slice_opportunity_positions = sorted(set(slice_opportunity_positions), reverse=True)  # Reversed so that pre-pending the WCRs works.
        for position in slice_opportunity_positions:
            WCR_to_ripple_right = df_turn_attributes.at[stic_turns[position], ROTATION_VECTOR]
            stic_turns[position] = df_turn_attributes.at[stic_turns[position], COMPLEMENT]  # sub in the complement (a slice)
            
            for i in range(len(stic_turns)):
                if i > position:
                    stic_turns[i] = ripple_right(stic_turns[i], WCR_to_ripple_right)
            trailing_WCRs = [WCR_to_ripple_right] + trailing_WCRs




    # NEW FUNCTIONALITY FOR THIS BRANCH: ADDS AN X, X', OR X2  WCR AT BEGINNING OF ALG  
    # # note the destructuring notation
    stic_turns, trailing_WCRs = X_ripples_right(stic_turns, trailing_WCRs, leading_X)
    

    trailing_WCRs_dual:list[list[str]] = replace_Trailing_WCRs_with_either_ONE_or_TWO_equivalent_YorZ_notations(trailing_WCRs)

    return [stic_turns, trailing_WCRs_dual]