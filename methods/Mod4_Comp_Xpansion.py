import copy

from variables.dataframes import df_complements_and_inverses, df_Ripple_R


def Mod4_Comp_Xpansion(alg_turns_shifting, trailing_YorZ_Xs, DNA_3_marker_cums):

    final_algs = []
    for DNA_3_marker_cum in DNA_3_marker_cums:
        final_alg_turns = copy.deepcopy(alg_turns_shifting)
        for index, rotation in enumerate(DNA_3_marker_cum):
            if rotation == "*":
              final_alg_turns[index] = df_complements_and_inverses.at[final_alg_turns[index], "complement"]
            else:
                final_alg_turns[index] = df_Ripple_R.at[final_alg_turns[index], "%sA-->B%s"%(rotation, rotation)]
        final_algs.append(final_alg_turns)


    return(final_algs)

