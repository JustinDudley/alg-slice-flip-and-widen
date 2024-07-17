from variables.constants import MERGE_YU_DICT

def insert_merge_YU_algs(from_single_SS__rippled_and_expanded_strTypeAlgs):

    from_single_SS__final_strTypeAlgs = []
    for strTypeAlg in from_single_SS__rippled_and_expanded_strTypeAlgs:
        from_single_SS__final_strTypeAlgs.append(strTypeAlg)
        for key, value in MERGE_YU_DICT.items():   # because don't want to append again if no change
            if key in strTypeAlg:
                strTypeAlg = strTypeAlg + " "   #so that the search works even for turns that aren't counterclockwise or double
                strTypeAlg = strTypeAlg.replace(key, value)
                strTypeAlg = strTypeAlg.strip()
                from_single_SS__final_strTypeAlgs.append(strTypeAlg)

                


        # if "D' R'" in strTypeAlg:
        #     strTypeAlg = strTypeAlg + "moo baa lalala"
        # from_single_SS__final_strTypeAlgs.append(strTypeAlg)



    return from_single_SS__final_strTypeAlgs