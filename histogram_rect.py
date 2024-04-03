def prev_small_elem_index(arr):
    stack = []  # This will store indices of elements
    pse_index = []  # To store the index of the Previous Smaller Element for each element
    for i in range(len(arr)):
        # Remove elements from the stack while the current element is less than or equal to 
        # the element at the index at the top of the stack
        while stack and arr[i] <= arr[stack[-1]]:
            stack.pop()
        # If stack is empty, it means there is no previous smaller element
        if not stack:
            pse_index.append(-1)
        else:
            # The top of the stack is the index of the previous smaller element
            pse_index.append(stack[-1])
        # Push the current index onto the stack
        stack.append(i)
    return pse_index

def next_small_elem_index(arr):
    stack = []  # This will store indices of elements
    nse_index = [-1] * len(arr)  # Initialize all indices as -1
    for i in range(len(arr)-1, -1, -1):
        # Remove elements from the stack while the current element is less than or equal to 
        # the element at the index at the top of the stack
        while stack and arr[i] <= arr[stack[-1]]:
            stack.pop()
        # If stack is not empty, the top of the stack is the index of the next smaller element
        if stack:
            nse_index[i] = stack[-1]
        # Push the current index onto the stack
        stack.append(i)
    return nse_index
        

def max_rect_area(arr):
    pse,nse=prev_small_elem_index(arr),next_small_elem_index(arr)
    area=[]
    for i in range(len(arr)):
        area.append((nse[i]-pse[i]-1)*arr[i])
    return max(area)

arr=[1,3,5,4,6,7,2]
print(max_rect_area(arr))