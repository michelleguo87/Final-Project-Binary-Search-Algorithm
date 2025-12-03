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
      if nums[mid] == target: 
         return mid
      elif nums[mid] < target: 
         lower = mid + 1 
      elif nums[mid] > target: 
         upper = mid - 1
   return  

with gr.Blocks() as demo: 
   title_text = gr.HTML("<p style= 'font-size: 20px;'>Binary Search Visualization</p>")

    #initial visuals
    array = gr.Textbox(value = "1, 2, 5, 7, 8, 10, 12, 15, 16", label = "Array") 
    target_input = gr.Number(label = "Please Enter the Target Number") 

    #buttons 
    startButton = gr.Button("Start Search")
    resetButton = gr.Button("Reset Search")

