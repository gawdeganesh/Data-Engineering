def anagram(word1:str, word2:str)-> bool:

    dict = {char : word1.lower().count(char) for char in word1.lower()}

    if len(word1) !=len(word2):
        return False

    for char in word2.lower():
        if char not in dict or dict[char]==0:
            return False
        
        dict[char]-=1

    return True



word1 = 'Anagram'
word2 = 'agraman'
print(anagram(word1, word2))
