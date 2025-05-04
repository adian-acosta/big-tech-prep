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
*[Media Type (MIME type)](https://en.wikipedia.org/wiki/Media_type)* - A two part identifier for file formats and content formats to identify intended data format. Comparable to [filename extensions](https://en.wikipedia.org/wiki/Filename_extension[) and [uniform type identifiers](https://en.wikipedia.org/wiki/Filename_extension).
*[HHTP header](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields)* - A list of strings sent and recieved by both the client program and server on every HTTP request and response defining how information sent/received through the connection are encoded, session verification and identification of the client or their anomymity thereof (VPN or proxy masking, user-agent spoofing), how the server should handle the data, and the age of the document being downloaded


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
- The approach:
  1. Keep track of the lowest price seen so far.
  2. At each step calculate profit = current price - lowest price
  3. If the calculated profit is higher than our current max profit update it to be our new max profit
  4. Time complexity of O(n) because we only pass once through the list
- after finding the answer and submitting I reviewed other's solutions, while identical in approach my code can be much more clearer and with minor optimizing such as instead of r starting at index 0 it should start at index 1. Instead of the variables being indexes they should be the elements themselves this would make the code much more cleaner and easier to understand.
- Struggled at first in putting the idea into practice but after drawing it out in ms paint it became much more clearer, I will have to get in the habit of drawing out the problems more often.

### Valid Parentheses (Time taken: 9 m 13 s)
- Used a stack to keep track of each opening bracket encountered and used it to pair with any closing brackets that were found within the string
- The approach:
  1. Check if the current pointer is a opening bracket if so push it on to the stack and continue along the string
  2. See if the stack is empty, if the loop continues and the current pointer is not a opening bracket then its a closing bracket. If the stack empty then return false as there is no pair
  3. If the stack is not empty and the current pointer is not a opening bracket then match the element with the top of the stack and pop it, if they match then continue otherwise return false
  4. After looping through the string check if the stack is empty, if empty then each bracket was paried and can return true. Otherwise return false

### Merge Two Sorted List (Time taken: 53 m 0 s)
- Merging the two sorted list using both iteration and recursion for a time complexity of O(n + m)
- The approach (iteration):
  1. Create a dummy head with a temp that will move forward finding which value to add to the list
  2. Add a loop that will add on to temp while list1 **or** list2 are not at the end
  3. Compare the head of both list1 and list2 and which ever is the smallest value add that to temp, if both equal any could be picked
  3. Move the list that was chosen to add to temp forward then move temp forward also
  4. Repeat till one of the list is at the end then exit the loop
  5. If there is a list that is still not empty we can safetly assume that we can add the rest of that list on to temp while still being in the correct order since these list are already sorted
  6. Move the dummy head forward once then return dummy
- The approach (recursive):
  1. Setup a base case where if one of the list is empty then return the other one
  2. Compare the list for finding which one has the smallest first element to be returned at the end
  3. Move the list that was chosen foward by recursively calling the function with the inputs being the chosen list moved foward while the other remains unchanged
  4. Keep moving forward until either list is at their last element
- The iterative methods makes a lot more sense to me and it's the one I prefer. Struggled trying to grasp the recursive method as I had to look into solution for this one and while I understand it I don't yet have a full grasp of it yet.

## Week 1 Reflection

### Day 1
- Learned about repo structure and a bit of practice for clean code organization
- Solved 2 Leetcode problems (Two Sum, Palindrone Number) with a bonus problem (Best Time to Buy and Sell Stock)
- Setup and worked with Git and GitHub using SSH
- Watched first CS50P lecture and practiced basic python
- Struggled with file setup
- Tried a new algorithm in sliding window technique

### Day 2
- Learned stack logic with valid parentheses
- Reviewed recursion in merge sort problem
- Completed CS50P second lecture
- Struggled with the merge sort Leetcode problem with working with linked list and using recursion