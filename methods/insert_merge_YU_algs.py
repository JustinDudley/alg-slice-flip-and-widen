from variables.constants import MERGE_YU_DICT

def insert_merge_YU_algs(one_ripple_round_of__final_strTypeAlgs):

    bfud_inserted__one_ripple_round_of__final_strTypeAlgs = []
    for strTypeAlg in one_ripple_round_of__final_strTypeAlgs:
        bfud_inserted__one_ripple_round_of__final_strTypeAlgs.append(strTypeAlg)
        for key, value in MERGE_YU_DICT.items():   # because don't want to append again if no change
            if key in strTypeAlg:
                strTypeAlg = strTypeAlg + " "   #so that the search works even for turns that aren't counterclockwise or double
                strTypeAlg = strTypeAlg.replace(key, value)
                strTypeAlg = strTypeAlg.strip()
                bfud_inserted__one_ripple_round_of__final_strTypeAlgs.append(strTypeAlg)



    return bfud_inserted__one_ripple_round_of__final_strTypeAlgs
