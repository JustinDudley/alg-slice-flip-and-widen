
README   /   LIBRARY OF 17 NOTABLE TEST ALGS


*************
This branch is the code I used to get all 42 results lists that are in the Final Repo. But,
I figured out that some algs don't have their inverses. And it looks like a StickerSolve alg 
that contains "...R L..." or "...U D2..." or "...F' B..." (to give a few examples) has an interesting property:
When you reverse the two letters (which doesn't change the resulting scramble) it actually yields
new possibilities when put through alg-slice-and-widen.
So:  Now I am going to make a few adjustments to alg-slice-and-widen so that it does the necessary
reversal additions as it creates the 60,000 final algs
*************


THE WORK OUTLINED BELOW HAS ALREADY BEEN DONE.
IN FUTURE, THE WAY TO TEST THE CURRENT PROGRAM AGAINST A CORRECTLY WORKING VERSION IS:
  -- SET is_test TO True, PASTE THE ALGS FROM THE FILE "testing/TEST_SUITE_17__INPUT_Wed.txt" INTO THE FILE "alg_list_input.txt", RUN PROGRAM, COMPARE OUTPUT FILE TO THE FILE "testing/TEST_SUITE_17__OUTPUT_Wed__comments_included.txt" USING DIFFCHECKER ONLINE
  -- SET is_test TO False, PASTE THE ALGS FROM THE FILE "testing/TEST_SUITE_17__INPUT_Wed.txt" INTO THE FILE "alg_list_input.txt", RUN PROGRAM, COMPARE OUTPUT FILE TO THE FILE "testing/TEST_SUITE_17__OUTPUT_Wed.txt" USING DIFFCHECKER ONLINE





These 17 algs were carefully selected to represent the whole.
The algs belong to DIFFERENT GROUPS, so beware when running them through various projects:  They won't produce the same centers OR the same edges/corners as each other.
Currently, these algs and their results constitue the entirety of my testing suite.


How to use the 17 algs to test this programming:
Run the program, open the resultant output file

  # check VALIDITY with validate-alg-list project   --Does each alg induce the correct pattern on the cube?  [Algs belong to different groups, so must run them separately through validate-alg-list]
	# check for DUPLICATES   --Using google sheets or Excel, check for duplicates in result list (AFTER eliminating the Y0 symbol). Duplicates would indicate ive done something wrong logically.
	# check COMPLETENESS (painstaking)  --see the 17 algs below
      - check a corners alg that has a slice.
      - check algs that have 0, 1, 2 and 3 slices.
      - check the X0 case for proper inclusion of the non-comp base alg
      - check 2 algs with U D, F B2 type duos to make sure YorZ ripples through them correctly and doesn't create functionally identical duplicates.
      - check an alg that has zero results. 
      - check all 4 dual examples.  [ ONLY CHECKING 3. That's okay. ]
      - check an X and an X' for proper iteration. Basically just need to run them through Validation project.



CHECKS FOR COMPLETENESS
Each of the 17 algs below has verbiage explaining why it's on this list, and what to (painstakingly) check for when viewing the results.

1.
R2 D2 F B' R L2 F B' D' L2 U R L' B'
  -  Y0 X0 
  -  So this SS_alg only yields one final alg
  -  CHECK FOR COMPLETENESS:  itertools found everything?
  -  CHECK FOR COMPLETENESS:  Y0 causes itertools to stop after one round



2.
R U' D B' D2 F R L' U' F2 U2 R L' B2
   -  After slice sub, this is a Y0. Single round of itertools, yields appox. 10 solutions
    - CHECK FOR COMPLETENESS:  this alg has 3 slices. Make sure all 3 work
    - 2nd CHECK FOR COMPLETENESS:  Check itertools is complete



3.
U' L D' B2 D B' D' B2 U2 B' L F' B2 U' F' R' B
   -  typical corners alg. DOES include merge_YU
   -  CHECK FOR COMPLETENESS:  This alg has zero slices. Make sure it looks same after slice method
   -  CHECK FOR COMPLETENESS:  Check that merge_YU is complete



4.
U F B' R2 F B' D' R' B L' U' D F L' B D2
  -  Y0 X0
  - Include in Validate, to see if X0 iterates correctly. 
  - CHECK FOR COMPLETENESS:  See that Y0 causes the alg to do the iteration method just once and then stops



5.
U D2 F' B R F2 L' U D' B L2 F B R L' D2
  - Y0 X0
  - ZERO solutions
  -  CHECK FOR COMPLETENESS:  This alg supposedly has zero solutions. Is that right?
  - NO.  Turns out for ALL ALGS with an X0, I need to add the base alg to the list of finals for EACH ripple round.
  - These base algs were getting missed because the CompXpansion logic ONLY looks for comp solutions, whereas these algs are already perfect WITHOUT comps
  - Before the era of slice substitution, this problem never came up because there was no X0
  - Most of the algs this catches will be oddballs:  2 S's and a T; a Y2 and a T... But some of those are still good algs.


6.
L' D F B' U R L2 F L F' R F2 D F' B' L' D'
- CHECK FOR COMPLETENESS:  This a corner alg with a slice comp. Check the slice worked out okay



7.
U B' L' F' R U' D B' R F R F2 B' R L' U2
  - Z' X0
  - surprisingly small number of iteration on some rounds
  - CHECK FOR COMPLETENESS:  This alg has 2 slices. See that they both work
  - After slice substitution, the Z' will ripple past an S', which is cool
  - This is a great alg for checking the addition of base algs with an X0
  - CHECK FOR COMPLETENESS:  Include this in Validate project, make sure X0 iteration works. 



8.
F' B R' L' D R L B' U2 R2 F' U D L F2 U2 L F2
 - Y' X
    - CHECK FOR COMPLETENESS:  Check that Y' ripples through U D without making duplicates



9.
R' B2 D2 B2 R' D B' D F' B R' B L D2 R' L'
  - Y0 X2
  - just 2 iterations
  - CHECK FOR COMPLETENESS:  Include this in Validate project, make sure X2 iteration works. 



10.
B' U' L' D F B' U R L2 F L F' R F2 D F' B'
 - X' in WCR
 CHECK FOR COMPLETENESS:  Just need to include this in Validate project, to make sure X' iteration works. Don't need to test this alg for completeness



11.
U2 R2 L B R B' L B2 D F' B' R' D' F' U R' L D'
 - Make sure the method "insert_reinstated_trailing_YorZ__patch" works for Y
 Also:
 - X in WCR
 CHECK FOR COMPLETENESS:  Just need to include this in Validate project, to make sure X iteration works. Don't need to test this alg for completeness



12.
U2 F' L2 U2 F' R' L' U B2 L2 U R' L' F' R L
- CHECK FOR COMPLETENESS:  DUAL:  Y2 X, Z2 X'



13.
U D R L2 U' D' F U2 L2 B R' L' U D2 B2 R2 D' R2
- CHECK FOR COMPLETENESS:  DUAL:  Y2 X', Z2 X



14.
R L U D' F2 L2 F U D' L' B2 R F B' U D2
  - Y0 X0
  - many iterations for its one ripple round. Just run it through Validate, no need to check for completeness
  - include in validate, to check X0 is working for itertools



15.
R' L F2 D' L2 F2 D' R' L' F U2 L2 F R' L' D' L2
 - DUAL:   [['Y2', 'X0'], ['Z2', 'X2']]
 - Finally, an example of the OTHER type of dual !!
 - CHECK FOR COMPLETENESS:  DUAL:  Y2 X0, Z2 X2



16.
L2 F U2 L2 F U D L' B2 U2 L' U D F U' D'
 - Contains a U' D' at end, so the Y component should ripple TWICE before itertools does its work



 17.
 R2 D' F B R U' D' F B' D2 F L2 D2 F R L U' L2
  - Make sure the method "insert_reinstated_trailing_YorZ__patch" works for Z