input_string = input()
output_string = [] 
space_flag = False # Flag to check if spaces have occured 
  
for index in range(len(input_string)): 
  
    if input_string[index] != ' ': 
        if space_flag == True: 
            if (input_string[index] == '.' 
                    or input_string[index] == '?' 
                    or input_string[index] == ','): 
                pass
            else: 
                output_string.append(' ') 
            space_flag = False
        output_string.append(input_string[index]) 
    elif input_string[index - 1] != ' ': 
        space_flag = True
  
print (''.join(output_string)) 
