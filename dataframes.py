import pandas as pd 

df_complements_and_inverses = pd.read_csv('/Users/justindudley/dev/cube/Alg_Slice_And_Widen_daddy/alg-slice-and-widen/tables/complements_and_inverses.csv', index_col="orig")
df_Ripple_L = pd.read_csv('/Users/justindudley/dev/cube/Alg_Slice_And_Widen_daddy/alg-slice-and-widen/tables/WCR_Ripples_Left.csv', index_col="orig") 
df_Ripple_R = pd.read_csv('/Users/justindudley/dev/cube/Alg_Slice_And_Widen_daddy/alg-slice-and-widen/tables/WCR_Ripples_Right.csv', index_col="orig") 
df_comp_rotation_nums = pd.read_csv('/Users/justindudley/dev/cube/Alg_Slice_And_Widen_daddy/alg-slice-and-widen/tables/comp_rotation_nums.csv', index_col="X") 

df_stickers_turned = pd.read_csv('/Users/justindudley/dev/cube/Alg_Slice_And_Widen_daddy/alg-slice-and-widen/tables/stickers_turned_by_alg_notation.csv', index_col="orig") 
df_stickers_rotated = pd.read_csv('/Users/justindudley/dev/cube/Alg_Slice_And_Widen_daddy/alg-slice-and-widen/tables/stickers_rotated_24.csv', index_col="orig") 
df_stickers_reflected = pd.read_csv('/Users/justindudley/dev/cube/Alg_Slice_And_Widen_daddy/alg-slice-and-widen/tables/stickers_reflected_24.csv', index_col="orig")




# print("\n\ndf_complements_and_inverses:\n\n", df_complements_and_inverses, "\n")
# print("df_Ripple_R:\n\n", df_Ripple_L, "\n")
# print("df_Ripple_L:\n\n", df_Ripple_R, "\n")
# print("comp_rotation_nums:\n\n", df_comp_rotation_nums, "\n")


# print("df_stickers_turned:\n\n", df_stickers_turned, "\n")
# print("df_stickers_rotated:\n\n", df_stickers_rotated, "\n")
# print("df_stickers_reflected:\n\n", df_stickers_reflected, "\n")