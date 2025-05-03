## CS50P

### Glossery

*python* - an interperter that translates words to machine language
*function* - an action or verb for the program to do something
*arguments* - an imput to a function that influences its behavior
*bugs* - a mistake in a program
*syntax error* - a mistake made within the keyboard
*return values* - result of a function
*variables* - a container for some value stored in the computers memory
*comments* - notes to yourself or others in the code
*pseudocode* - a way to outline your code in advance
*string* - a swquence of text
*parameters* - like arguments its an input to a function but viewed somewhere else from the code instead of within the function
*interactive mode* - writing python code and instantly running
*def* - define, keyword to create a function
*scope* - a variable that only exist in the context where it was defined


## Leetcode Problems

### Two Sum (Time taken: 5 m 40 s)
- Instead of using a brute force method to check every pair of elements (which would be too slow), I chose to use a hashmap to make the code more efficient.
- The approach:
  1. For each element, find the complement of the target by subtracting the current element.
  2. Check if the complement exists in the hashmap.
  3. If the complement is not in the hashmap, add the current element and its index to the hashmap.
  4. If the complement is found, return both its index and the index of the current element.
- This reduces the time complexity because we can return early when the solution is found, avoiding the need to iterate through the entire list. The worst-case scenario is when the solution is at the very end.

### Palindrome Number (Time taken: 16 m 1 s)
- A easy solution would be to convert the input int into a string and use a two-pointer approach to check the front and back. But I chose to keep the input as an int for the added challenge.
- The approach:
  1. Check if the input is a negative number. If it is, return false early because negative numbers cannot be palindromes.
  2. Create a copy of the original input to avoid altering it accidentally.
  3. Reverse the number using an [arithmetic method](https://www.programiz.com/python-programming/examples/reverse-a-number).
  4. Compare the reversed number with the original. If they are the same, the number is a palindrome; otherwise, return false.

### (Optional) Best Time to Buy and Sell Stock (Time taken: 17 m 19 s)
- Using the [sliding window](https://www.geeksforgeeks.org/window-sliding-technique/) technique with an aim for that time complexity of O(n).
- The appreach:
  1. Keep track of the lowest price seen so far.
  2. At each step calculate profit = current price - lowest price
  3. If the calculated profit is higher than our current max profit update it to be our new max profit
  4. Time complexity of O(n) because we only pass once through the list
- after finding the answer and submitting I reviewed other's solutions, while identical in approach my code can be much more clearer and with minor optimizing such as instead of r starting at index 0 it should start at index 1. Instead of the variables being indexes they should be the elements themselves this would make the code much more cleaner and easier to understand.
- Struggled at first in putting the idea into practice but after drawing it out in ms paint it became much more clearer, I will have to get in the habit of drawing out the problems more often.


## Week 1 Reflection

### Day 1
- Learned about repo structure and a bit of practice for clean code organization
- Solved 2 Leetcode problems (Two Sum, Palindrone Number) with a bonus problem (Best Time to Buy and Sell Stock)
- Setup and worked with Git and GitHub using SSH
- Watched first CS50P lecture and practiced basic python
- Struggled with file setup
- Tried a new algorithm in sliding window technique