
from variables import df_Ripple_R, df_stickers_turned, df_complements_and_inverses, WHAT_BRINGS_Q_HERE, SLICE_COMPS  




def ripple_right(turn, WCR):
	column = "%sA-->B%s"%(WCR, WCR)
	return df_Ripple_R.at[turn, column]

def ripple_right_WCR_list(turn, WCR_list):
	for WCR in WCR_list:
		turn = ripple_right(turn, WCR)
	return turn




def move_sticker_once(sticker, WCR):
	## !!!  The line below used to say df_sticker_rotated. I changed it when I added Y0  and X0 as column names of df_sticker_rotated
	## !!!  Need to check that this still works!
	return df_stickers_turned.at[sticker, WCR]

def replace_Trailing_WCRs_with_up_to_TWO_equivalent_YorZ_notations(WCRs):
	sticker = "Q"
	for WCR in WCRs:
		sticker = move_sticker_once(sticker, WCR)
	trailing_WCRs_dual = WHAT_BRINGS_Q_HERE[sticker]
	return trailing_WCRs_dual



def sub_in_slices_and_ripple_right(alg_turns, trailing_WCRs):
    print("hi")



    slice_opportunity_positions = []
    for i in range(len(SLICE_COMPS)):
        for j in range(len(alg_turns)):
            if SLICE_COMPS[i] == alg_turns[j]:
                slice_opportunity_positions.append(j)

    slice_opportunity_positions = sorted(set(slice_opportunity_positions), reverse=True)  # Reversed so that pre-pending the WCRs works.
    print("\nslice opportunity positions: ", slice_opportunity_positions)
    # What happens if slice_opportunity_positions is empty?  Do I need to account for this?



    # Do I even need this IF statement??
    if slice_opportunity_positions:  # returns True if a Python list is non-empty
        for position in slice_opportunity_positions:
            WCR_to_ripple_right = df_complements_and_inverses.at[alg_turns[position], "rotation_direction"]
            alg_turns[position] = df_complements_and_inverses.at[alg_turns[position], "complement"]  # sub in the complement (a slice)
            for index, alg_turn in enumerate(alg_turns):
                if index > position:
                    alg_turns[index] = ripple_right(alg_turns[index], WCR_to_ripple_right)
            trailing_WCRs = [WCR_to_ripple_right] + trailing_WCRs



    print(trailing_WCRs)

    # list[list[str]]
    trailing_WCRs_dual = replace_Trailing_WCRs_with_up_to_TWO_equivalent_YorZ_notations(trailing_WCRs)


    return[alg_turns, trailing_WCRs_dual]