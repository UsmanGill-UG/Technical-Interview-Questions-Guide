# MYSTERIOUS DATA STRUCTURE

In an ancient book of Mysterious Algorithms, there is a mention of such a data structure that has unpredictable behavior for each of its instances. This data structure, in its simplest form, has two operations: push and pop. push takes an integer as a parameter and puts it into a data structure. pop, on the other hand. takes out an element.

It is possible to guess the behavior of this data structure by performing a sequence of push and pop operations. It can behave like a stack, a queue, a priority queue (larger first) or something that we don’t know in this modern world. Your task is to write a program that will determine the data structure when given a sequence of operations.

Input Format
Input will be read from the file. The first line of input will begin with an integer O, representing the number of operations. O lines follow, each containing either push or pop operations. push operation will be of form push x, where x is the parameter of push as defined above. The pop operation will be of form pop x, where x is the returned element.

Output Format
For each test case, output one of the following:

If it is a stack

LIFO

If it is queue

FIFO

If it is a priority queue

PQ

If it can be more than one of the above

NOT SURE

If it is none of the above

IMPOSSIBLE

# PALINDROME

Problem Statement
A word is a Palindrome if it is spelled the same backward as forward. Examples include madam, Racecar. Given a string, determine if it is a palindrome or not.

Input
The input will be read from a file. The file will have a single word. Each character in the word will be an alphabet.

Output
Output TRUE if the word is a palindrome. FALSE otherwise.

Estimated Time
10-15 minutes
Input file reading Instructions:

The input is read from a file. The filename/path of the file is passed to your program as the first command-line argument. There is no fixed name for the input file. Do not hardcode the input file name.
