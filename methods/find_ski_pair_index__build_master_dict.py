
from variables.constants import SKI_PAIRS


def find_ski_pair_index__build_master_dict(stic_turns, stic_alg_dict):

    # Find string index, then figure out list index
    stic_alg_post_slice_insertion = " ".join(stic_turns) + " "
    post_slice_alg__index = 0
    stic_turns__index = 0
    stic_master_dict = {}

    for ski_pair in SKI_PAIRS:
        index = stic_alg_post_slice_insertion.find(ski_pair)
        if index != -1:
            post_slice_alg__index = index
            break
    stic_turns__index = stic_alg_post_slice_insertion[:post_slice_alg__index + 1].count(" ") # the number of spaces in the string up until the ski_pair is equal to the index of the first of the ski_pair turns in the original algorithm (as expressed as a list named "xyz_turns")



    # Build stic_master dictionary
    stic_master_dict = {"turns": stic_turns, "alg": stic_alg_dict["alg"], "has_exactly_one_ski_pair": True, "ski_pair_list_index": stic_turns__index}


    return stic_master_dict


