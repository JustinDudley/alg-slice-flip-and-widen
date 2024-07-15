
def add_collapsified_algs(from_single_SS__rippled_and_expanded_strTypeAlgs):

    from_single_SS__final_strTypeAlgs = []
    for strTypeAlg in from_single_SS__rippled_and_expanded_strTypeAlgs:
        from_single_SS__final_strTypeAlgs.append(strTypeAlg)
        if "R' D" in strTypeAlg:
            strTypeAlg = strTypeAlg + "moo baa lalala"
        from_single_SS__final_strTypeAlgs.append(strTypeAlg)



    return from_single_SS__final_strTypeAlgs