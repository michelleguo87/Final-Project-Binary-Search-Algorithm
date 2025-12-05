#AI Disclaimer: used ChatGPT throughout parts of the code

import gradio as gr
import time 

def binarySearch(target, array):
    """
       parameters: num is an integer, array is a list of integers
       constraints:
       array has to be sorted in ascending order
       -2**31 <= target <= (2**31) - 1
       1 <= len(array) <= 1000
       input has to be integers 
       output: the index that the target number is found at 
    """
    #check for constraints:
    if target < -2**31 or target > (2**31)-1:
        yield "<p style='color:red;'>Please enter another number</p>"
        return
    if len(array) < 1 or len(array) > 1000:
        yield "<p style='color:red;'>Array is too short or too long</p>"
        return 

    #initialize pointers 
    left = 0
    right = len(array) - 1
    iteration = 0 #keep track of iteration to display in app 

    
    while right >= left:
        mid = (left + right)//2
        iteration += 1 

        #colour the pointers in the array
        colored_array = ""
        color = ""
        for i in range(len(array)):
            if i == mid:
                color = "green"
            elif i == left:
                color = "orange"
            elif i == right:
                color = "blue"
            else:
                color = "white" 

            colored_array += "<p style='color:" + color + ";'>" + str(array[i]) + "</p>"

        #show left, right, middle pointers as text each iteration 
        pointers = ""
        pointers += "<p>Iteration: " + str(iteration) + "</p>" #AI Disclaimer: asked how html works in gradio and for examples on how to implement colors
        pointers += "<p style='color:orange;'>left bound index: " + str(left) + "</p>" 
        pointers += "<p style='color:green;'>middle index: " + str(mid) + "</p>"
        pointers += "<p style='color:blue;'>right bound index: " + str(right) + "</p>"

        yield colored_array, pointers #AI Disclaimer: asked how to ensure the colored array is only shown at the top and is updated rather than displaying an array every iteration

        #binary search algorithm 
        if array[mid] == target:
            yield colored_array, "<p style='color:green;'>Target number found at index: " + str(mid) + "</p>"
            return 
        elif array[mid] < target:
            left = mid + 1
        elif array[mid] > target: 
            right = mid - 1 
    yield colored_array, "<p style='color:red;'>Target number not found</p>"
    return


#app code: 
with gr.Blocks() as demo: 
    title_text = gr.HTML("<p style= 'font-size: 20px;'>Binary Search Visualization</p>")

    #Ask for user input: 
    array_input = gr.Textbox(label = "Please enter an array of integers that has at least one number and less than 1000 numbers, seperated by commas. Eg: 1,2,3") 
    target_input = gr.Number(label = "Please Enter the Target Number") 

    #buttons 
    startButton = gr.Button("Start Search")
    resetButton = gr.Button("Reset Search")

    #displays
    with gr.Row():
        colored_array = gr.HTML(label = "Array Visual") 
        output_steps = gr.HTML(label = "Steps")
    
    #running the binary search
    def run(array, target):
        array_list = []
        for char in array.split(","): #AI Disclaimer: asked prompt: how to convert string into list of integers while ignoring commas.
            if "-" in char:
                if char[1:].isdigit() == False:            
                    yield "<p style ='color:red;'>Please enter numbers and commas only</p>", ""
                    return #accounts for negative numbers
                else:
                    array_list.append(int(char))
    
            elif char.isdigit() == False:
                yield "<p style ='color:red;'>Please enter numbers and commas only</p>", ""
                return
            else: 
                array_list.append(int(char))
        array_list.sort() #Sort function in case user inputs an array that is not sorted in ascending order 

        #display different steps and colored array each iteration
        steps = ""
        for arr, step in binarySearch(target, array_list): 
            steps += step
            time.sleep(2) #Learned from gradio streaming output document example 
            yield arr, steps

    #reset the search 
    def reset():
        return "", "" 

    #button events 
    startButton.click(run, inputs = [array_input, target_input], outputs = [colored_array, output_steps])
    resetButton.click(reset, outputs = [colored_array, output_steps]) 

demo.launch(share = True) 
