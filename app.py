import gradio as gr 

def binarySearch(nums, target): 
   """
      parameter: nums is a list of numbers in ascending order, target is an integer 
      output: index if target is found, -1 if not found 
   """ 
   #initalize index of upper and lower bounds 
   upper = len(nums)-1
   lower = 0 
   while upper > lower:  
      mid = (lower + upper)//2
      iteration += 1 
      #show left, right, middle pointers as text each iteration 
      pointers = ""
      pointers += "<p>Iteration: " + str(iteration) + "</p>" #AI Disclaimer: asked how html works in gradio and for examples on how to implement colors
      pointers += "<p style='color:orange;'>left bound index: " + str(left) + "</p>" 
      pointers += "<p style='color:green;'>middle index: " + str(mid) + "</p>"
      pointers += "<p style='color:blue;'>right bound index: " + str(right) + "</p>"

      yield pointers 
      if array[mid] == target:
         yield "<p style='color:green;'>Target number found at index: " + str(mid) + "</p>"
         return 
      elif array[mid] < target:
         left = mid + 1
      elif array[mid] > target: 
         right = mid - 1 
    yield "<p style='color:red;'>Target number not found</p>"
    return 

with gr.Blocks() as demo: 
   title_text = gr.HTML("<p style= 'font-size: 20px;'>Binary Search Visualization</p>")

    #initial visuals
    array_input = gr.Textbox(label = "Please enter an array of integers that has at least one number and less than 1000 numbers, seperated by commas. Eg: 1,2,3")  
    target_input = gr.Number(label = "Please Enter the Target Number") 

    #buttons 
    startButton = gr.Button("Start Search")
    resetButton = gr.Button("Reset Search")

    def run(array, target):
       array_list = []
       for char in array.split(","): #AI Disclaimer: asked prompt: how to convert string into list of integers while ignoring commas.
          array_list.append(char) 
        #display different steps and colored array each iteration
       steps = ""
       for step in binarySearch(target, array_list): 
          steps += step
          time.sleep(2) #Learned from gradio streaming output document example 
          yield steps

    #reset the search 
    def reset():
       return "", "" 

   startButton.click(run, inputs = [array_input, target_input], outputs = [output_steps])
   resetButton.click(reset, outputs = [output_steps]) 

demo.launch() 
