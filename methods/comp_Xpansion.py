import copy

from variables.constants import COMPLEMENT
from variables.dataframes import df_turn_attributes, df_Ripple_R


def comp_Xpansion(YorZ_added__shifting_turns, DNA_3_marker_cums):

    final_algs = []
    for DNA_3_marker_cum in DNA_3_marker_cums:
        final_turns = copy.deepcopy(YorZ_added__shifting_turns)
        for index, rotation in enumerate(DNA_3_marker_cum):
            if rotation == "*":
              final_turns[index] = df_turn_attributes.at[final_turns[index], COMPLEMENT]
            else:
                final_turns[index] = df_Ripple_R.at[final_turns[index], "%sA-->B%s"%(rotation, rotation)]
        
        final_alg = " ".join(final_turns)
        final_algs.append(final_alg)


    return(final_algs)
