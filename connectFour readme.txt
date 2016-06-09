****************************************
****************************************


CONNECT FOUR version 2 by Yu-Jin Tan (yjt21)


****************************************
****************************************

No cd/floppy disk/installation required and perfect for when friends are over.

----------------------------------------
Contents
----------------------------------------
1.1 Featured changes/fixes from previous versions
1.2 How to run ConnectFour
1.3 How to play ConnectFour
1.4 Saving and loading game.
1.5 Frequently Asked Questions (F.A.Qs)
1.6 Contact Me

----------------------------------------
1.1 Featured changes/fixes from previous versions
----------------------------------------
-Game now features a 2 player mode which is turn based and allows either player 1 or player 2 to win based upon 4 winning conditions.
-Player tokens were changed from 'X's' and 'O's' to '1' and '2' which I felt indicated easily who's token was just played.
-Player can now save and load a game.

----------------------------------------
1.2 How to run ConnectFour
----------------------------------------
-Within the same folder (ConnectFour-yjt21) as this README file, lies one other file, connectFour.py find this and run it with a python shell.
-To run it with python shell through lcpu, type in the bash command: python connectFour.py and the program should run.
-To run with a seperate python shell such as IDLE (a python GUI), look at the upper toolbar, click on file then click open... to look for connect four file. Once the file has been opened look at the upper toolbar again and click on Run and then Run Module. Alternatively you could just press F5.

----------------------------------------
1.3 How to play ConnectFour
----------------------------------------
-Find a friend to play with.
-Decide amoung you and your friend how tall you want the board.
-Decide amoung you and your friend how wide you want the board.
-A board should now be shown on you desired width and height, you can now start playing.

For example: 
I entered rows 6, columns 7 and I have this on my screen;

rows 6
columns 7
PLAYER 1 STARTS
at any point of the game press 's' to save or 'l' to load game.
0 0 0 0 0 0 0 
0 0 0 0 0 0 0 
0 0 0 0 0 0 0 
0 0 0 0 0 0 0 
0 0 0 0 0 0 0 
0 0 0 0 0 0 0 
play column: 


-Decide amoung you and your friend who be player 1, remember player 1 goes first which is always an advantage in winning.
-Take it in turns to enter column values(which are within the boards range) to enter tokens until a player has a four in a row.
-Some example winning conditions are:

A player 1 vertical win.

0 0 0 0 0 0 0 
0 0 0 0 0 0 0 
0 0 0 0 0 0 1 
0 0 0 0 0 2 1 
0 0 0 0 0 2 1 
0 0 0 0 0 2 1 

A player 1 horizontal win.

0 0 0 0 0 0 0 
0 0 0 0 0 0 0 
0 0 0 0 0 0 0 
0 0 0 0 0 0 0 
2 2 2 0 0 0 0 
1 1 1 1 0 0 0 

A player 2 horizontal win.

0 0 0 0 0 0 0 
0 0 0 0 0 0 0 
0 0 0 0 0 0 0 
0 0 0 1 1 0 0 
0 0 0 2 1 1 0 
0 0 2 2 2 2 1 


A player 1 south west to north east diagonal win.

0 0 0 0 0 0 0 
0 0 0 0 0 0 0 
2 0 0 1 0 0 0 
1 0 1 2 0 0 0 
1 1 2 1 0 0 0 
1 2 2 2 0 0 0 

A player 1 south east to north west diagonal win.

0 0 0 0 0 0 0 
0 0 0 0 0 0 0 
0 0 0 1 0 0 0 
0 0 0 1 1 2 0 
0 0 0 2 1 1 0 
0 0 0 2 2 2 1

when any a player has connected four, you'll be prompted by a line. "You won the game!" So who ever entered a column last wins the game!

----------------------------------------
1.4 Saving and loading game.
----------------------------------------

Short of time to complete a game? Well, you will be glad to know there's a save and load feature to complete your game with your friend another time.

-To save game and anytime, press 's' and it will save the game to a .txt file within the same directory as the game.
-To load that save game simply press 'l'.

----------------------------------------
1.5 Frequently Asked Questions (F.A.Qs)
----------------------------------------

Q. I have a board of 6 rows and 7 columns, I keep wanting to enter into column 9 but the game keeps closing and giving me "IndexError: list assignment index out of range" what am I doing wrong?

A. If you have specified your board to be of width x, you cannot enter token values in column x + 1, x + 2, x + n, where n is showing that the number could be huge. Fact is, it's not excepted.


----------------------------------------
1.6 Contact Me
----------------------------------------

If you have further enquiries about this game, email me at yjt21@bath.ac.uk