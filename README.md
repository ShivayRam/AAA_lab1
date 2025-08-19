Advanced Analysis of Algorithms
Lab 1: Uninformed Search
1 Introduction
In this lab, we’ll be implementing breadth-first search on the 8-puzzle problem.
Due Date: 18 August 2025
2 8-Puzzle
The 8-Puzzle is a game in which a player is required to slide tiles around on a 3 × 3 grid
in order to reach a goal configuration. If you have never played before, I recommend trying
it out here: http://www.artbylogic.com/puzzles/numSlider/numberShuffle.htm?rows=3&
cols=3&sqr=1.
There is one empty space that an adjacent tile can be slid into. An alternative (and simpler)
view is that we are simply moving the blank square around the grid. Note that not all actions
can be used at all times. For example, the blank tile cannot be shifted up if it is already on the
top row!


Submission 1: Implementing moves (10 marks)
The first step is to implement action dynamics for a given game state. Write a Python or Java
program that takes in an initial configuration and an action, and outputs the resulting configuration and the associated cost.
Input
Input consists of two lines. The first line is a single string of digits and the hash symbol. The
position of the digit in the string is its location on the board, starting from top-left and moving
to bottom right. The hash represents the blank space. For example, the board configuration
given in Figure 1(a) would be represented by the string 1857#3462. The second line is the
action taken, which is one of either UP, DOWN, LEFT or RIGHT.
Output
The output should be formatted as a single string of digits and the hash symbol. The position of
the digits in the string is its location on the board, starting from top-left and moving to bottom
right. The hash represents the blank space.
Example Input-Output Pairs
Sample Input #1
1857#3462
LEFT
Sample Output #1
185#73462
Sample Input #2
18573#462
UP
Sample Output #2
18#735462
Sample Input #3
78651#432
DOWN
Sample Output #3
78651243#


Submission 2: Implementing available actions (10 marks)
The next step is to determine which actions are available in which states. Write a Python or
Java program that takes in an initial configuration, and outputs which actions are available at
the given state.
Input
Input consists of a single string of digits and the hash symbol. The position of the digit in the
string is its location on the board, starting from top-left and moving to bottom right. The hash
represents the blank space. For example, the board configuration given in Figure 1(a) would be
represented by the string 1857#3462.
Output
Output the list of available actions, each on their own line. The actions should be output in the
order UP, DOWN, LEFT, RIGHT.
Example Input-Output Pairs
Sample Input #1
1857#3462
Sample Output #1
UP
DOWN
LEFT
RIGHT
Sample Input #2
18573#462
Sample Output #2
UP
DOWN
LEFT
Sample Input #3
78651432#
Sample Output #3
UP
LEFT


Submission 3: Breadth-first search (40 marks)
Now that we’ve implemented the problem, we can now implement our search strategies. First,
write a Python or Java program that accepts an initial and goal state, and returns the cost of
the shortest path between the two, given that every action has a cost of 1.
Input
Input consists of two lines. The first line is a representation of the initial state, and the second
line is the goal state.
Output
Output the cost of the optimal plan from the start to the goal state.
Example Input-Output Pairs
Sample Input #1
78651#432
12345678#
Sample Output #1
25
Sample Input #2
1857#3462
185#73462
Sample Output #2
1
Sample Input #3
1857#3462
78651432#
Sample Output #3
20
