import copy

from variables.constants import COMPLEMENT
from variables.dataframes import df_turn_attributes, df_Ripple_R


def comp_Xpansion(add_YorZ__shifting_listTypeAlg, DNA_3_marker_cums):

    final_strTypeAlgs:list[str] = []
    for DNA_3_marker_cum in DNA_3_marker_cums:
        final_listTypeAlg = copy.deepcopy(add_YorZ__shifting_listTypeAlg)
        for index, rotation in enumerate(DNA_3_marker_cum):
            if rotation == "*":
              final_listTypeAlg[index] = df_turn_attributes.at[final_listTypeAlg[index], COMPLEMENT]
            else:
                final_listTypeAlg[index] = df_Ripple_R.at[final_listTypeAlg[index], "%sA-->B%s"%(rotation, rotation)]
        
        final_strTypeAlg = " ".join(final_listTypeAlg)
        final_strTypeAlgs.append(final_strTypeAlg)


    return(final_strTypeAlgs)

