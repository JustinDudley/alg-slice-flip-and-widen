
# Note on TESTING: There are 3 lines of code that call testing methods.
# These methods simply add a few explanatory notes to the list of algs that will be written to file
# The methods are called TESTING_1, TESTING_2, TESTING_3.
# To add the notes:  Set is_test to TRUE in the file testing/is_test




def TESTING_1(ALL_ripple_rounds_from_single_SS__strTypeAlgs, strTypeAlg, listTypeAlg):
     ALL_ripple_rounds_from_single_SS__strTypeAlgs.extend(["\n\n\n\n\n\n", "original alg is:               %s\n"%(strTypeAlg), "alg after slice insertion is:  %s\n"%(" ".join(listTypeAlg))])
     
     return(ALL_ripple_rounds_from_single_SS__strTypeAlgs)




def TESTING_2(ALL_ripple_rounds_from_single_SS__strTypeAlgs, trailing_YorZ_Xs_dual, trailing_YorZ_Xs):
    ALL_ripple_rounds_from_single_SS__strTypeAlgs.extend(["\nDUAL list:  %s"%(trailing_YorZ_Xs_dual), "\nactive member of DUAL list:  %s"%(trailing_YorZ_Xs)  ])
    if trailing_YorZ_Xs[0] == "Y0" or trailing_YorZ_Xs[0] == "Z0":
        ALL_ripple_rounds_from_single_SS__strTypeAlgs.extend(["\nNote that the YorZ component is a Y0 or Z0 !!!"])

    return ALL_ripple_rounds_from_single_SS__strTypeAlgs




def TESTING_3(one_ripple_round_of__final_strTypeAlgs, indx, add_YorZ__shifting_listTypeAlg):
    one_ripple_round_of__final_strTypeAlgs = ["\nadd_YorZ__shifting_listTypeAlg  is now:\n" + " ".join(add_YorZ__shifting_listTypeAlg) + "\nThe indexes are going in reverse order; here are the algs for the current index, which is:  " + str(indx) + "\n"] + one_ripple_round_of__final_strTypeAlgs

    return one_ripple_round_of__final_strTypeAlgs
