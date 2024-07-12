import copy

from variables.constants import COMPLEMENT
from variables.dataframes import df_turn_attributes, df_Ripple_R


def comp_Xpansion(alg_turns_shifting, DNA_3_marker_cums):

    final_alg_strings:list[str] = []
    for DNA_3_marker_cum in DNA_3_marker_cums:
        final_alg_turns = copy.deepcopy(alg_turns_shifting)
        for index, rotation in enumerate(DNA_3_marker_cum):
            if rotation == "*":
              final_alg_turns[index] = df_turn_attributes.at[final_alg_turns[index], COMPLEMENT]
            else:
                final_alg_turns[index] = df_Ripple_R.at[final_alg_turns[index], "%sA-->B%s"%(rotation, rotation)]
        
        final_alg_string = " ".join(final_alg_turns)
        final_alg_strings.append(final_alg_string)


    return(final_alg_strings)

