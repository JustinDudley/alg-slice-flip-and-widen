
import pandas as pd 
from variables import *  


print("\n\ndf_basics:\n\n", df_basics, "\n")
print("\n\ndf_slice_comps:\n\n", df_slice_comps, "\n")
print("df_Ripple_R:\n\n", df_Ripple_L, "\n")
print("df_Ripple_L:\n\n", df_Ripple_R, "\n")

print("df_core:\n\n", df_core, "\n")
print("df_turns:\n\n", df_turns, "\n")
print("df_rotations:\n\n", df_rotations, "\n")
print("df_reflections:\n\n", df_reflections, "\n")


# Must choose a group before running program. (1-6)
group = 1
alg = "U R2 U D' F B L' B2 R U D' B R L' U2 B2"



# R L' -->  RL',  D U' --> U'D, etc.   This block replaces every instance of each substring in dict 
for key, value in slice_comp_dict.items():
	alg = alg.replace(key, value)
print("alg after replacements:\n", alg)

alg_list = alg.split()
print("\nalg_list is:", alg_list)

coro_scheme = group_dict[group]
coro_scheme_list = coro_scheme.split()
print(coro_scheme_list)

# alg_two_components:  [['U', 'R2', "UD'", 'F', 'B', "L'", 'B2', 'R', "UD'", 'B', "RL'", 'U2', 'B2'], ['X2', 'Y']]
alg_two_components = [alg_list, coro_scheme_list]

for turn in alg_two_components[0]:
      print(turn)
      # now replace slice comps with slices, and alter the remainder of the alg
      # will I be able to alter alg_two_components[0] directly?  It's a list within a list, which is tricky


