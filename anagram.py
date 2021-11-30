def check_anagram(first_word, second_word):
    return sorted(first_word) == sorted(second_word)


print(check_anagram("neo", "one"))

