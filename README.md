# Chekio_Peons
Pawn game in Checkio
 You are given a set of square coordinates where we have placed white pawns. You should count how many pawns are safe.

Input: Placed pawns coordinates as a set of strings.

Output: The number of safe pawns as a integer.

Example:

safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1

How it is used: For a game AI one of the important tasks is the ability to estimate game state. This concept will show how you can do this on the simple chess figures positions.

Precondition:
0 < pawns ≤ 8
