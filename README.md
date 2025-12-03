#Algorithm Chosen: 
I chose the binary search algorithm. I chose a searching algorithm specifically because many applications, either general websites or even games have aspects where searching an element is required. I chose binary search because it is generally more efficient than linear search in time complexity, and that can be especially important in larger and more complicated codes. 

## Problem Breakdown: 
#Decomposition: 
* divide the array length by two to get a variable representing the middle element 
* divide the array left of the middle element or the array right of the element into half depending on if the target number is less than the mid pointer or greater than the mid pointer respectively
* continue dividing each sub-array until target is found 

#Pattern Recognition: 
* array has to be sorted for binary search to work 
* if the target number is greater than the current middle element (set lower pointer to be mid + 1)
* if target number is less than the current middle element (set upper pointer to be mid)
* keep dividing each sub-array by two to get the new current middle element 

#Abstraction: 
* the user does not need to see the part of the code that checks for edge cases and constraints or the general code structure
* user should see the left, mid, right pointers for each iteration
* finally, user should see the index that the target number was found or display text saying the number was not found

#Algorithm: 
* input: an array of integer numbers and an integer target number 
* output: the index that the target number is at, visually show where the target number is and how it was found
* constraints: target number should be between -2**31 and 2**31 - 1, length of array should not be more than 1000, number input has to be an integer 

#Flow Chart: 

![FLow Chart](https://github.com/michelleguo87/Final-Project-Binary-Search-Algorithm/blob/ec38db244550cfad083fc6572124e6bd80a3d314/Binary%20Search%20Flow%20Chart.jpeg)

## Demo Video: 

## Hugging Face Link: 

## Author and Acknolwedgement: 
Author: Michelle Guo 
