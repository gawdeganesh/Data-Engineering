def printPrime(num1:int, num2:int)->int:

    for num in range(num1, num2+1):
        # find the factors of num1 and if the count of factors are 2 then it is a prime number
        fact_cnt = 0
        
        # check factors 
        for i in range(1,num+1):
            if num%i==0:
                fact_cnt+=1

        if fact_cnt == 2:
            print(num, end=' ')

    print()    

printPrime(10,20)
printPrime(1,20)