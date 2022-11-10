## Steepest-Ascent Hill Climbing
The dart board is filled with 12 sectors and each sector can perform 4 operations, rotate clockwise, rotate anticlockwise, shift down (till center). Given an *intital state* (Fig A), we need to design an effective heuristic approach using **Steepest Ascent Hill Climbing Algorithm** to reach *Goal State*.  (Fig B).  This [file](https://github.com/Abhi-2809/AI-Assignment-Bits-Hyderabad-/blob/main/AI_Assignment_1(Q2)/AI_Assignment_1(Q2).ipynb) contains the code for the given problem. You can run the notebook on jupyter or colab to execute the code.

Further Notes:
1. While performing the jump operation (shift down), the numbers will be swapped. For example
in FIG A, if 4 jumps to 9, the values in these positions will be swapped
2. For your convenience the first two steps are as below:
a. JUMP(4) : will result in swapping 4 with 9
b. C_ROTATE(9): will rotate the sector containing 9 by one step in clockwise direction.
c. A_ROTATE(9): will rotate the sector containing 9 by one step in anticlockwise
3. It is possible that the input combination may not end up in the goal state also. This should be reflected in the output
4. If the combination exists for the given input, the sequence of steps need to be printed.



![Screenshot 2022-11-09 at 10 31 01 PM](https://user-images.githubusercontent.com/68343079/200857887-ca6b6823-c3aa-4653-98e6-ab4dabf33b1d.png)
