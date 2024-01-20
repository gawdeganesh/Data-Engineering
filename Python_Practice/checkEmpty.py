def chcekEmpty(input,pattern):
    if len(input)==0 and len(pattern)==0:
        return 'true'
    
    if len(pattern)==0:
        return 'false'
    
    index = 0
    while(len(input))>0:
        if input[index:index+len(pattern)] == pattern:
            print(f"string found at index {index}")
            input= input[0:index]+input[index+len(pattern):]
            index=0
        else:
            index +=1    

    if len(input)==0:
        return 'true'
    else :
        return 'false'
        

# Driver program
if __name__ == "__main__":
    input ='GEEGEEKSKS'
    pattern ='GEEKS'
    print (chcekEmpty(input, pattern))