# https://leetcode.com/problems/top-k-frequent-words/

from collections import Counter

def top_k_frequent(words, k):

    word_counts = Counter(words)

    # Sort by (-frequency, word) to achieve the desired ordering
    unique_words = sorted(word_counts.items(), key=lambda item: (-item[1], item[0]))
    print(unique_words)

    return [word for word, _ in unique_words[:k]]

# Example usage (same as before)
words1 = ["i","love","leetcode","i","love","coding"]
k1 = 2
words2 = ["the","day","is","sunny","the","the","the","sunny","is","is"]
k2 = 4

print(top_k_frequent(words1, k1))  
print(top_k_frequent(words2, k2))  
