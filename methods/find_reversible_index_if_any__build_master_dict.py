
from variables.constants import ITERATIVE_DELTA_SWAP_DICT



def find_reversible_index_if_any__build_master_dict(stic_turns, stic_alg_dict):

    # (1) Find string index and then figure out list index
    stic_alg_post_slice_insertion = " ".join(stic_turns) + " "
    post_slice_alg__index = 0
    stic_turns__index = 0
    stic_master_dict = {}

    tri_turns = list(ITERATIVE_DELTA_SWAP_DICT.keys())

    for tri_turn in tri_turns:
        index = stic_alg_post_slice_insertion.find(tri_turn)
        if index != -1:
            post_slice_alg__index = index
            break

    stic_turns__index = stic_alg_post_slice_insertion[:post_slice_alg__index + 1].count(" ") #the number of spaces in the string up until the tri-turn is equal to the index of the first of the tri-turn turns in the original algorithm (as expressed as a list named "xyz_turns")




    # (2) Build stic_master dictionary
    if stic_alg_dict["is_reversified"]:
        stic_master_dict = {"turns": stic_turns, "alg": stic_alg_dict["alg"], "is_reversified": True, "tri_turn_list_index": stic_turns__index}
    
    if not stic_alg_dict["is_reversified"]:
        stic_master_dict = {"turns": stic_turns, "alg": stic_alg_dict["alg"], "is_reversified": False, "tri_turn_list_index": -1}
    


    return stic_master_dict


