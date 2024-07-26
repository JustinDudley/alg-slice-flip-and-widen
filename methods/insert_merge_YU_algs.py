from variables.constants import MERGE_YU_DICT

def insert_merge_YU_algs(one_ripple_round_of__final_algs):

    bfud_inserted__one_ripple_round_of__final_algs = []
    for alg in one_ripple_round_of__final_algs:
        bfud_inserted__one_ripple_round_of__final_algs.append(alg)
        for key, value in MERGE_YU_DICT.items():  
            if key in alg:                 # because don't want to append again if no change
                alg = alg + " "     # so that the search works even for turns that aren't counterclockwise or double
                alg = alg.replace(key, value)
                alg = alg.strip()
                bfud_inserted__one_ripple_round_of__final_algs.append(alg)



    return bfud_inserted__one_ripple_round_of__final_algs
