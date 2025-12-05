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

## Testing and Verification: 
* I tried testing the colored array updating, and the app ended up displaying each iteration of the colored array, instead of constantly updating one. ChatGPT suggested to yield the outputs seperately as a tuple, and after changing what the code yields, the code created 1 array.
* after trying different combinations of numbers, I found that the code did not account for some edge cases like negative numbers, especially because the run function has to convert the string input into a list of numbers. It also did not account for double digit numbers at first before I used the .split() function.
* While trying different combinations of arrays, I realized that I did not account for scenarios where the input array is not sorted, I then adjusted by using the sort function
* After testing the app on a different browser, I realized if the background was white, parts of the array will not be seen, so I updated it the text to adjust to backgrounds after asking ChatGPT how that could be done

##Test Screenshots: 
![Regular Case](https://github.com/michelleguo87/Final-Project-Binary-Search-Algorithm/blob/main/Regular%20Case.png)
![Searching for Negative Number](https://github.com/michelleguo87/Final-Project-Binary-Search-Algorithm/blob/main/Searching%20for%20Negative%20Number.png)
![Target Number Not Found](https://github.com/michelleguo87/Final-Project-Binary-Search-Algorithm/blob/main/Target%20Number%20Not%20Found.png)
![Letters Input](https://github.com/michelleguo87/Final-Project-Binary-Search-Algorithm/blob/main/Letters%20Entered%20Instead%20of%20Numbers%20Case.png)
![Negative Numbers in Array](https://github.com/michelleguo87/Final-Project-Binary-Search-Algorithm/blob/main/Handles%20Negative%20Numbers.png)

## Demo Video: 
![App Demo](https://github.com/michelleguo87/Final-Project-Binary-Search-Algorithm/blob/main/Demo%20Video%20-%20Binary%20Search.mov) 
* may have to download raw video to view

## Hugging Face Link: 

https://huggingface.co/spaces/michelleg87/Binary-Search-Algorithm-Visual

## Author and Acknolwedgement: 
Author: Michelle Guo 

AI Use Disclosure: 
* I used ChatGPT throughout the project to help with my code writing process. Here is a general summary of what I used it for.
* I used ChatGPT to learn how to use the gradio components better, specifically I would ask ChatGPT for examples of how to implement html into the app because the gradio documentation often lacked examples.
* I specifically asked ChatGPT how buttons, button events, html and streaming works
* Asked ChatGPT how to account for different background colors, while allowing the code to adapt accordingly
* There were times where the code would lead to an error related to gradio and I was unsure of what was causing that error. So I input into ChatGPT the specific error, like a streaming error and adjusted my code accordingly.
* There was also an error where the run function was not returning enough outputs, but I was not sure how outputs were counted within the blocks, so I asked ChatGPT to explain what that error really meant.
* From ChatGPT, I learned a lot about how Gradio can sometimes function very differently from normal python code. For exmaple, the arguments that have to go into the button click event, have to be gradio components, or the program will not work
* Whenever I asked ChatGPT for help with parts of the code, I made sure to understand what ChatGPT was telling me and to test out the code after implementing any changes, as ChatGPT can often get the concept right, but suggests code that leads to errors. 
