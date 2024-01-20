def drawPattern(N):
    if N < 1:
        return None

    # for i in range(1,height+1):
    #     for j in range(1,i+1):
    #         print(i, end = " ")
    #     print("")   # this is important

    # s = ""
    # for i in range(1,N+1):
    #     s += str(i)+ " "
    #     print (s)

    # for i in range(1,N+1):
    #     new_string = (str(i)+ " ") * i
    #     print (new_string)

    # * * * * *
    # * * * *
    # * * *
    # * *
    # *

    # for i in range(N,0,-1):
    #     new_string = ('*'+ " ") * i
    #     print (new_string)

    # 1 2 3 4 5
    # 1 2 3 4
    # 1 2 3
    # 1 2
    # 1
    # for i in range(1,N+1):
    #     for j in range(1,(N-i)+2):
    #         print(j, end =" ")
    #     print()    # this is important

    #     *
    #    ***
    #   *****
    #  *******
    # *********

    # new_string = ""
    # for i in range(1, N+1):
    #     new_string = " "*(N-i) + "*"*(2*i-1) + " "*(N-i)
    #     print(new_string)

    # *********
    #  *******
    #   *****
    #    ***
    #     *

    # new_string = ""
    # for i in range(1, N+1):
    #     new_string = " "*(i-1) + "*"*(2*(N-i)+1) + " "*(i-1)
    #     print(new_string)

    # *
    # **
    # ***
    # ****
    # *****
    # ****
    # ***
    # **
    # *
    # for i in range(1,2*N):
    #     if i<= N:
    #         print("*"* i)
    #     else:
    #         print("*"*(2*N -i))

    # 1
    # 0 1
    # 1 0 1
    # 0 1 0 1
    # 1 0 1 0 1

    # for i in range(1,N+1):
    #     count = i
    #     for j in range(1,i+1):
    #         print(count%2, end =" ")
    #         count += 1
    #     print()

    # for i in range(1,N+1):
    #     for j in range(1,i+1):
    #         if (i+j)%2==0:
    #             print("1 ",end="")
    #         else:
    #             print("0 ",end="")
    #     print()

    # 1             1
    # 1 2         2 1
    # 1 2 3     3 2 1
    # 1 2 3 4 4 3 2 1
    # for i in range(1,N+1):
    #         #number
    #     for j1 in range(1,i+1):
    #         print(j1,end=" ")
    #         #space
    #     for j2 in range(2*N-2*i):
    #         print(" ",end=" ")
    #         #number
    #     for j3 in range(i,0,-1):
    #         print(j3,end=" ")
    #     print()
    # 1
    # 2 3
    # 4 5 6
    # 7 8 9 10
    # 11 12 13 14 15
    # counter = 1
    # for i in range(1,N+1):
    #     for j in range(1,i+1):
    #         print(counter, end=" ")
    #         counter+=1
    #     print()

    # A
    # A B
    # A B C
    # A B C D
    # A B C D E

    # for i in range(1, N+1):
    #     for j in range(1, i+1):
    #         print(chr(ord('A')+j-1), end=" ")
    #     print()

    # A B C D E
    # A B C D
    # A B C
    # A B
    # A

    # for i in range(1,N+1):
    #     for j in range(1,(N-i)+2):
    #         print(chr(ord('A')+j-1), end=" ")
    #     print()
    # A
    # B B
    # C C C
    # D D D D
    # E E E E E

    # for i in range(1,N+1):
    #     print((chr(ord('A')+i-1) + " ")*i)

    #       A
    #     A B A
    #   A B C A B
    # A B C D A B C

    # for i in range(1,N+1):
    #     for j in range(1,(N-i)+1):
    #         print(" ", end=" ")
    #     for k in range(1,i+1):
    #         print(chr(ord('A')+k-1), end=" ")
    #     for l in range(1,i):
    #         print(chr(ord('A')+l-1), end=" ")
    #     for m in range(1,(N-i)+1):
    #         print(" ", end=" ")
    #     print()
    # E
    # D E
    # C D E
    # B C D E
    # A B C D E
    # for i in range(N, 0, -1):
    #     for j in range(i,N+1):
    #          print(chr(ord('A')+j-1), end=" ")
    #     print()

    for i in range(1, N + 1):
        for j in range(1, i + 1):
            print(chr(ord("A") + j + (N - i) - 1), end=" ")
        print()


height = int(input("enter height of the rectangle: \n"))

print(f"the pattern is \n ")
drawPattern(height)
