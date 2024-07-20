

def TESTING_1(ALL_ripple_rounds_from_single_SS__strTypeAlgs, trailing_YorZ_Xs_dual, trailing_YorZ_Xs):
    
    ALL_ripple_rounds_from_single_SS__strTypeAlgs.extend(["\nDUAL list:  %s"%(trailing_YorZ_Xs_dual), "\nactive member of DUAL list:  %s"%(trailing_YorZ_Xs)  ])
    if trailing_YorZ_Xs[0] == "Y0" or trailing_YorZ_Xs[0] == "Z0":
        ALL_ripple_rounds_from_single_SS__strTypeAlgs.extend(["\nNote that the YorZ component is a Y0 or Z0 !!!"])


    return ALL_ripple_rounds_from_single_SS__strTypeAlgs



def TESTING_2(one_ripple_round_of__final_strTypeAlgs, indx):
    
    one_ripple_round_of__final_strTypeAlgs = ["\nGoing in reverse order, these are the algs for index:", " " + str(indx)] + one_ripple_round_of__final_strTypeAlgs


    return one_ripple_round_of__final_strTypeAlgs



