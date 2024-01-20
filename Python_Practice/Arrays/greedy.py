def maxSum(arr:list[int],n:int):
    # code here
    arr.sort()
    
    list = []
    sum = 0
    i=0
    j=n-1
    counter = 0
    
    while (counter < n):
        if counter%2 ==0:
            list.append(arr[i])
            i+=1
        else:
            list.append(arr[j])
            j-=1
        
        counter+=1
        
    for ele in range(0,n-1):
        sum += abs(list[ele+1]-list[ele]) 

    sum+= list[n-1]-list[0]
    print(sum)   

n=4
a=[1,2,4,8]
maxSum(a,n)