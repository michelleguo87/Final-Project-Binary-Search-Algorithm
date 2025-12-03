#Algorithm Chosen: 
I chose the binary search algorithm. I chose a searching algorithm specifically because many applications, either general websites or even games have aspects where searching an element is required. I chose binary search because it is generally more efficient than linear search in time complexity, and that can be especially important in larger and more complicated codes. 

## Problem Breakdown: 
#Decomposition: 
* divide the array length by two to get a variable representing the middle element 
* divide the array left of the middle element or the array right of the element into half
* continue dividing each sub-array until target is found 

#Pattern Recognition: 
* if the target number is greater than the current middle element (set lower pointer to be mid + 1)
* if target number is less than the current middle element (set upper pointer to be mid)
* keep dividing each sub-array by two to get the new current middle element 

#Abstraction: 
* the user does not need to see the part of the code that checks for edge cases and constraints or the general code structure
* user should see the current part of the array the code is looking at, the current middle element and the target number 

#Algorithm: 
* input: an array of integer numbers and an integer target number 
* output: the index that the target number is at, visually show where the target number is and how it was found
* constraints: 

#Flow Chart: 
![FLow Chart](Binary Search FLow Chart.jpeg) 

## Demo Video: 

## Hugging Face Link: 

## Author and Acknolwedgement: 
Author: Michelle Guo 
