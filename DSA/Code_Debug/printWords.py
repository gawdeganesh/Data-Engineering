def printWords(num:int)-> str:
    dict = { 1 : 'One',
             2 : 'Two',
             3 : 'Three',
             4 : 'Four',
             5 : 'Five',
             6 : 'Six',
             7 : 'Seven',
             8 : 'Eight',
             9 : 'Nine',
             0 : 'Zero'

    }
    n = str(num)
    word_list = []

    for ele in n:
        if int(ele) in dict:
            word_list.append(dict[int(ele)])

    print(' '.join(word_list))

printWords(91)
printWords(1221)
printWords(9854)
printWords(1001)