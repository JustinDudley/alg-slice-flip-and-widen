
from variables.constants import WHAT_BRINGS_Q_HERE, SLICE_COMPS, ROTATION_VECTOR, COMPLEMENT
from variables.dataframes import df_Ripple_R, df_stickers_turned, df_turn_attributes


def ripple_right(turn, WCR):
	column = "%sA-->B%s"%(WCR, WCR)
	return df_Ripple_R.at[turn, column]

def ripple_right_WCR_list(turn, WCR_list):
	for WCR in WCR_list:
		turn = ripple_right(turn, WCR)
	return turn



def move_sticker_once(sticker, WCR):
	return df_stickers_turned.at[sticker, WCR]

def replace_Trailing_WCRs_with_either_ONE_or_TWO_equivalent_YorZ_notations(WCRs):
	sticker = "Q"
	for WCR in WCRs:
		sticker = move_sticker_once(sticker, WCR)
	trailing_YorZ_Xs_dual = WHAT_BRINGS_Q_HERE[sticker]
	return trailing_YorZ_Xs_dual



def sub_in_slices_and_ripple_right(listTypeAlg, trailing_WCRs):
    print("NOW INSIDE sub_in_slices_and_ripple_right")
    slice_opportunity_positions = []
    for i in range(len(SLICE_COMPS)):
        for j in range(len(listTypeAlg)):
            if SLICE_COMPS[i] == listTypeAlg[j]:
                slice_opportunity_positions.append(j)

   

    if slice_opportunity_positions:  # returns True if a Python list is non-empty
        
        slice_opportunity_positions = sorted(set(slice_opportunity_positions), reverse=True)  # Reversed so that pre-pending the WCRs works.
        print("\nslice opportunity positions, one list per SS_alg: ", slice_opportunity_positions)
        for position in slice_opportunity_positions:
            WCR_to_ripple_right = df_turn_attributes.at[listTypeAlg[position], ROTATION_VECTOR]
            listTypeAlg[position] = df_turn_attributes.at[listTypeAlg[position], COMPLEMENT]  # sub in the complement (a slice)
            
            # for i, alg_turn in enumerate(listTypeAlg):  ## changed code to below, on 7/13
            for i in range(len(listTypeAlg)):
                if i > position:
                    listTypeAlg[i] = ripple_right(listTypeAlg[i], WCR_to_ripple_right)
            trailing_WCRs = [WCR_to_ripple_right] + trailing_WCRs


    # list[list[str]]
    trailing_WCRs_dual = replace_Trailing_WCRs_with_either_ONE_or_TWO_equivalent_YorZ_notations(trailing_WCRs)

    return[listTypeAlg, trailing_WCRs_dual]